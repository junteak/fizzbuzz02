number = 3


def fizzbuzz_covert(number):
    if number % 3 == 0:
        return 'Fizz'


print(fizzbuzz_covert(number))

assert fizzbuzz_covert(3) == 'Fizz'
