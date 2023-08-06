from typing import Optional, Callable, Union
from dataclasses import dataclass
import datetime as datetimelib
import time as timelib

UTC_TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S.%f UTC"

Date = datetimelib.date
DateTime = datetimelib.datetime


@dataclass(frozen=True, order=True)
class LogTime:
    start: float
    end: float
    elapsed: float


    @classmethod
    def since(cls, __start: float):
        end = gettime()
        start = __start
        elapsed = end-start
        return cls(start=start, end=end,elapsed=elapsed)



def sleep(secs: Union[float, int]):
    return timelib.sleep(float(secs))


def gettime():
    return timelib.time()


def now():
    return datetimelib.datetime.now()


def utcnow():
    return datetimelib.datetime.utcnow()


def timestamp_factory(strformat: Optional[str] = None):
    strformat = UTC_TIMESTAMP_FORMAT if strformat is None else strformat

    def generate_timestamp():
        return now().strftime(strformat)

    return generate_timestamp


def timestamp(strformat: Optional[str] = None):
    return now().timestamp(UTC_TIMESTAMP_FORMAT if strformat is None else strformat)


def __logger_name(__file: str):
    result = __file.replace("/", ".").removesuffix(".py")
    if ".." in result:
        result = result.split("..", 1)[1]
    while result.startswith("."):
        result = result.removeprefix(".")
    return result


def __form_format_result(**config) -> Callable[[object], str]:
    if config["include_result"]:
        format_result = config["format_result"]
        message_limit = config["message_limit"]
        allow_newlines = config["allow_newlines"]
        format_base = lambda __result: str(format_result(__result))
        if message_limit:
            format_limit = lambda __result: format_base(__result)[:message_limit]
            format_mid = lambda __result: format_limit(__result)
        else:
            format_mid = lambda __result: format_base(__result)
        if allow_newlines:
            format_top = format_mid
        else:
            format_top = lambda __result: format_mid(__result).replace("\n", " ")
        result = lambda __result: f": [{format_top(__result)}]"
    else:
        result = lambda __result: ""
    return result


def __form_timestamp_generator(**config):
    timestamp_strformat = None
    if config["timestamp_strformat"]:
        timestamp_strformat = config["timestamp_strformat"]
    elif config["include_timestamp"]:
        timestamp_strformat = UTC_TIMESTAMP_FORMAT
    if timestamp_strformat is not None:
        timestamp_strformat = f"[ {timestamp_strformat} ]"

        def generate_timestamp():
            return utcnow().strftime(timestamp_strformat)

    else:

        def generate_timestamp():
            return ""

    return generate_timestamp


def __form_log_message(config: dict, func):
    func_id = func.__name__
    module_id = __logger_name(config["file"])

    form_result = __form_format_result(config)
    timestamp_generator = __form_timestamp_generator(config)

    def form_time(__elapsed: str):
        return f"( {str(__elapsed)[:12]}s )"

    def log_message(result, elapsed: str):
        args = (
            f"INFO:    ",
            timestamp_generator(),
            " ",
            form_time(elapsed),
            ": ",
            module_id,
            ".",
            func_id,
            form_result(result),
        )
        print(*args, sep="")

    return log_message


def __timelog_sync(**config):
    def sublog(func):
        log_message = __form_log_message(config=config, func=func)

        def inner(*args, **kwargs):
            start = timelib.time()
            result = func(*args, **kwargs)
            elapsed = timelib.time() - start
            log_message(result=result, elapsed=elapsed)
            return result

        return inner

    return sublog


def __timelog_async(**config):
    def sublog(func):
        log_message = __form_log_message(config=config, func=func)

        async def inner(*args, **kwargs):
            start = timelib.time()
            result = await func(*args, **kwargs)
            elapsed = timelib.time() - start
            log_message(result=result, elapsed=elapsed)
            return result

        return inner

    return sublog


def log(
    file: Optional[str],
    color: Optional[Union[str, int]] = None,
    include_result: bool = True,
    format_result: Callable[[object], str] = lambda value: value,
    message_limit: Optional[int] = None,
    include_timestamp: bool = False,
    timestamp_strformat: Optional[str] = None,
    is_async: bool = False,
    allow_newlines: bool = False,
):

    config = dict(
        file=file,
        color=color,
        message_limit=message_limit,
        format_result=format_result,
        include_result=include_result,
        timestamp_strformat=timestamp_strformat,
        include_timestamp=include_timestamp,
        allow_newlines=allow_newlines,
    )
    return (__timelog_async if is_async else __timelog_sync)(**config)


def __duration_handler(__min_duration: float):
    min_duration = float(__min_duration)

    def handle_min_duration(__logtime: LogTime):
        remainder = min_duration - __logtime.elapsed
        if remainder > 0:
            sleep(remainder)
        return None

    return handle_min_duration


def __echo_handler(func):
    name = func.__name__

    def handle_result_echo(__logtime: LogTime):
        print(f"{name} : {str(__logtime.elapsed)}s")
        return None

    return handle_result_echo


def __postprocess_handler(
    func, echo: Optional[bool] = None, min_duration: Optional[float] = None
):
    postprocesses = []
    if min_duration is not None and min_duration:
        postprocesses.append(__duration_handler(min_duration))
    if echo is not None and echo:
        postprocesses.append(__echo_handler(func))
    if postprocesses:

        def postprocess(__logtime: LogTime):
            for subprocess in postprocesses:
                subprocess(__logtime)
            return None

    else:

        def postprocess(__logtime: LogTime):
            return None

    return postprocess


def timed(
    echo: Optional[bool] = None,
    min_duration: Optional[float] = None,
    is_async: bool = False,
):
    def __timed_func(func):
        postprocess = __postprocess_handler(
            func=func, echo=echo, min_duration=min_duration
        )

        def __postprocess(__since: float):
            logtime = LogTime.since(__since)
            postprocess(logtime)

        if is_async:

            async def __inner(*args, **kwargs):
                start = gettime()
                result = await func(*args, **kwargs)
                __postprocess(start)
                return result

        else:

            def __inner(*args, **kwargs):
                start = gettime()
                result = func(*args, **kwargs)
                __postprocess(start)
                return result

        return __inner

    return __timed_func
