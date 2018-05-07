def deco_save_table(func):
    max_num = 0
    table = []

    def wrapper(num):
        nonlocal max_num, table

        if max_num < num:
            max_num = num
            table = func(num)
            return table
        elif max_num == num:
            return table
        else:
            part_table = [n for n in table if n < num]
            return part_table

    return wrapper


# エラトステネスの篩（高速版）
@deco_save_table
def sieve_of_eratosthenes_fast(x):
    import math
    judge_list = [True] * (x - 1)

    search_end_num = math.sqrt(x)
    check_num = 2
    while check_num < search_end_num:
        for n in range(check_num + 1, x + 1):
            if n % check_num == 0:
                judge_list[n - 2] = False
        for n in range(check_num + 1, x + 1):
            if judge_list[n - 2]:
                check_num = n
                break

    prime_list = []
    for i in range(2, len(judge_list)):
        if judge_list[i - 2]:
            prime_list += [i]

    return prime_list


# 素数リストを取得して表示する
import time
start = time.time()

prime_list = sieve_of_eratosthenes_fast(100000)

elapsed_time = time.time() - start
print ("time:{0}".format(elapsed_time) + "[sec]")

for prime in prime_list:
    print(prime)
