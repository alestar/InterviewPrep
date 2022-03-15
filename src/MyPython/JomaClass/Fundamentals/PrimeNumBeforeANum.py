def prime_num_before(n):
    print(1)
    c = 2
    while (c <= n):
        for i in range(2, c):
            if (c % i) == 0:
                break
        else:
            print(c)
        c += 1

prime_num_before(11)