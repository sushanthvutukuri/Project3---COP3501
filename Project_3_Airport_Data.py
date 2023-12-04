import airlines
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
    #Method that returns data in grpah format
    @staticmethod
    def printData(code, self):
        airdata = []
        airtime = []
        counter=0
        airport_name="";
        print("Following is a graph and text representation of the data requested.")
        for index in self.airlist:
            if index["Code"] == code or index["Name"] == code:
                print(index["Name"])
                airport_name=index["Name"]
                break
        for index in self.airports:
            if(index["Airport"]["Code"]==code):
                print(index["Time"])
                print(index["Statistics"]["Flights"])
                airdata.append(index["Statistics"]["Flights"]["Total"]-index["Statistics"]["Flights"]["On Time"])
                airtime.append(index["Time"]["Label"])
        if(len(airdata)==0):
            print("Invalid code or name. Please make sure that your spelling is correct. Codes are case sensitive and must be capitalized. Names must be specific.")
            print()
            return
        fig, ax=plt.subplots(figsize=(13, 4), layout='constrained')
        ax.plot(airtime, airdata)
        string="Date (From "+(airtime[0])+" to "+(airtime[-1])+")"
        ax.set_xlabel(string)
        ax.set_ylabel("Number of Delays")
        ax.set_title("Trend for Delays at " + airport_name)
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

            

class main:
    data= Data()
    print("This is a Flight Data Compiler that retrieves and stores data using a sorting algorithm based on delayed and missed flights.")
    print("These are the following commands:")
    cont=True
    while cont:
        print("Press 1 to generate a graph and data based on an airport code or name")
        print("Press 2 to generate a list of all airports sorted in ascending order based on the number of flights delayed")
        print("Press 3 to exit")
        print()
        print("Type in command and hit enter:")
        num=input()
        print()
        if num=="1":
            print("Enter the airport code or name: ")
            code = input()
            data.printData(code, data)
            #data.getData(code, data)
        if num=="2":
            #placeholder
            print("hello")
        if num=="3":
            print("Thank you for using this app!")
            cont=False
