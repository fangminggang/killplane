import time

def logit(funs):
    def logs():
        funs()
        print('logit函数')
    return logs


def fun():
    print('fun函数')

funs = logit(fun)
funs()

class zhuangshi():
    def __call__(self, *args, **kwargs):



