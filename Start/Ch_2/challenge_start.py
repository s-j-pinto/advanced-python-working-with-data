# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
# produce summary of events by type of event
eventtypes = {}

# for event in data["features"]:
#     etype = event["properties"]["type"]
#     if etype in eventtypes:
#         eventtypes[etype] += 1
#     else:
#         eventtypes[etype] = 1
for event in data["features"]:
    etype = event["properties"]["type"]
    if etype in eventtypes:
        eventtypes[etype] += 1
    else:
        eventtypes[etype] = 1

print("Event Type Summary:")
for etype, count in eventtypes.items():
    print(f"{etype}: {count}")  

    