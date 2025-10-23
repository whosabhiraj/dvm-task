import csv
import random

stations_data = "stations.csv"

class line():
    def __init__(self, name, station_ids):
        self.name = name
        self.station_ids = station_ids


class station():
    def __init__(self, name, id, line_color):
        self.name = name
        self.id = id
        self.line_color = line_color

class ticket():
    def __init__(self, id, start_station, end_station, price):
        self.id = random.randint(1000, 9999)
        self.start_station = start_station
        self.end_station = end_station
        self.price = price

    def display_ticket(self):
        print("------------------------")
        print(f"Ticket ID: {self.id}")
        print(f"From: {self.start_station.name} \n To: {self.end_station.name}")
        print(f"Price: {self.price}")
        print("------------------------")

class metro_system():
    def __init__(self):
        self.stations = self.load_stations()

    def load_stations(self):
        stations = []
        with open(stations_data, mode ='r') as file:
            csvFile = csv.reader(file)
            next(csvFile)

            for lines in csvFile:
                station_id, name, color = lines
                stations.append(station(name, station_id, color))

        return stations

    def display_stations(self):
        print("Available Stations:")
        for station in self.stations:
            print(f"Station {station.name} with ID {station.id} is on the {station.line_color} line.")
        print("------------------------")

    def generate_ticket(self, start_name, end_name):
        length = 0
        for i in range(len(self.stations)):
            if self.stations[i].name == start_name:
                start_station = self.stations[i]
                start_index = i
            if self.stations[i].name == end_name:
                end_station = self.stations[i]
                end_index = i

        length = abs(end_index - start_index)
        price = 10
        ticket_new = ticket(random.randint(1000, 9999), start_station, end_station, price*length)
        ticket_new.display_ticket()

    def cli():
        while True:
            print("1. View Stations")
            print("2. Purchase ticket")
            print("3. Exit")
            choice = input("Enter your choice: ")
            print("--------------------------")

            if choice == '1':
                metro_system().display_stations()

            elif choice == '2':
                print("Enter starting station name: ")
                start_name = input().strip().lower()
                print("Enter ending station name: ")
                end_name = input().strip().lower()
                metro_system().generate_ticket(start_name, end_name)

            elif choice == '3':
                print("Exiting.")
                break
                
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    metro_system.cli()