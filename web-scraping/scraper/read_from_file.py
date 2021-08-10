import csv
import json


def read_from_json_file():
    with open('output/data.json') as json_file:
        data = json.load(json_file)

    return data


def read_from_csv_file():
    with open('output/data.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        for info in csv_reader:
            print(info)
