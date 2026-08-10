# 📊 AI Marketing Report Assistant

An AI-powered marketing analytics dashboard that analyzes campaign performance, calculates important marketing KPIs, generates interactive charts, and provides AI-powered marketing insights.

## 🚀 Live Demo

[👉 Add your Streamlit Cloud link here](https://ai-marketing-report-assistant-xdsepewtzoqkwra239qcq9.streamlit.app/)

## 📌 Project Overview

The AI Marketing Report Assistant helps marketers analyze CSV-based campaign data and quickly understand campaign performance.

Users can upload a marketing report and get:

- 📈 Marketing KPIs
- 📊 Interactive charts
- 🤖 AI-generated marketing insights
- 🏆 Best performing campaign
- ❌ Worst performing campaign
- 📄 PDF reports
- 📊 Excel reports
- 💾 Saved marketing reports

## ✨ Features

### 📂 CSV Upload
Upload marketing campaign data in CSV format.

### 🧹 Data Cleaning
Automatically handles duplicate and missing data.

### 📈 KPI Dashboard
Calculates:

- Impressions
- Clicks
- Spend
- Conversions
- CTR
- CPC
- Conversion Rate
- Revenue
- ROI

### 📊 Marketing Dashboard

Interactive visualizations include:

- Campaign Spend Analysis
- Campaign Spend Distribution
- Campaign Click Analysis
- Campaign Conversion Analysis
- Revenue vs Spend

### 🤖 AI Marketing Insights

Uses Groq AI to generate:

- Best Performing Campaign
- Worst Performing Campaign
- Marketing Recommendations
- Budget Suggestions
- Executive Summary

### 📄 Report Generation

Generate downloadable:

- PDF Marketing Report
- Excel Marketing Report

### 💾 Database

Uses SQLite to save and retrieve generated marketing reports.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Groq API
- SQLite
- ReportLab
- OpenPyXL
- Python-dotenv

## 📁 Project Structure

```text
AI-Marketing-Report-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── units/
│   ├── __init__.py
│   ├── charts.py
│   ├── database.py
│   ├── llm.py
│   ├── preprocess.py
│   └── report.py
│
├── data/
├── database/
└── reports/
## 📸 Screenshots

### 📊 Marketing Dashboard

![Marketing Dashboard](screenshots/dashboard.png)

### 🤖 AI Marketing Insights

![AI Marketing Insights](screenshots/ai-insights.png)

### 📄 Reports

![Reports](screenshots/reports.png)