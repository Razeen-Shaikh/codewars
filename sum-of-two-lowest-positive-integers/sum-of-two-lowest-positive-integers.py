def sum_two_smallest_numbers(numbers):
    numbers.sort()
    numbers = filter(lambda x: x > 0, numbers)
    numbers = list(filter(lambda x: type(x) == int, numbers))
    numbers = numbers[0:2]
    return sum(numbers)
