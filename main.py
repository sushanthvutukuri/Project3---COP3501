import time
import airlines

def insertion_sort(arr):
    """
    Implementation of the Insertion Sort algorithm for tuples.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[0] < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    """
    Implementation of the Selection Sort algorithm for tuples.
    """
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_index][0]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

def processData(airports: list):
    totalDelays = []  # Initialize an empty list

    # ["Statistics"]["Flights"]["# of Delays"]
    # calculate total number of delays which includes: Carrier, Late aircraft,
    # National aviation system, Security, Weather.
    for entry in airports:
        temp1DelayTime = entry["Statistics"]["Flights"]["Delayed"]
        temp2AirportCode = entry["Airport"]["Code"]
        totalDelays.append((temp1DelayTime, temp2AirportCode))

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

    # print the list of delays from least to most delays
    for entries in totalDelays:
        print(entries)

if __name__ == '__main__':
    airports = airlines.get_airports()
    processData(airports)
