
# ==========================================
# SHOW REGISTRATION & MANAGEMENT MODULE
# ==========================================

shows = []


# 1. REGISTER NEW SHOW
def registerShow():

    print("\n===== REGISTER NEW SHOW =====")

    show_id = input("Enter Show ID: ").strip()

    # Check duplicate Show ID
    for show in shows:
        if show["show_id"] == show_id:
            print("Show ID already exists!")
            return

    show_title = input("Enter Show Title: ").strip()
    show_date = input("Enter Show Date (DD/MM/YYYY): ").strip()
    show_time = input("Enter Show Time (HH:MM): ").strip()

    # Validate ticket price
    try:
        ticket_price = float(input("Enter Ticket Price (RM): "))

        if ticket_price <= 0:
            print("Invalid Ticket Price!")
            return

    except ValueError:
        print("Please enter a valid ticket price!")
        return

    # Validate ticket quantity
    try:
        available_tickets = int(input("Enter Available Tickets: "))

        if available_tickets <= 0:
            print("Invalid Ticket Quantity!")
            return

    except ValueError:
        print("Please enter a valid ticket quantity!")
        return

    # Create new show record
    new_show = {
        "show_id": show_id,
        "show_title": show_title,
        "show_date": show_date,
        "show_time": show_time,
        "ticket_price": ticket_price,
        "available_tickets": available_tickets
    }

    shows.append(new_show)

    print("\nShow registered successfully!")


# 2. VIEW ALL SHOWS
def viewShows():

    print("\n===== ALL REGISTERED SHOWS =====")

    if len(shows) == 0:
        print("No Shows Available!")
        return

    for show in shows:

        print("--------------------------------")
        print("Show ID:", show["show_id"])
        print("Show Title:", show["show_title"])
        print("Show Date:", show["show_date"])
        print("Show Time:", show["show_time"])
        print("Ticket Price: RM {:.2f}".format(show["ticket_price"]))
        print("Available Tickets:", show["available_tickets"])

    print("--------------------------------")


# 3. SEARCH SHOW
def searchShow():

    print("\n===== SEARCH SHOW =====")

    if len(shows) == 0:
        print("No Shows Available!")
        return

    search_id = input("Enter Show ID to Search: ").strip()

    for show in shows:

        if show["show_id"] == search_id:

            print("\nShow Found!")
            print("--------------------------------")
            print("Show ID:", show["show_id"])
            print("Show Title:", show["show_title"])
            print("Show Date:", show["show_date"])
            print("Show Time:", show["show_time"])
            print("Ticket Price: RM {:.2f}".format(show["ticket_price"]))
            print("Available Tickets:", show["available_tickets"])
            print("--------------------------------")

            return

    print("Show Not Found!")


# 4. UPDATE SHOW
def updateShow():

    print("\n===== UPDATE SHOW =====")

    if len(shows) == 0:
        print("No Shows Available!")
        return

    search_id = input("Enter Show ID to Update: ").strip()

    for show in shows:

        if show["show_id"] == search_id:

            print("\nShow Found!")
            print("1. Update Show Title")
            print("2. Update Show Date")
            print("3. Update Show Time")
            print("4. Update Ticket Price")
            print("5. Update Available Tickets")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":

                new_title = input("Enter New Show Title: ").strip()

                if new_title != "":
                    show["show_title"] = new_title
                    print("Show Title Updated Successfully!")
                else:
                    print("Show Title Cannot Be Empty!")

            elif choice == "2":

                new_date = input("Enter New Show Date: ").strip()

                if new_date != "":
                    show["show_date"] = new_date
                    print("Show Date Updated Successfully!")
                else:
                    print("Show Date Cannot Be Empty!")

            elif choice == "3":

                new_time = input("Enter New Show Time: ").strip()

                if new_time != "":
                    show["show_time"] = new_time
                    print("Show Time Updated Successfully!")
                else:
                    print("Show Time Cannot Be Empty!")

            elif choice == "4":

                try:
                    new_price = float(input("Enter New Ticket Price: "))

                    if new_price > 0:
                        show["ticket_price"] = new_price
                        print("Ticket Price Updated Successfully!")
                    else:
                        print("Invalid Ticket Price!")

                except ValueError:
                    print("Please Enter a Valid Price!")

            elif choice == "5":

                try:
                    new_quantity = int(input("Enter New Available Tickets: "))

                    if new_quantity >= 0:
                        show["available_tickets"] = new_quantity
                        print("Ticket Quantity Updated Successfully!")
                    else:
                        print("Invalid Ticket Quantity!")

                except ValueError:
                    print("Please Enter a Valid Quantity!")

            elif choice == "6":
                return

            else:
                print("Invalid Choice!")

            return

    print("Show Not Found!")


# 5. DELETE SHOW
def deleteShow():

    print("\n===== DELETE SHOW =====")

    if len(shows) == 0:
        print("No Shows Available!")
        return

    search_id = input("Enter Show ID to Delete: ").strip()

    for show in shows:

        if show["show_id"] == search_id:

            print("\nShow Found!")
            print("Show Title:", show["show_title"])

            confirm = input(
                "Are you sure you want to delete this show? (Y/N): "
            )

            if confirm.upper() == "Y":

                shows.remove(show)
                print("Show Deleted Successfully!")

            elif confirm.upper() == "N":

                print("Deletion Cancelled!")

            else:

                print("Invalid Choice!")

            return

    print("Show Not Found!")


# 6. SHOW REGISTRATION MENU
def showRegistrationMenu():

    while True:

        print("\n====================================")
        print("   SHOW REGISTRATION & MANAGEMENT")
        print("====================================")
        print("1. Register New Show")
        print("2. View All Shows")
        print("3. Search Show")
        print("4. Update Show")
        print("5. Delete Show")
        print("6. Back to Main Menu")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            registerShow()

        elif choice == "2":
            viewShows()

        elif choice == "3":
            searchShow()

        elif choice == "4":
            updateShow()

        elif choice == "5":
            deleteShow()

        elif choice == "6":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid Choice! Please Try Again.")


# ==========================================
# TEMPORARY TESTING
# ==========================================

if __name__ == "__main__":
    showRegistrationMenu()
