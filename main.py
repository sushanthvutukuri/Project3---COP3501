import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
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
    airportsSet = set()


    # ["Statistics"]["Flights"]["# of Delays"]
    # calculate total number of delays which includes: Carrier, Late aircraft,
    # National aviation system, Security, Weather.
    for entry in airports:
        temp1DelayTime = entry["Statistics"]["Flights"]["Delayed"]
        temp2AirportCode = entry["Airport"]["Code"]
        totalDelays.append((temp1DelayTime, temp2AirportCode))

        # add to the airport set the airport code
        airportsSet.add(temp2AirportCode)

    # turn set into a list of airports
    airportList = list(airportsSet)
    # create array for average delay time  with same amount of entries as airports
    averageDelayTime = [0] * len(airportList)
    airportDelays = [[] for _ in range(len(airportList))]
    for entry in airports:
        temp1DelayTime = entry["Statistics"]["Flights"]["Delayed"]
        temp2AirportCode = entry["Airport"]["Code"]
        # add delay value to the airport
        index = airportList.index(temp2AirportCode)
        airportDelays[index].append(temp1DelayTime)

    # calculate average delay time for each airport
    for i in range(len(airportDelays)):
        total = 0
        count = 0
        for j in range(len(airportDelays[i])):
            total += airportDelays[i][j]
            count += 1
        averageDelayTime[i] = total/count


    for i in range(len(averageDelayTime)):
        print(f"{airportList[i]} {averageDelayTime[i]}")

    # plot the averages of airport delays
    fig, ax = plt.subplots(figsize = (13,2.7), layout = 'constrained')
    ax.bar(airportList, averageDelayTime)
    plt.show()


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
