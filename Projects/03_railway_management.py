# Railway management System

class Train:
    def __init__(self, name, fare, total_seats):
        self.name = name
        self.fare = fare
        self.total_seats = total_seats
        self.booked_seats = []

    def get_status(self):
        print("Status:")
        print(f"The name of the train is {self.name}")
        print(f"The total seats in the train are {self.total_seats}")
        print(f"The available seats are {self.total_seats - len(self.booked_seats)}")
        print()

    def fare_info(self):
        print("Fare information:")
        print(f"The price of the ticket is: Rs {self.fare}")
        print()

    def book_ticket(self):
        print("Ticket booking:")
        if len(self.booked_seats) < self.total_seats:
            # Find the first available seat
            seat = 1
            while seat in self.booked_seats:
                seat += 1

            self.booked_seats.append(seat)
            print(f"Your ticket has been booked! Your seat number is {seat}")
        else:
            print("Sorry, this train is full! Kindly try in tatkal")
        print()

    def cancel_ticket(self):
        print("Ticket cancellation:")
        if len(self.booked_seats) > 0:
            seat_to_cancel = int(input("Enter your seat number to cancel: "))
            if seat_to_cancel in self.booked_seats:
                self.booked_seats.remove(seat_to_cancel)
                print(f"Your ticket for seat number {seat_to_cancel} has been canceled successfully.")
            else:
                print("Invalid seat number or not booked.")
        else:
            print("No booked seats to cancel.")
        print()

         
train1 = Train("Intercity Express: 14015", 90, 3)
train1.fare_info()
train1.get_status()
train1.book_ticket()
train1.book_ticket()
train1.book_ticket()
train1.book_ticket()
train1.get_status()
train1.cancel_ticket()
train1.cancel_ticket()
train1.get_status()
train1.book_ticket()
train1.get_status()


# Program for railway management system 
# containing methods to get fare info, get train info, book and cancel tickets
# for booking again the user will be given the least indexed seat number
# here no choice is being given to user to choose the seat number to book
# for cancelling, user will be asked which seat to be cancelled and that seat will be cancelled 
# if the seat number hasnt been booked or is invalid then nothing will happen
# while booking again least index seat number will be given regardless of the seat numbers cancelled




'''OUTPUT
Fare information:
The price of the ticket is: Rs 90

Status:
The name of the train is Intercity Express
The total seats in the train are 3
The available seats are 3

Ticket booking:
Your ticket has been booked! Your seat number is 1

Ticket booking:
Your ticket has been booked! Your seat number is 2

Ticket booking:
Your ticket has been booked! Your seat number is 3

Ticket booking:
Sorry, this train is full! Kindly try in tatkal

Status:
The name of the train is Intercity Express
The total seats in the train are 3
The available seats are 0

Ticket cancellation:
Enter your seat number to cancel: 2
Your ticket for seat number 2 has been canceled successfully.

Ticket cancellation:
Enter your seat number to cancel: 4
Invalid seat number or not booked.

Status:
The name of the train is Intercity Express
The total seats in the train are 3
The available seats are 1

Ticket booking:
Your ticket has been booked! Your seat number is 2

Status:
The name of the train is Intercity Express
The total seats in the train are 3
The available seats are 0

'''
