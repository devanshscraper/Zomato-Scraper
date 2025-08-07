🍽️ Zomato Restaurant Scraper
This Python script (in the login repo) scrapes restaurant menu data from Zomato, including item names, prices, and descriptions. The data is saved in a CSV file.

✅ Features
Automates search by city and restaurant

Extracts food item name, price, and description

Saves results to a CSV file

Speaks errors aloud using pyttsx3

🛠️ Requirements
Install the required libraries:

bash
Copy
Edit

pip install selenium undetected-chromedriver pyttsx3
▶️ Before You Run
First, save your Zomato login cookies by running the code from login.py file in the repo:

▶️ Usage
Clone the login repo.

Run the script script.py.

Enter the city and restaurant name when prompted.

The output will be saved in a CSV file:
Data_<restaurant_name>_1.csv
