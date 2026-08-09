import streamlit as st
import pandas as pd

from units.charts import campaign_chart
from units.llm import generate_marketing_insights
from units.preprocess import clean_data
from units.charts import (
    campaign_chart,
    spend_pie_chart,
    clicks_line_chart,
    conversion_chart,
    revenue_spend_chart
)
from units.report import generate_pdf
from units.report import generate_excel 
from units.auth import login
from units.database import save_report, get_reports

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI Marketing Report Assistant",
    page_icon="📊",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.markdown("""
<style>

.main{
    backgraound-color:#f5f7fb:
}

div[data-testid="stMetric"]{
   background:white;
   padding:15px;
   border-radius:12px;
   box-shadow:0px 3px 10px rba(0,0,0,0.10);
   text-align:center;
   
}

h1{
   color:#1f2937;
}

h2,h3{
    color:#374151;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    background:#2563eb;
    color:white;
    font-size:18px;
    border:none;
}

.stButton>button:hover{
    background:#1d4ed8;
}

div[data-testid="stMetric"]{
    background:white;
    border-left:6px solid #2563eb;
    border-radius:12px;
    padding:20px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
    text-align:center;
}

</style>
""", unsafe_allow_html=True
)

# -------------------------
# professional Sidebar
# -------------------------
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=100
    )

    st.title("📊 AI Marketing Report Assistant")

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "📂 Upload Marketing Report (.csv)",
        type=["csv"]
    )

    st.markdown("---")

    st.success("✅ Dashboard Ready")

    st.markdown("## 📂 Features")

    st.markdown("""
    ✅ CSV Upload

    ✅ Data Cleaning

    ✅ KPI Dashboard

    ✅ Interactive Charts

    ✅ AI Insights (Groq)

    ✅ PDF Report

    ✅ Excel Report
    """)

    st.markdown("---")

    st.info("""
👨‍💻 **Developed By**

**Pratik Malap**

AI Marketing Dashboard
""")

    st.markdown("---")

    st.caption("Version 1.0")

st.markdown("----")
if st.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.markdown("---")

if st.checkbox("📜 Show Report History"):
    reports = get_reports()

    for report in reports:

        st.write(report)
# -------------------------
# Main Title
# -------------------------
st.markdown("""
# 📊 AI Marketing Report Assistant

### Analyze Marketing Campaigns with AI

Upload your CSV file and generate professional reports instantly.
""")

st.info("""
## 🚀 AI Powered Marketing Dashboard

Upload your marketing report and get:

✅ KPI Analysis

✅ Interactive Charts

✅ AI Insights

✅ PDF & Excel Reports
""")

if not st.session_state.logged_in:
    login()
    st.stop()

# -------------------------
# File Upload
# -------------------------
#uploaded_file = st.sidebar.file_uploader(
   # "📂 Upload Marketing Report (.csv)",
   # type=["csv"]
#)

# -------------------------
# If File Uploaded
# -------------------------
if uploaded_file is not None:

    # -------------------------
    # Read CSV
    # -------------------------
    df = pd.read_csv(uploaded_file)
    df = clean_data(df)

    #--------------------------
    # Campaign Filter
    #--------------------------

    st.sidebar.markdown("---")
    st.sidebar.subheader("🎯 Filters")

    campaign = st.sidebar.selectbox(
        "Select Campaign",
            ["All"] + list(df["Campaign"].unique())   
    )

    if campaign !="All":
        df = df[df["Campaign"] == campaign]

    st.sidebar.subheader("💰 Revenue Filter")

    min_rev = int(df["Revenue"].min())
    max_rev = int(df["Revenue"].max())

    revenue_range = st.sidebar.slider(
    "Revenue",
    min_rev,
    max_rev,
    (min_rev, max_rev)
    )

    df = df[
    (df["Revenue"] >= revenue_range[0]) &
    (df["Revenue"] <= revenue_range[1])
   ]

    campaigns = ["All"] + list(df["Campaign"].unique())

    selected_campaign = st.selectbox(
        "Select Campaign",
            campaigns
    )

    if selected_campaign != "All":
        df = df[df["Campaign"] == selected_campaign]

    min_revenue = st.slider(
        "Minimum Revenue",
        int(df["Revenue"].min()),
    int(df["Revenue"].max()),
    int(df["Revenue"].min())
    )

    df = df[df["Revenue"] >= min_revenue]

    best = df.loc[df["Revenue"].idxmax()]

    st.success(f"""
    🏆 Best Campaign

    Campaign: {best['Campaign']}

    Revenue: ₹ {best['Revenue']:,}
    """)

    
    st.success("✅ File Uploaded Successfully!")

    st.subheader("📂 File Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Filename:**", uploaded_file.name)

    with col2:
        st.write("**Size:**", f"{uploaded_file.size/1024:.2f} KB")

    st.subheader("📈 Dashboard Progress")

    st.progress(100)

    st.success("Dashboard Loaded Successfully")

    # -------------------------
    # Dataset Preview
    # -------------------------
    st.subheader("📋 Dataset Preview")
    st.dataframe(df)

    st.subheader("🔍 Search & Filter")

    search = st.text_input("Search Campaign")

    if search:
        df = df[df["Campaign"].str.contains(search, case=False, na=False)]

    # -------------------------
    # KPI Calculations
    # -------------------------
    st.subheader("📈 Marketing KPIs")

    total_impressions = df["Impressions"].sum()
    total_clicks = df["Clicks"].sum()
    total_spend = df["Spend"].sum()
    total_conversions = df["Conversions"].sum()
    total_revenue = df["Revenue"].sum()

    ctr = (total_clicks / total_impressions) * 100
    cpc = total_spend / total_clicks
    conversion_rate = (total_conversions / total_clicks) * 100
    roi = ((total_revenue - total_spend) / total_spend) * 100

    # -------------------------
    # KPI Cards
    # -------------------------
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.metric("👀 Impressions", f"{total_impressions:,}")

    with col2:
        st.metric("🖱 Clicks", f"{total_clicks:,}")

    with col3:
        st.metric("💰 Spend", f"₹ {total_spend:,}")

    with col4:
        st.metric("🎯 Conversions", f"{total_conversions:,}")

    with col5:
        st.metric("📈 CTR", f"{ctr:.2f}%")

    with col6:
        st.metric("💲 CPC", f"₹ {cpc:.2f}")

    # -------------------------
    # Extra KPI Cards
    # -------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💵 Revenue", f"₹ {total_revenue:,}")

    with col2:
        st.metric("📈 ROI", f"{roi:.2f}%")

    with col3:
        st.metric("🎯 Conversion Rate", f"{conversion_rate:.2f}%")
   
    

    # -------------------------
    # marketing dashboard
    # -------------------------
    st.subheader("📊 Marketing Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(campaign_chart(df), use_container_width=True)
        st.plotly_chart(clicks_line_chart(df), use_container_width=True)
    

    with col2:
        st.plotly_chart(spend_pie_chart(df), use_container_width=True)
        st.plotly_chart(conversion_chart(df), use_container_width=True)
    

    # Revenue vs Spend
    st.plotly_chart(revenue_spend_chart(df), use_container_width=True)

    best = df.loc[df["Revenue"].idxmax()]

    st.subheader("🏆 Top 5 Campaigns")

    top5 = df.sort_values("Revenue", ascending=False).head(5)

    st.dataframe(top5)

    st.subheader("📉 Lowest 5 Campaigns")

    bottom5 = df.sort_values("Revenue").head(5)

    st.dataframe(bottom5)

    st.subheader("🥇 Revenue Leaderboard")

    leaderboard = df[["Campaign", "Revenue"]]

    leaderboard = leaderboard.sort_values(
        "Revenue",
        ascending=False
    )

    st.table(leaderboard)

    st.subheader("📊 KPI Summary")

    summary = {
        "Metric":[
            "Total Spend",
        "Total Revenue",
        "Total Clicks",
        "Total Conversions",
        "ROI %"
        ],

        "Value": [
        total_spend,
        total_revenue,
        total_clicks,
        total_conversions,
        round(roi, 2)
        ]
    }

    summary_df = pd.DataFrame(summary)

    st.table(summary_df)

    csv = summary_df.to_csv(index=False).encode("utf-8")

    st.download_button(
    label="📥 Download Analytics CSV",
    data=csv,
    file_name="analytics_summary.csv",
    mime="text/csv"
    )

    st.success(f"""
    🏆 Best Campaign
    
    Campaign : {best["Campaign"]}
    
    Revenue : ₹ {best["Revenue"]:,}
    """)

    worst = df.loc[df["Revenue"].idxmin()]

    st.error(f"""
    ❌ Worst Campaign

    Campaign : {worst["Campaign"]}

    Revenue : ₹ {worst["Revenue"]:,}
    """)

    worst = df.loc[df["Revenue"].idxmin()]

    st.error(f"""
    ❌ Worst Campaign

    Campaign: {worst['Campaign']}

    Revenue: ₹ {worst['Revenue']:,}
    """)
    # -------------------------
    # AI Marketing Insights
    # -------------------------
    st.subheader("🤖 AI Marketing Insights")

    prompt = f"""
Analyze the following marketing campaign data.

{df.to_string(index=False)}

Please provide:

1. Best Performing Campaign
2. Worst Performing Campaign
3. Marketing Recommendations
4. Budget Suggestions
5. Executive Summary
"""

if st.button("🚀 Generate AI Report"):
    with st.spinner("Generating AI Report..."):
            st.session_state.result = generate_marketing_insights(prompt)

    # ==========================================
# SAVE REPORT
# ==========================================

if "result" in st.session_state:

    if st.button("💾 Save Report"):

        save_report(
            date=str(pd.Timestamp.now().date()),
            campaign="Marketing Campaign",
            spend=float(df["Spend"].sum()),
            revenue=float(df["Revenue"].sum()),
            report=st.session_state.result
        )

        st.success("✅ Report saved successfully!")

    from datetime import datetime

    save_report(
    datetime.now().strftime("%d-%m-%Y %H: %M"),

    "All Campaigns",

    total_spend,

    total_revenue,

    st.session_state.result
   )
       

# -------------------------
# Show Result
# -------------------------

if "result" in st.session_state:

    st.success("✅ AI Analysis Completed!")

    st.write(st.session_state.result)

    # -------------------------
    # PDF Download
    # -------------------------

    pdf_file = generate_pdf(st.session_state.result)

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="Marketing_Report.pdf",
            mime="application/pdf"
        )

    # -------------------------
    # Excel Download
    # -------------------------

    excel_file = generate_excel(df)

    with open(excel_file, "rb") as file:
        st.download_button(
            label="📊 Download Excel Report",
            data=file,
            file_name="Marketing_Report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    # -------------------------
    # Dataset Information
    # -------------------------
    st.subheader("📄 Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing values", df.isnull().sum().sum())

# -------------------------
# No File Uploaded
# -------------------------
else:
    st.info("📂 Please upload a CSV file.")

# ==========================================
# SAVED REPORTS
# ==========================================

st.divider()

st.subheader("📁 Saved Marketing Reports")

saved_reports = get_reports()

if saved_reports:

    for report in saved_reports:

        report_id = report[0]
        date = report[1]
        campaign = report[2]
        spend = report[3]
        revenue = report[4]
        report_text = report[5]

        with st.expander(f"📊 {campaign} | {date}"):
             col1, col2 = st.columns(2)

        with col1:
            try:
                spend_value = float(spend)
            except (ValueError, TypeError):
                spend_value = 0.0

            st.metric(
                "💰 Spend",
                f"₹{spend_value:,.2f}"
            )

        with col2:
            try:
                revenue_value = float(revenue)
            except (ValueError, TypeError):
                revenue_value = 0.0

            st.metric(
                "💵 Revenue",
                f"₹{revenue_value:,.2f}"
            )        

        st.markdown("### 🤖 AI Marketing Insights")

        st.write(report_text)

else:
    st.info("No saved reports yet.")


st.markdown("---")

st.caption(
    "© 2026 AI Marketing Report Assistant | Developed by Pratik Malap"
)