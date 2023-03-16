### this code defines a simple reservation system for flights that includes seat allocation and changing, and passenger information retrieval.

class Aircraft:
    """A class representing an aircraft.

    Attributes:
        aircraft_type (str): The type of the aircraft.
        num_rows (int): The number of rows in the aircraft.
        num_seats_per_row (int): The number of seats per row in the aircraft.
    """
    def __init__(self, aircraft_type, num_rows, num_seats_per_row):
        self.aircraft_type = aircraft_type
        self.num_rows = num_rows
        self.num_seats_per_row = num_seats_per_row

    def get_seat_config(self):
        """
        Returns a tuple containing the number of rows and seats per row of the aircraft.
        """
        return (self.num_rows, self.num_seats_per_row)

class Flight:
    """A class representing a flight.

    Attributes:
        flight_number (str): The flight number.
        aircraft (Aircraft): The aircraft used for the flight.
        available_seats (List[str]): A list of available seat numbers for the flight.
        passengers (List[Passenger]): A list of passengers on the flight.
    """
    def __init__(self, flight_number, aircraft):
        self.flight_number = flight_number
        self.aircraft = aircraft
        self.available_seats = self._get_available_seats()
        self.passengers = []

    def _get_available_seats(self):
        """
        Generates a list of available seat numbers for the flight.
        """
        num_rows, num_seats_per_row = self.aircraft.get_seat_config()
        return [str(row) + letter for row in range(1, num_rows + 1)
                for letter in 'ABCDEFGHIJKL'[:num_seats_per_row]]

    def get_seat_info(self):
        """
        Returns a string containing the flight number and the number of available seats.
        """
        return f'Flight {self.flight_number} has {len(self.available_seats)} available seats.'

    def make_reservation(self, passenger_name, seat_number):
        """Makes a reservation for a passenger on a seat.

        Args:
            passenger_name (str): The name of the passenger.
            seat_number (str): The seat number for the reservation.

        Returns:
            str: A message confirming the seat reservation or an error message if the seat is already occupied.
        """
        if seat_number not in self.available_seats:
            return f'Seat {seat_number} is already occupied.'
        else:
            self.available_seats.remove(seat_number)
            self.passengers.append(Passenger(passenger_name, seat_number))
            return f'Seat {seat_number} has been allocated.'

    def change_reservation(self, passenger_name, old_seat_number, new_seat_number):
        """Changes a passenger's seat assignment on the flight.

        Parameters:
        - passenger_name (str): the name of the passenger
        - old_seat_number (str): the passenger's current seat number
        - new_seat_number (str): the passenger's desired new seat number

        Returns:
        - a string describing the result of the seat change
        """
        passenger = Passenger(passenger_name, old_seat_number)
        if passenger not in self.passengers:
            return f'No passenger with name {passenger_name} on seat {old_seat_number}.'
        if new_seat_number not in self.available_seats:
            return f'Seat {new_seat_number} is not available.'
        # Reserve new seat
        self.available_seats.remove(new_seat_number)
        self.available_seats.append(old_seat_number)
        self.passengers[self.passengers.index(passenger)].seat = new_seat_number
        return f'Seat {old_seat_number} of {passenger_name} has been changed to {new_seat_number}.'


    def get_reservation_details(self, passenger):
        """
        Retrieves the details of a reservation for a given passenger on this flight.

        passenger (str) : The name of the passenger.

        Returns:
         A string with the reservation details or an error message.
        """
        for p in self.passengers:
            if passenger == p.name:
                return f"{passenger}:\n Flight: {self.flight_number}\n Seat: {p.seat}"
                break
        else:
            return "No passenger with this name on this flight"

class Passenger:
    """A class representing a passenger.

    Attributes:
        name (str): The name of the passenger.
        seat (str): The seat of the passenger.
    """
    def __init__(self, name, seat):
        self.name = name
        self.seat = seat

    # Define __eq__ that returns True if the attributes are equal 
    def __eq__(self, other):
        return (self.name == other.name and self.seat == other.seat)

if __name__ == '__main__':
    # Create aircraft
    aircraft = Aircraft('Boeing 737', 10, 6)

    # Create flight
    flight = Flight('BA123', aircraft)

    # Make reservations
    flight.make_reservation('John', '1A')
    flight.make_reservation('Sara', '2F')

    # Change reservation
    flight.change_reservation('John', '1A', '2D')
    flight.change_reservation('John', '2D', '3D')

    # Get reservation details
    print(flight.get_reservation_details('Sara'))
    print(flight.get_reservation_details('John'))
