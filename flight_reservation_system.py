import argparse
from src.flight_reservation import Aircraft, Flight


def main():
    parser = argparse.ArgumentParser(description='Flight Reservation System')
    parser.add_argument('flight_number', type=str, help='Flight number')
    parser.add_argument('aircraft_model', type=str, help='Aircraft model')
    parser.add_argument('num_rows', type=int, help='Number of rows in the aircraft')
    parser.add_argument('num_seats_per_row', type=int, help='Number of seats per row')
    args = parser.parse_args()

    aircraft = Aircraft(args.aircraft_model, args.num_rows, args.num_seats_per_row)
    flight = Flight(args.flight_number, aircraft)

    while True:
        print('\n' + '='*30)
        print('Flight Reservation System')
        print('1. Check flight seat availability')
        print('2. Make a reservation')
        print('3. Change a reservation')
        print('4. Get passenger reservation')
        print('5. Exit')
        print('='*30 + '\n')
        choice = input('Enter choice (1/2/3/4/5): ')

        if choice == '1':
            print(flight.get_seat_info())
        elif choice == '2':
            name = input('Enter passenger name: ')
            seat = input('Enter seat number: ')
            print(flight.make_reservation(name, seat))
        elif choice == '3':
            name = input('Enter passenger name: ')
            from_seat = input('Enter current seat number: ')
            to_seat = input('Enter new seat number: ')
            print(flight.change_reservation(name, from_seat, to_seat))
        elif choice == '4':
            name = input('Enter passenger name: ')
            print(flight.get_reservation_details(name))
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
