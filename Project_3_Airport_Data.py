import airlines
import time
import hashlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

class Data:
    airports = airlines.get_airports()
    #Semi-Dict Data Structure - Basically implements the data as a strucutre where there are no repeats and using the getData function one can get the data at a specific key within the airports
    airlist = []
    #Constructor that creates a Set Data Structure
    def __init__(self):
        airports = airlines.get_airports()
        for index in airports:
            if self.airlist.count(index["Airport"]) == 0:
                self.airlist.append(index["Airport"])
    #Method that returns data in graph format
    @staticmethod
    def printData(code, self):
        airdata = []
        airtime = []
        counter=0
        airport_name="";
        print("Following is a graph and text representation of the data requested.")
        #loop for finding the specific airport or code to see if it exists
        for index in self.airlist:
            if index["Code"] == code or index["Name"] == code:
                print(index["Name"])
                airport_name=index["Name"]
                break

        #if the specific airport does exist, add all the statistics related to that airport into sets
        for index in self.airports:
            if(index["Airport"]["Code"]==code):
                print(index["Time"])
                print(index["Statistics"]["Flights"])
                airdata.append(index["Statistics"]["Flights"]["Total"]-index["Statistics"]["Flights"]["On Time"])
                airtime.append(index["Time"]["Label"])
        #if the length of the sets containng the data is 0, then the airport does not exist so return and display that it was an invalid code
        if(len(airdata)==0):
            print("Invalid code or name. Please make sure that your spelling is correct. Codes are case sensitive and must be capitalized. Names must be specific.")
            print()
            return

        #create a plot of the data at one ariport over a specific period of time
        fig, ax=plt.subplots(figsize=(20, 4), layout='constrained')
        string="Date (From "+(airtime[0])+" to "+(airtime[-1])+")"
        ax.plot(airtime, airdata)
        ax.set_xlabel(string)
        ax.set_ylabel("Number of Delays")
        ax.set_title("Trend for Delays at " + airport_name)
        #display information about the plot
        print()
        print("NOTE: Unfortunately, due to large data sets, the X-Axis is may be unreadable. To counteract this issue, please use the zoom in feature on the graph ")
        print()
        print("Once you are finished with the graph, please close to continue using the Compiler")
        print()
        plt.show()
        return;
    
    #Internal method used early on for testing purposes
    @staticmethod
    def getData(code, self):
        for index in self.airports:
            if index["Airport"]["Code"]==code or index["Airport"]["Name"]==code:
                print(index["Statistics"]["Flights"])

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

def processData(airports: list, displayGraph: bool):
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


    #for i in range(len(averageDelayTime)):
        #print(f"{airportList[i]} {averageDelayTime[i]}")

    if(displayGraph):
        # plot the averages of airport delays
        fig, ax = plt.subplots(figsize = (13,2.7), layout = 'constrained')
        ax.bar(airportList, averageDelayTime)
        plt.show()

    # print the list of delays from least to most delays
    if(displayGraph == False):
        for entries in totalDelays:
            print(entries)

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
    #main UI using input output system
    data= Data()
    print("This is a Flight Data Compiler that retrieves and stores data using a sorting algorithm based on delayed and missed flights.")
    print("These are the following commands:")
    cont=True
    while cont:
        #displays the commands available
        print("Press 1 to generate a graph and data based on an airport code or name")
        print("Press 2 to generate a graph of all airports flight delays averaged over multiple months")
        print("Press 3 to print the sorted list of delays from least to most delays and, \n display the algorithims performance analysis")
        print("Press 4 to exit")
        print()
        print("Type in command and hit enter:")
        num=input()
        print()
        if num=="1":
            #displays statistics of flight delays at one airport
            print("Enter the airport code or name: ")
            code = input()
            data.printData(code, data)
        elif num=="2":
            #displays statistics of flight delays at all airports in the dataset averaged over multiple months
            print("The graph displays the average delays at an airport by taking into account the delays over multiple months")
            print()
            print("Once you are finished with the graph, please close to continue using the Compiler")
            processData(airports, True)
        elif num == "3":
            processData(airports, False)
        elif num=="4":
            #command for exit program
            print("Thank you for using this program!")
            cont=False
        else:
            #if command is invalid displays this error
            print("Invalid command, please try again")
            print()


    
