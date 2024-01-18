class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parking_spaces = list(range(1, total_parking_spaces + 1))
        self.current_ticket = {'ticket_number': None, 'paid': False}

    def take_ticket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parking_spaces.pop(0)
            self.current_ticket = {'ticket_number': ticket_number, 'paid': False}
            print(f"Ticket {ticket_number} issued. Park at space {parking_space}.")

    def pay_for_parking(self):
        if self.current_ticket['ticket_number'] is not None and not self.current_ticket['paid']:
            payment = input("Enter the amount to pay: ")
            if payment:
                print("Ticket has been paid. You have 15 minutes to leave.")
                self.current_ticket['paid'] = True
            else:
                print("Payment not received. Ticket remains unpaid.")

    def leave_garage(self):
        if self.current_ticket['ticket_number'] is not None:
            if self.current_ticket['paid']:
                print("Thank you! Have a nice day.")
            else:
                payment = input("Please pay before leaving: ")
                if payment:
                    print("Thank you! Have a nice day.")
                    self.current_ticket['paid'] = True
                else:
                    print("Payment not received. You cannot leave without payment.")

                self.parking_spaces.append(self.current_ticket['ticket_number'])
                self.tickets.append(self.current_ticket['ticket_number'])
                self.current_ticket = {'ticket_number': None, 'paid': False}


def main():
    total_tickets = 10
    total_parking_spaces = 10
    garage = ParkingGarage(total_tickets, total_parking_spaces)

    while True:
        print("\nParking Garage Menu:")
        print("1. Take Ticket")
        print("2. Pay for Parking")
        print("3. Leave Garage")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            garage.take_ticket()
        elif choice == '2':
            garage.pay_for_parking()
        elif choice == '3':
            garage.leave_garage()
        elif choice == '4':
            print("Thank you for using the Parking Garage. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
