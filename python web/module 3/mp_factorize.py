from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor
from time import time

def timer(func):
    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time() - start_time
        print(f'program complete in : {end_time}')
        return result
    return inner

@timer
def factorize(*numbers):
    # YOUR CODE HERE
    result = []
    for number in numbers:
        temp = []
        for i in range(1, number+1):
            if not (number % i):
                temp.append(i)
        result.append(temp)
        
    return result
       
cpu = cpu_count()


# with ProcessPoolExecutor(max_workers=cpu) as executor:
#     a, b, c, d  = list(executor.map(factorize, [128, 255, 99999, 10651060]))
    
a, b, c, d  = factorize(128, 255, 99999, 10651060)  
# print(f'a: {a}', f'b: {b}', f'c: {c}', f'd: {d}', sep='\n')

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]