def isSumTwo(numbers, sum):
    seen = set()
    for num in numbers:
        complement = sum - num
        if complement in seen:
            return True
        seen.add(num)
    return False


def maxNegativeRepr(numbers):
    num_set = set(numbers)
    max_positive = -1
    
    for num in num_set:
        if num > 0 and -num in num_set:
            max_positive = max(max_positive, num)
    
    return max_positive

