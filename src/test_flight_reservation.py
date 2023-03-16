import unittest
from flight_reservation import Aircraft, Flight

class FlightReservationSystemTest(unittest.TestCase):
    def setUp(self):
        self.aircraft = Aircraft('Boeing 737', 10, 6)
        self.flight = Flight('BA123', self.aircraft)

    def test_make_reservation(self):
        # Allocate a seat that is available
        result = self.flight.make_reservation('John', '1A')
        self.assertEqual(result, 'Seat 1A has been allocated.')
        result = self.flight.available_seats
        self.assertNotIn('1A', result)
        # Allocate a seat that is already occupied
        result = self.flight.make_reservation('Sara', '1A')
        self.assertEqual(result, 'Seat 1A is already occupied.')
        
    def test_change_reservation(self):
        # Change a seat that is available to a new available seat
        self.flight.make_reservation('John', '1A')
        result = self.flight.change_reservation('John', '1A', '2B')
        self.assertEqual(result, 'Seat 1A of John has been changed to 2B.')
        result = self.flight.available_seats
        self.assertIn('1A', result)
        self.assertNotIn('2B', result)
        # Change reservation with wrong passenger info
        result = self.flight.change_reservation('John','1A', '1B')
        self.assertEqual(result, 'No passenger with name John on seat 1A.')
        result = self.flight.change_reservation('Emma','2B', '1B')
        self.assertEqual(result, 'No passenger with name Emma on seat 2B.')
        # Change reservation to another not available seat
        self.flight.make_reservation('Sara', '1B')
        self.flight.make_reservation('John', '1A')
        result = self.flight.change_reservation('John','1A', '1B')
        self.assertEqual(result, 'Seat 1B is not available.')
        result = self.flight.available_seats
        self.assertNotIn('1A', result)
        self.assertNotIn('1B', result)
    
    def test_get_seat_info(self):
        # Get seat info before any reservation is made
        result = self.flight.get_seat_info()
        self.assertEqual(result, 'Flight BA123 has 60 available seats.')
        # Allocate a seat
        self.flight.make_reservation('John', '1A')
        # Get seat info after a reservation is made
        result = self.flight.get_seat_info()
        self.assertEqual(result, 'Flight BA123 has 59 available seats.')

    def test_get_reservation_details(self):
        # Allocate a seat
        self.flight.make_reservation('John', '1A')
        # Get reservation info of John
        result = self.flight.get_reservation_details('John')
        self.assertEqual(result, 'John:\n Flight: BA123\n Seat: 1A')
        # Get reservation info of a wrong passenger
        result = self.flight.get_reservation_details('Sara') 
        self.assertEqual(result, 'No passenger with this name on this flight')
   
if __name__ == '__main__':
    unittest.main()
