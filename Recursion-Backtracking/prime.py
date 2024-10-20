import math

i = 20

def all_primes_up_to(n):
    # primes = []
    # for i in range(2, n + 1):
    #     is_prime = True
        for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                # is_prime = False
                # break
        # if is_prime:
        #     primes.append(i)
                return "Not Prime"
        return "Prime"

print(all_primes_up_to(17))
