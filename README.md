# 📌 Telegram Data Processing Pipeline

This project is designed to scrape, clean, and store Telegram e-commerce data in a structured format for analysis. The pipeline consists of data scraping, cleaning, and storage in a database.

## 🛠 Project Structure

```
WEEK7/
│── data/                          # Raw and cleaned data storage
│   ├── CheMed123_data.csv
│   ├── DoctorsET_data.csv
│   ├── EAHCI_data.csv
│   ├── lobelia4cosmetics_data.csv
│   ├── yetenaweg_data.csv
│   ├── cleaned_telegram_data.csv  # Cleaned merged dataset
│── logs/                          # Logging directory
│── notebook/                      # Jupyter Notebooks for analysis
│   ├── data_cleaning_loading.ipynb
│── scripts/                        # Python scripts for processing
│   ├── data_cleaning.py            # Functions for data cleaning
│   ├── database_setup.py           # Database connection and table creation
│   ├── scrape_data.py              # Telegram data scraper
│── .env                            # Environment variables
│── .gitignore                      # Files to ignore in version control
│── channels.json                    # List of Telegram channels
│── requirements.txt                 # Required Python dependencies
│── run_scraper.sh                   # Shell script to execute scraper
│── README.md                        # Project documentation
```


## 🚀 How to Run the Project

1️⃣ Set Up the Environment

Ensure you have Python 3.8+ installed. Create a virtual environment and install dependencies:
```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    pip install -r requirements.txt
```

2️⃣ Configure Environment Variables

Create a .env file inside the project directory:

```bash
  DB_NAME=your_database
  DB_USER=your_user
  DB_PASSWORD=your_password
  DB_HOST=localhost
  DB_PORT=5432
```

3️⃣ Scrape Data from Telegram

Run the scraper to collect messages and store them in CSV format:
```bash
  python scripts/scrape_data.py
```
4️⃣ Clean the Data

Run the data cleaning script to preprocess the collected data:
```bash
  python scripts/data_cleaning.py
```
5️⃣ Store Data in Database

Set up the database and insert the cleaned data:
```bash
  python scripts/database_setup.py
```
📊 Jupyter Notebook

You can also use the Jupyter Notebook for step-by-step execution:

jupyter notebook notebook/data_cleaning_loading.ipynb

### 📌 Features

✅ Automated Telegram Data Scraping✅ Data Cleaning & Preprocessing✅ Database Storage for Easy Access✅ Structured Logging & Error Handling✅ Jupyter Notebook for Interactive Exploration

📞 Contact & Support

For any issues, open a GitHub issue or contact the developer. 🚀

