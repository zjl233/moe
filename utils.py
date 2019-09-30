import time

debug = True


def log(*args, **kwargs):
    if not debug:
        return
        # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    # format = '%H:%M:%S'
    format_ = '%Y:%M:%D'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format_, value)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)
