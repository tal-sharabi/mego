import sys


class Taxi:
    def __init__(self, driver_name, taxi_id, num_pass=4):
        self.__driver_name = driver_name
        self.__taxi_id = taxi_id
        self.__num_pass = num_pass
        self.__available = True

    def taxi_busy(self):
        self.__available = False

    @property
    def get_id(self):
        return self.__taxi_id

    @property
    def get_name(self):
        return self.__driver_name

    @property
    def get_num_pass(self):
        return self.__num_pass

    @property
    def is_available(self):
        return self.__available


class TaxiStation:
    def __init__(self, station_name):
        self.__station_name = station_name
        self.__num_taxis = 0
        self.__taxis = []

    @property
    def station_name(self):
        return self.__station_name

    @property
    def num_taxis(self):
        return self.__num_taxis

    def add_taxi(self, driver_name, taxi_id, num_pass):
        if self.__num_taxis < 80:
            self.__taxis.append(Taxi(driver_name, taxi_id, num_pass))
            self.__num_taxis += 1
        else:
            print("Taxi station is full")

    def get_taxi(self, num_passengers):

        closest_taxi = None
        min_difference = sys.maxsize  # Initialize minimum difference to the maximum integer value

        # Iterate through all taxis to find the closest available one
        for taxi in self.__taxis:
            if taxi.is_available and taxi.get_num_pass >= num_passengers:
                difference = abs(taxi.get_num_pass - num_passengers)
                if difference < min_difference:
                    closest_taxi = taxi
                    min_difference = difference

        if closest_taxi:  # If a suitable taxi is found
            closest_taxi.taxi_busy()  # Mark the taxi as busy
            return closest_taxi
        else:
            return None  # No suitable taxi found


if __name__ == "__main__":
    station = TaxiStation("Central Station")
    station.add_taxi("Tal", "2409", 4)
    station.add_taxi("Yoel", "6869", 7)
    station.add_taxi("Haim", "4568", 1)

    # Prompt user for number of passengers
    number_of_people = int(input("Enter number of passengers >>> "))
    taxi = station.get_taxi(number_of_people)

    if taxi:
        print("\nA taxi for you is on its way!")
        print("\nTaxi Details: ")
        print("\tID:", taxi.get_id)  # Accessing taxi ID through property
        print("\tDriver's name:", taxi.get_name)  # Accessing driver's name through property
        print("\tCapacity:", taxi.get_num_pass)  # Accessing taxi capacity through property
    else:
        print("Sorry, no taxi available at this time.")
