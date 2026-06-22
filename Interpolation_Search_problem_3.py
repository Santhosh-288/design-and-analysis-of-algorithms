import random
import time

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    probes = 0

    while low <= high and arr[low] <= target <= arr[high]:

        probes += 1

        if low == high:
            if arr[low] == target:
                return low, probes
            return -1, probes

        if arr[high] == arr[low]:
            break

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if pos < low or pos > high:
            break

        if arr[pos] == target:
            return pos, probes

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, probes


print("\nINTERPOLATION SEARCH ON USER DEFINED DATASETS")
print("-" * 50)

print("\nChoose Dataset Type")
print("1. Uniform Distribution")
print("2. Non-Uniform Distribution")

choice = int(input("Enter choice: "))

print("\nData Creation Method")
print("1. Manual Input")
print("2. Random Generation")

method = int(input("Enter choice: "))

# DATASET CREATION

if method == 1:

    n = int(input("Enter number of elements: "))

    arr = list(map(int, input("Enter elements: ").split()))

else:

    n = int(input("Enter dataset size: "))

    if choice == 1:
        # Uniform distribution
        arr = sorted(random.sample(range(1, n * 10), n))

    else:
        # Non-uniform distribution
        arr = sorted([random.randint(1, 100) ** 2 for _ in range(n)])

print("\nDataset:")
print(arr)

# SORT CHECK

if arr != sorted(arr):

    print("\nDataset is not sorted.")
    sort_choice = input("Sort before searching? (y/n): ")

    if sort_choice.lower() == 'y':
        arr.sort()
        print("Array sorted.")

# SEARCH

key = int(input("\nEnter search key: "))

start = time.perf_counter()

index, probes = interpolation_search(arr, key)

end = time.perf_counter()

execution_time = (end - start) * 1000

# OUTPUT

print("\nRESULTS")
print("-" * 30)

if index != -1:
    print("Key Found")
    print("Index Position :", index)
else:
    print("Key Not Found")

print("Probes/Comparisons :", probes)
print("Execution Time     : {:.6f} ms".format(execution_time))

"""
sample 1 (Uniform dataset):

INTERPOLATION SEARCH ON USER DEFINED DATASETS
--------------------------------------------------

Choose Dataset Type
1. Uniform Distribution
2. Non-Uniform Distribution
Enter choice: 1

Data Creation Method
1. Manual Input
2. Random Generation
Enter choice: 2
Enter dataset size: 50

Dataset:
[27, 36, 38, 48, 62, 76, 80, 102, 111, 118, 121, 127, 133, 136, 145, 147, 163, 167, 168, 171, 175, 189, 208, 211, 213, 221, 225, 233, 237, 254, 256, 258, 273, 278, 295, 300, 308, 318, 321, 322, 343, 377, 382, 387, 394, 395, 403, 438, 495, 499]

Enter search key: 171

RESULTS
------------------------------
Key Found
Index Position : 19
Probes/Comparisons : 4
Execution Time     : 0.033000 ms

sample 2: (non uniform dataset)

INTERPOLATION SEARCH ON USER DEFINED DATASETS
--------------------------------------------------

Choose Dataset Type
1. Uniform Distribution
2. Non-Uniform Distribution
Enter choice: 2

Data Creation Method
1. Manual Input
2. Random Generation
Enter choice: 2
Enter dataset size: 50

Dataset:
[9, 16, 25, 25, 64, 64, 81, 100, 289, 361, 400, 400, 676, 900, 1024, 1089, 1225, 1225, 2116, 2401, 2601, 2601, 2704, 2809, 2916, 3249, 3249, 3364, 3721, 3844, 3969, 4096, 4356, 4489, 4900, 5184, 5929, 6084, 6561, 6724, 6889, 7056, 7056, 7056, 7396, 8100, 8281, 9216, 9409, 9604]

Enter search key: 2809

RESULTS
------------------------------
Key Found
Index Position : 23
Probes/Comparisons : 4
Execution Time     : 0.033900 ms

"""



