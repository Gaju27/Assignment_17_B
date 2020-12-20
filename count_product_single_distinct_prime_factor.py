# Count pairs whose product contains single distinct prime factor
# Input: arr[] = {1, 2, 3, 4}
# Output: 4
# Explanation:
# Pairs having single distinct prime factor in their product is as follows:
# arr[0] * arr[1] = (1 * 2) = 2. Therefore, the single distinct prime factor is 2.
# arr[0] * arr[2] = (1 * 3) = 3. Therefore, the single distinct prime factor is 3.
# arr[0] * arr[3] = (1 * 4) = 22 Therefore, the single distinct prime factor is 2.
# arr[1] * arr[3] = (2 * 4) = 8 23 Therefore, the single distinct prime factor is 2.
# Therefore, the required output is 4.
#
# Input: arr[] = {2, 4, 6, 8}
# Output: 3


# Python3 program to implement
# the above approach

# Function to find a single
# distinct prime factor of N
def singlePrimeFactor(N):
    # Stores distinct
    # prime factors of N
    disPrimeFact = {}

    # Calculate prime factor of N
    for i in range(2, N + 1):
        if i * i > N:
            break

        # Calculate distinct
        # prime factor
        while (N % i == 0):
            # Insert i into
            # disPrimeFact
            disPrimeFact[i] = 1

            # Update N
            N //= i

    # If N is not equal to 1
    if (N != 1):
        # Insert N into
        # disPrimeFact
        disPrimeFact[N] = 1

    # If N contains a single
    # distinct prime factor
    if (len(disPrimeFact) == 1):
        # Return single distinct
        # prime factor of N
        return list(disPrimeFact.keys())[0]

    # If N contains more than one
    # distinct prime factor
    return -1


# Function to count pairs in the array
# whose product contains only
# single distinct prime factor
def cntsingleFactorPair(arr, N):
    # Stores count of 1s
    # in the array
    countOf1 = 0

    # mp[i]: Stores count of array elements
    # whose distinct prime factor is only i
    mp = {}

    # Traverse the array arr[]
    for i in range(N):

        # If current element is 1
        if (arr[i] == 1):
            countOf1 += 1
            continue

        # Store distinct
        # prime factor of arr[i]
        factorValue = singlePrimeFactor(arr[i])

        # If arr[i] contains more
        # than one prime factor
        if (factorValue == -1):
            continue

        # If arr[i] contains
        # a single prime factor
        else:
            mp[factorValue] = mp.get(factorValue, 0) + 1

    # Stores the count of pairs whose
    # product of elements contains only
    # a single distinct prime factor
    res = 0

    # Traverse the map mp[]
    for it in mp:
        # Stores count of array elements
        # whose prime factor is (it.first)
        X = mp[it]

        # Update res
        res += countOf1 * X + (X * (X - 1)) // 2

    return res

# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    N = len(arr)

    print(cntsingleFactorPair(arr, N))