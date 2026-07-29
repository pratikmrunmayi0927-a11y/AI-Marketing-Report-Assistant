import streamlit as st
import pandas as pd
from utils.charts import campaign_chart

#-------------------------
#page configuration
#-------------------------
st.set_page_config(
    page_title="AI Marketing Report Assistant",
    page_icon="📊",
    layout="wide"
)

#------------------------
#sidebar
#------------------------
st.sidebar.title("📊 AI Marketing Report Assistant")
st.sidebar.markdown("-----")
st.sidebar.info("Upload your Marketing Report")
st.sidebar.markdown("----")

#------------------------
#Main Title
#-----------------------
st.title("📊 AI Marketing Report Assistant")

st.write(
    "Upload your marketing report (CSV) to analyze campaign performance."
)

# ------------------------
# File Upload
# ------------------------
uploaded_file = st.file_uploader(
    "Upload Marketing Report (.csv)",
    type=["csv"]
)

# ------------------------
# Display Data
# ------------------------
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ File Uploaded Successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(df)

    st.subheader("📈 Marketing KPIs")
    #kpi calculations
    total_impressions = df["Impressions"].sum()
    total_clicks = df["Clicks"].sum()
    total_spend = df["Spend"].sum()
    total_conversions = df["Conversions"].sum()

    ctr = (total_clicks / total_impressions) * 100
    cpc = total_spend / total_clicks
    conversions_rate = (total_conversions / total_clicks) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👀 Impressions", f"₹ {total_spend:,}")
        st.metric("🖱 Clicks", f"{total_clicks:,}")

    with col2:
        st.metric("💰 Spend", f"₹ {total_spend:,}")
        st.metric("🎯 Conversions" , total_conversions)

    with col3:
        st.metric("CTR", f"{ctr:.2f}%")
        st.metric("CPC", f"₹ {cpc:.2f}")

    st.metric("Conversion Rate", f"{conversions_rate:.2f}%")

    # kpi code
    st.subheader("📊 Campaign Spend Analysis")
    fig = campaign_chart(df)

    st.plotly_chart(fig, use_container_width=True)
                            

    st.subheader("Dataset Informations")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

else:

    st.info("Please upload a CSV file.")