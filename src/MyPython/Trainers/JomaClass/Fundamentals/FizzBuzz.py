def fizz_buzz(f, b, n):
    c = 0
    while c <= n:
        if c % f == 0 and c % b == 0:
            print("fizzbuzz")
        elif c % f == 0 and not c % b == 0:
            print("fizz")
        elif c % b == 0 and not c % f == 0:
            print("buzz")
            # elif(not c%b == 0 and not c%f == 0  ):
        else:
            print(c)
        c += 1
