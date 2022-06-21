# Original code taken from https://pythonexamples.org/python-csv-to-json/
# Adapted and updated by Guillermo Arrambide
# 18JUN22 || arrambi.de

# Import dependencies
import csv
import json


# Define function
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # Read CSV file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # Load CSV file data using built-in CSV library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # Convert each CSV row into Python dictionary object
        for row in csvReader:
            # Add dictionary object to a JSON array
            jsonArray.append(row)

    # Convert Python JSON array to JSON string and write it to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


# CSV input file
csvFilePath = r'data.csv'

# JSON output file
jsonFilePath = r'data.json'

# Call to execute main function
csv_to_json(csvFilePath, jsonFilePath)
