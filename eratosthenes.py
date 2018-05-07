# エラトステネスの篩
def sieve_of_eratosthenes(x):
    import math
    prime_list = []

    # 1. 探索リストに2から指定した値maxまでの整数を昇順で入れる。
    search_list = [i for i in range(2, x + 1)]

    # 3. 2の操作を探索リストの先頭値がmaxの平方根に達するまで行う。
    search_end_num = math.sqrt(x)
    while search_list[0] < search_end_num:
        # 2. 探索リストの先頭の数を素数リストに移動し、その倍数を探索リストから削除する。
        check_num = search_list[0]
        prime_list.append(check_num)
        for i in search_list:
            if i % check_num == 0:
                search_list.remove(i)

    # 4. 探索リストに残った数を素数リストに移動する。
    prime_list += search_list

    return prime_list


# 素数リストを取得して表示する
import time
start = time.time()

prime_list = sieve_of_eratosthenes(10000)

elapsed_time = time.time() - start
print ("time:{0}".format(elapsed_time) + "[sec]")

for prime in prime_list:
    print(prime)
