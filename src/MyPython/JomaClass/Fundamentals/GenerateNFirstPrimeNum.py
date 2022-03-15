def generate_n_first_prime_num(request):
    found = 0
    upper_bound = 100
    last_prime = 0
    while found < request:
        lower_bound = last_prime + 1
        for i in range(lower_bound, upper_bound):
            if isPrime(i):
                print(i)
                found += 1
                last_prime = i
            if(found == request):
                break
        upper_bound += 100

# function to check if a given number is prime
def isPrime(n):
    # since 0 and 1 is not prime return false.
    if n == 1 or n == 0:
        return False

    # Run a loop from 2 to n-1
    for i in range(2, n):
        # if the number is divisible by i, then n is not a prime number.
        if n % i == 0:
            return False

    # otherwise, n is prime number.
    return True


generate_n_first_prime_num(1000000)
