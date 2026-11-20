# ==========================================
# STAGE SHOW TICKET BOOKING SYSTEM
# MAIN PROGRAM
# ==========================================

import show_registration
import ticket_booking##i am waiting to change this file names or youall can use this name
import cancellation
import report


def main():

    while True:

        print("\n====================================")
        print(" STAGE SHOW TICKET BOOKING SYSTEM")
        print("====================================")
        print("1. Show Registration")
        print("2. Ticket Booking")
        print("3. Cancellation")
        print("4. Reports")
        print("5. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_registration.showRegistrationMenu()

        elif choice == "2":
            ticket_booking.ticketBookingMenu()

        elif choice == "3":
            cancellation.cancellationMenu()

        elif choice == "4":
            report.reportMenu()

        elif choice == "5":
            print("Thank you for using our system!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
