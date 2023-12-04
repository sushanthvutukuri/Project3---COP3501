import time
import airlines

def insertion_sort(arr):
    """
    Implementation of the Insertion Sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    """
    Implementation of the Selection Sort algorithm.
    """
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

def processData(airports: list):
    totalDelays = []  # Initialize an empty list
    totalOnTime = []
    delayRatio = []

    # ["Statistics"]["Flights"]["# of Delays"]
    # calculate total number of delays which includes: Carrier, Late aircraft,
    # National aviation system, Security, Weather.
    for entry in airports:
        temp1 = entry["Statistics"]["Flights"]["Delayed"]
        temp2 = entry["Statistics"]["Flights"]["On Time"]
        totalDelays.append(temp1)
        totalOnTime.append(temp2)
        delayRatio.append(temp1 / temp2)

    # Use Selection Sort to sort the airports based on the total number of delays
    start_time = time.time()
    selection_sort(totalDelays)
    end_time = time.time()

    # Additional performance analysis of Selection Sort
    print("Performance Analysis:")
    print(f"Selection Sort Time: {end_time - start_time} seconds")

    # Use Insertion Sort
    totalDelaysCopy = totalDelays.copy()
    start_time = time.time()
    insertion_sort(totalDelaysCopy)
    end_time = time.time()
    print(f"Insertion Sort Time: {end_time - start_time} seconds")

    # Use built-in sort (for comparison)
    start_time = time.time()
    totalDelaysCopy = totalDelays.copy()
    totalDelaysCopy.sort()
    end_time = time.time()
    print(f"Built-in Sort Time: {end_time - start_time} seconds")


if __name__ == '__main__':
    airports = airlines.get_airports()
    processData(airports)


# in my computer the results of the performance analysis were:
# Performance Analysis:
# Selection Sort Time: 0.46306920051574707 seconds
# Insertion Sort Time: 0.0005593299865722656 seconds
# Built-in Sort Time: 3.814697265625e-05 seconds