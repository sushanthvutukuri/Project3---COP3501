import airlines
import hashlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

class Data:
    airports = airlines.get_airports()
    print(len(airports))
    #Semi-Dict Data Structure - Basically implements the data as a strucutre where there are no repeats and using the getData function one can get the data at a specific key within the airports
    airlist = []
    def __init__(self):
        airports = airlines.get_airports()
        for index in airports:
            if self.airlist.count(index["Airport"]) == 0:
                self.airlist.append(index["Airport"])
    @staticmethod
    def printData(code, self):
        counter=0
        for index in self.airlist:
            if index["Code"] == code or index["Name"]:
                print(index["Name"])
                break
        for index in self.airports:
            if(index["Airport"]["Code"]==code):
                print(index["Statistics"]["Flights"])
    @staticmethod
    def getData(code, self):
        for index in self.airports:
            if index["Airport"]["Code"]==code or index["Airport"]["Name"]==code:
                print(index["Statistics"]["Flights"])

            

class main:
    data= Data()
    print("Enter the airport code or name: ")
    code = input()
    #data.printData(code, data)
    #data.getData(code, data)
