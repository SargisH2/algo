#Decorators. printing, time, #authorization
import time

def printing(func) -> None:
    '''Print function return value'''
    def inner(*args, **kwargs):
        res=func(*args, **kwargs)
        print(res)
        return res
    return inner

#Example
@printing
def float_sum(*nums):
    return float(sum(nums))
float_sum(3,4,5)

###################

def tm(func) -> None:
    '''Print function work time'''
    def inner(*args, **kwargs):
        time0=time.time()
        func(*args, **kwargs)
        print(f"Function runs {time.time()-time0} sec")
        return func(*args, **kwargs)
    return inner

#Example
@tm
def str_sum(*nums):
    return str(sum(nums))
print(str_sum(*range(5000000)))

###################

# def Authorization(func):
#     def inner()
