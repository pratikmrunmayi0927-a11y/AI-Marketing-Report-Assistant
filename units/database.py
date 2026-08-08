import sqlite3
import os

# Create database folder if it does not exist
os.makedirs("database", exist_ok=True)

# Database path
DB_PATH = "database/marketing.db"

# Connect to database
conn = sqlite3.connect(DB_PATH, check_same_thread=False)

cursor = conn.cursor()

# Create reports table
cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    campaign TEXT,
    spend REAL,
    revenue REAL,
    report TEXT
)
""")

conn.commit()


def save_report(date, campaign, spend, revenue, report):

    cursor.execute("""
        INSERT INTO reports
        (date, campaign, spend, revenue, report)
        VALUES (?, ?, ?, ?, ?)
    """, (
        date,
        campaign,
        spend,
        revenue,
        report
    ))

    conn.commit()


def get_reports():

    cursor.execute("""
        SELECT *
        FROM reports
        ORDER BY id DESC
    """)

    return cursor.fetchall()