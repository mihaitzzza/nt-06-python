import json
import csv


def write_to_json_file(data):
    with open('output/data.json', 'w+') as json_file:
        json.dump(data, json_file, indent=2)


def write_to_csv_file():
  data_to_store = [{
    'brand': 'Opel',
    'model': 'Astra',
    'year': 2002
  }, {
    'brand': 'Mazda',
    'model': '6',
    'year': 2007
  }]

  with open('output/data.csv', 'w+') as csv_file:
    csv_writer = csv.writer(csv_file)

    header = list(data_to_store[0].keys())
    csv_writer.writerow(header)

    for car in data_to_store:
      car_data = list(car.values())
      csv_writer.writerow(car_data)
