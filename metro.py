import csv
import random

stations_data = "stations.csv"
lines_data = "lines.csv"

class line():
    def __init__(self, name, station_ids):
        self.name = name
        self.station_ids = station_ids

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

class metro_system():
    def __init__(self):
        self.stations = self.load_stations()
        

    def load_stations(self):
        stations = []
        with open(stations_data, mode ='r') as file:
            csvFile = csv.reader(file)
            next(csvFile)

            for lines in csvFile:
                station_id, name= lines
                stations.append(station(name, station_id))

        return stations
    

    def load_lines(self):
        lines = {}
        with open(lines_data, mode ='r') as file:
            csvFile = csv.reader(file)
            next(csvFile)

            for line in csvFile:
                color = line[0]
                stations_on_line = line[1].split(';')
                lines[color] = stations_on_line

        return lines


    def display_stations(self):
        print("Available Stations:")
        for station in self.stations:
            print(f"Station {station.name} is available.")
        print("------------------------")


    def display_lines(self):
        lines = self.load_lines()
        print("Available Lines:")
        for line, stations in lines.items():
            print(f"Line {line} with stations: {', '.join(stations)}")
        print("------------------------")


    def generate_ticket(self, start_name, end_name):
        length = 0
        start_station = None
        end_station = None
        start_index = -1
        end_index = -1

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
        metro_system().display_ticket(ticket_new)


    def display_ticket(self, ticket):
        print("------------------------")
        print(f"Ticket ID: {ticket.id}")
        print(f"From: {ticket.start_station.name} \n To: {ticket.end_station.name}")
        print(f"Price: {ticket.price}")
        print("------------------------")


    def cli(self):
        while True:
            print("1. View Stations")
            print("2. View Lines")
            print("3. Purchase ticket")
            print("4. Exit")
            choice = input("Enter your choice: ")
            print("--------------------------")

            if choice == '1':
                metro_system().display_stations()

            elif choice == '2':
                metro_system().display_lines()

            elif choice == '3':
                print("Enter starting station name: ")
                start_name = input().strip().lower()
                print("Enter ending station name: ")
                end_name = input().strip().lower()
                metro_system().generate_ticket(start_name, end_name)

            elif choice == '4':
                print("Exiting.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    metro_system().cli()
