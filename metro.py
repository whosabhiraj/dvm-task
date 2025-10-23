import csv
import random

stations_data = "stations.csv"

class station():
    def __init__(self, name, id):
        self.name = name
        self.id = id

class ticket():
    def __init__(self, id, start_station, end_station, price):
        self.id = random.randint(1000, 9999)
        self.start_station = start_station
        self.end_station = end_station
        self.price = price

    def display_ticket(self):
        print(f"Ticket ID: {self.id}")
        print(f"From: {self.start_station.name} \n To: {self.end_station.name}")
        print(f"Price: {self.price}")

class metro_system():
    def __init__(self):
        self.stations = self.load_stations()

    def load_stations(self):
        stations = []
        with open(stations_data, mode ='r') as file:
            csvFile = csv.reader(file)
            next(csvFile)

            for lines in csvFile:
                station_id, name = lines
                stations.append(station(name, station_id))

        return stations

    def display_stations(self):
        print("Available Stations:")
        for station in self.stations:
            print(f"Station {station.name} with ID {station.id}")
    
    def cli():
        stations = metro_system().stations
        while True:
            print("1. View Stations")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                metro_system().display_stations()
            elif choice == '2':
                print("Exiting.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    metro_system.cli()