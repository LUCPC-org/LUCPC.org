import json

wordsDict = {}

with open('dictionary.txt', 'r') as f:

    for line in f.readlines():

        wordsDict[line.strip()] = { 'num-enters': 0,
                                    'num-unique-enters': 0 }

database = {}
database['words'] = wordsDict

with open("database.json", "w") as outfile:
    json.dump(database, outfile)