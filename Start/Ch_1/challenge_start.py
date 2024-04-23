# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json
import math
import pprint


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
# 1: How many quakes are there in total?
total_quakes = len(data["features"])
print(f"Total quakes: {total_quakes}")
# 2: How many quakes were felt by at least 200 people?
quakes_felt = list(quake["properties"]["felt"] != None and quake["properties"]["felt"] >= 200 for quake in data["features"]) 
#3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getfelt(dataitem):
    felt = dataitem["properties"]["felt"]
    if (felt is None):
        felt = 0
    return float(felt)
quakes_maxfelt =  max(data["features"],key=getfelt)
pprint.pp(quakes_maxfelt)
print(f"Quake felt by the most people: {quakes_maxfelt['properties']['place']} - {quakes_maxfelt['properties']['felt']} reports")

#4: Print the top 10 most significant events, with the significance value of each
def sigevent(dataitem):
    if dataitem["properties"]["sig"] != None:
        return float(dataitem["properties"]["sig"])
    else:
        return 0
sigevents = sorted(data["features"], key=sigevent, reverse=True)
for i in range(0,10):
    print(f"Event: {sigevents[i]['properties']['title']} - Significance: {sigevents[i]['properties']['sig']}")
    