# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    current_date = datetime.now()  # Get the current date
    future_date = current_date + timedelta(days=days)  # Calculate future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format future date
    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()  # Display the current date and time
    days = int(input("Enter the number of days to add to the current date: "))  # Prompt for user input
    calculate_future_date(days)  # Calculate and display the future date

if __name__ == "__main__":
    main()

