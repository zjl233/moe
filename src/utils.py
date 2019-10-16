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
