from typing import List, Dict, Tuple

# Star Cinema Class
class Star_Cinema:
    def __init__(self) -> None:
        self.hall_list: List[Hall] = []

    def entry_hall(self, hall_no: int, rows: int, cols: int):
        self.hall_list.append(Hall(rows, cols, hall_no))

# Hall Class
class Hall:
    def __init__(self, rows: int, cols: int, hall_no: int) -> None:
        self.__seats: Dict[str, List[List[bool]]] = {}
        self.__show_list: List[Tuple[str, str, str]] = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id: str, movie_name: str, time: str):
        self.__show_list.append((id, movie_name, time))
        SeatArray = [[False for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = SeatArray
        print(f'---------Show "{movie_name}" Entered Successfully for Hall {self.__hall_no}---------')

    def book_seats(self, id: str, seats: List[Tuple[int, int]]):
        if id not in self.__seats:
            print('Invalid Show ID')
            return
        for row, col in seats:
            if (row < 0 or row >= self.__rows) or (col < 0 or col >= self.__cols):
                print(f'Invalid seat: Row {row}, Col {col}')
                return
            if self.__seats[id][row][col]:
                print(f'Seat at Row {row}, Col {col} is already booked')
            else:
                self.__seats[id][row][col] = True
                print(f'Seat at Row {row}, Col {col} Booked Successfully')

    def view_show_list(self):
        print(f"-------Show List for Hall {self.__hall_no}------------")
        for id, movie, time in self.__show_list:
            print(f'Show ID: {id} | Movie: {movie} | Time: {time}')

    def view_available_seats(self, id: str):
        if id not in self.__seats:
            print('Invalid Show ID')
            return
        print(f"-------Available Seats for Show {id} in Hall {self.__hall_no}------------")
        for row in range(self.__rows):
            for col in range(self.__cols):
                if not self.__seats[id][row][col]:
                    print(f'Available Seat - Row: {row}, Col: {col}')


# Function to demonstrate the replica cinema system
def cinema_system_replica():
    print("Initializing the replica cinema system...\n")

    # Replica cinema 1
    cinema_1 = Star_Cinema()
    cinema_1.entry_hall(1, 7, 7)  # Hall 1 with 7x7 seats
    cinema_1.hall_list[0].entry_show('S1', 'Movie 01', '10:00 AM')
    cinema_1.hall_list[0].entry_show('S2', 'Movie 02', '01:00 PM')

    # Replica cinema 2
    cinema_2 = Star_Cinema()
    cinema_2.entry_hall(2, 5, 5)  # Hall 2 with 5x5 seats
    cinema_2.hall_list[0].entry_show('S3', 'Movie 03', '03:00 PM')
    cinema_2.hall_list[0].entry_show('S4', 'Movie 04', '06:00 PM')

    # Menu for cinema 1
    print("----- Cinema 1 System -----")
    while True:
        print("\n1. View all shows")
        print("2. View available seats")
        print("3. Book tickets")
        print("4. Exit Cinema 1")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            cinema_1.hall_list[0].view_show_list()

        elif choice == 2:
            show_id = input("Enter Show ID: ")
            cinema_1.hall_list[0].view_available_seats(show_id)

        elif choice == 3:
            show_id = input("Enter Show ID: ")
            num_tickets = int(input("Enter number of tickets: "))
            seat_list = []
            for i in range(num_tickets):
                row, col = map(int, input(f"Enter Row and Column for ticket {i+1}: ").split())
                seat_list.append((row, col))
            cinema_1.hall_list[0].book_seats(show_id, seat_list)

        elif choice == 4:
            print("Exiting Cinema 1...")
            break

        else:
            print("Invalid choice. Please try again.")

    # Menu for cinema 2
    print("\n----- Cinema 2 System -----")
    while True:
        print("\n1. View all shows")
        print("2. View available seats")
        print("3. Book tickets")
        print("4. Exit Cinema 2")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            cinema_2.hall_list[0].view_show_list()

        elif choice == 2:
            show_id = input("Enter Show ID: ")
            cinema_2.hall_list[0].view_available_seats(show_id)

        elif choice == 3:
            show_id = input("Enter Show ID: ")
            num_tickets = int(input("Enter number of tickets: "))
            seat_list = []
            for i in range(num_tickets):
                row, col = map(int, input(f"Enter Row and Column for ticket {i+1}: ").split())
                seat_list.append((row, col))
            cinema_2.hall_list[0].book_seats(show_id, seat_list)

        elif choice == 4:
            print("Exiting Cinema 2...")
            break

        else:
            print("Invalid choice. Please try again.")


# Running the system with replica cinemas
cinema_system_replica()
