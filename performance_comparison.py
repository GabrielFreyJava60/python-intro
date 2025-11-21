import time
import random
from main import isSumTwo, maxNegativeRepr


def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, (end_time - start_time) * 1000


def test_isSumTwo_performance():
    print("=== Testing isSumTwo Performance ===\n")
    
    test_cases = [
        (100, "Small dataset"),
        (1000, "Medium dataset"),
        (10000, "Large dataset"),
        (100000, "Very large dataset")
    ]
    
    for size, description in test_cases:
        numbers = [random.randint(-1000, 1000) for _ in range(size)]
        target_sum = random.randint(-2000, 2000)
        
        result, elapsed_time = measure_time(isSumTwo, numbers, target_sum)
        print(f"{description} (n={size}): {elapsed_time:.4f} ms - Result: {result}")
    
    print()


def test_maxNegativeRepr_performance():
    print("=== Testing maxNegativeRepr Performance ===\n")
    
    test_cases = [
        (100, "Small dataset"),
        (1000, "Medium dataset"),
        (10000, "Large dataset"),
        (100000, "Very large dataset")
    ]
    
    for size, description in test_cases:
        numbers = [random.randint(-1000, 1000) for _ in range(size)]
        
        result, elapsed_time = measure_time(maxNegativeRepr, numbers)
        print(f"{description} (n={size}): {elapsed_time:.4f} ms - Result: {result}")
    
    print()


def analyze_complexity():
    print("=== Time Complexity Analysis ===\n")
    print("isSumTwo: O(n)")
    print("- Uses a set to track seen numbers")
    print("- Single pass through the list")
    print("- Set lookup is O(1) average case")
    print()
    print("maxNegativeRepr: O(n)")
    print("- Converts list to set: O(n)")
    print("- Single iteration through set: O(n)")
    print("- Set membership check is O(1) average case")
    print()


if __name__ == "__main__":
    test_isSumTwo_performance()
    test_maxNegativeRepr_performance()
    analyze_complexity()

