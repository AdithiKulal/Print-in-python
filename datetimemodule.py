import datetime

events = {}

def display_current_datetime():
    current_datetime = datetime.datetime.now()
    print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

def schedule_event():
    event_name = input("Enter event name: ")
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))
    event_datetime = datetime.datetime(year, month, day, hour, minute)
    events[event_name] = event_datetime
    print("Event scheduled successfully!")

def view_upcoming_events():
    print("Upcoming Events:")
    for event, datetime in events.items():
        print(f"{event}: {datetime.strftime('%Y-%m-%d %H:%M:%S')}")

def delete_event():
    event_name = input("Enter event name to delete: ")
    if event_name in events:
        del events[event_name]
        print("Event deleted successfully!")
    else:
        print("Event not found!")

def main():
    while True:
        print("Personal Event Planner")
        print("1. Display Current Date and Time")
        print("2. Schedule Event")
        print("3. View Upcoming Events")
        print("4. Delete Event")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_current_datetime()
        elif choice == "2":
            schedule_event()
        elif choice == "3":
            view_upcoming_events()
        elif choice == "4":
            delete_event()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()