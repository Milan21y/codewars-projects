#https://www.codewars.com/kata/5262119038c0985a5b00029f/solutions/python
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:

        if n % i == 0:

            return False
        i += 1
    return True