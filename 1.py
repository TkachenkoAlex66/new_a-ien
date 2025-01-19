import time
def timer(func):
    def my_wr():
        start_time = time.time()
        func()
        print(time.time() - start_time)
    return my_wr()
@timer
def sp():
    spisok = [i ** 2 for i in range(1,100000) if i % 2 == 0]
    print(spisok)
sp