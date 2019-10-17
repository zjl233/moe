import inspect
import time

debug = True


def log(*args, **kwargs):
    if not debug:
        return
    format_ = '%Y:%M:%D'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format_, value)
    with open('test.log', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def dump_args(func):
    """Decorator to print function call details - parameters names and effective values.
    """

    def wrapper(*args, **kwargs):
        func_args = inspect.signature(func).bind(*args, **kwargs).arguments
        func_args_str = ', '.join('{} = {!r}'.format(*item) for item in func_args.items())
        log(f'{func.__module__}.{func.__qualname__} ( {func_args_str} )')
        return func(*args, **kwargs)

    return wrapper
