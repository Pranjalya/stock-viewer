# Stock Viewer
A web app to check out the latest updates in stock market.

## Tasks

Write a standalone Python Django web app / server that:
- Downloads the equity bhavcopy zip from the above page every day at 6 PM hours for the current date
- Extracts and parses the CSV file in it
- Writes the records into Redis into appropriate data structures (Fields: code, name, open, high, low, close)
- Renders a simple VueJS frontend with a search box that allows the stored entries to be searched by name and renders a table of results and optionally download the results as CSV.


**API** : https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

# Process

1. Install Redis Server
```
sudo apt-get install redis-server
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Create new Django Project
```
django-admin startproject app
```

4. Create new Django app
```
cd app
django-admin startapp api
```

5. Migrate for database safety
```
python manage.py migrate
```

6. Set up APScheduler (Advanced Python Scheduler) for scheduling the CRON job of fetching data

