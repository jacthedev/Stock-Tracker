def second_smallest(numbers):
    smallest = numbers[0]
    second = numbers[0]
    for n in numbers:
        if n < smallest:
            second = smallest
            smallest = n
    return second

print(second_smallest([5, 2, 9]))   # should be 5
print(second_smallest([2, 5, 9]))   # should be 5
print(second_smallest([3, 1]))      # should be 3