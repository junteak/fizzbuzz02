

def fizzbuzz_covert(number):
    if number % 3 == 0:
        return 'Fizz'

    if number % 5 == 0:
        return 'Buzz'

    if number % 15 == 0:
        return 'FizzBuzz'

    return str(number)


for number in range(1, 101):
    print(fizzbuzz_covert(number))

# アラートを出すための。定義。
assert fizzbuzz_covert(3) == 'Fizz'

assert fizzbuzz_covert(5) == 'Buzz'

assert fizzbuzz_covert(15) == 'FizzBuzz'
