import csv
from datetime import datetime, timedelta
import random

# Define the starting date and ending date (Sept 1st, 2024 to Nov 16th, 2024)
start_date = datetime(2024, 9, 1)
end_date = datetime(2024, 11, 16)

# Define the initial petrol and diesel prices (based on estimated prices)
initial_petrol_price = 100.00  # Estimated petrol price on Sep 1, 2024 (INR)
initial_diesel_price = 90.00   # Estimated diesel price on Sep 1, 2024 (INR)

# Define the daily price fluctuation ranges (reasonable fluctuations for the Indian market)
petrol_daily_change_range = (0.05, 0.20)  # Petrol price can change by ₹0.05 to ₹0.20 daily
diesel_daily_change_range = (0.03, 0.10)  # Diesel price can change by ₹0.03 to ₹0.10 daily

# Open the CSV file for writing
with open('indian_petrol_diesel_prices_2024.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["Date", "Petrol Price (INR)", "Diesel Price (INR)"])
    
    # Initialize prices with the base prices
    petrol_price = initial_petrol_price
    diesel_price = initial_diesel_price

    # Loop through each day from start_date to end_date
    current_date = start_date
    while current_date <= end_date:
        # Simulate the daily price change for petrol and diesel
        petrol_change = random.uniform(*petrol_daily_change_range)  # Random fluctuation for petrol
        diesel_change = random.uniform(*diesel_daily_change_range)  # Random fluctuation for diesel

        # Apply the fluctuations (randomly increase or decrease the price)
        petrol_price += random.choice([-1, 1]) * petrol_change
        diesel_price += random.choice([-1, 1]) * diesel_change

        # Ensure that prices don't fall below a reasonable threshold (e.g., ₹80 for petrol and ₹70 for diesel)
        petrol_price = max(petrol_price, 80.00)
        diesel_price = max(diesel_price, 70.00)

        # Write the row with the date and the prices
        writer.writerow([current_date.strftime('%Y-%m-%d'), round(petrol_price, 2), round(diesel_price, 2)])
        
        # Move to the next day
        current_date += timedelta(days=1)

print("CSV file 'indian_petrol_diesel_prices_2024.csv' has been generated with realistic prices.")
