import airlines


#
# ["Statistics"]["Flights"]["Total"]
# get ratio of delayed flights vs on time in a monthly basis
def processData(airports: list):
    totalDelays = []  # Initialize an empty list

    # ["Statistics"]["Flights"]["# of Delays"]
    # calculate total number of delays which includes: Carrier, Late aircraft,
    # National aviation system, Security, Weather.
    for entry in airports:
        totalDelay = (
                entry["Statistics"]["# of Delays"]["Carrier"] +
                entry["Statistics"]["# of Delays"]["Late Aircraft"] +
                entry["Statistics"]["# of Delays"]["National Aviation System"] +
                entry["Statistics"]["# of Delays"]["Security"] +
                entry["Statistics"]["# of Delays"]["Weather"]
        )
        totalDelays.append(totalDelay)

    max_value, max_index = max((value, index) for index, value in enumerate(totalDelays))
    print("The airport with most delays is: " + airports[max_index]["Airport"]["Code"])
    print(f"With total number of delays: {max_value}")

if __name__ == '__main__':
    airports = airlines.get_airports()
    processData(airports)
