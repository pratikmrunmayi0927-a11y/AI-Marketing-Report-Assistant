import plotly.express as px

# 1. campaign spend
def campaign_chart(df):
    fig = px.bar(
        df,
        x="Campaign",
        y="Spend",
        color="Campaign",
        title="Campaign Spend Analysis"
    )
    return fig

# 2. platform spend pie chart
def spend_pie_chart(df):
    fig = px.pie(
        df,
        names="Campaign",
        values="Spend",
        title="Campaign Spend Distribution"
    )
    return fig

# 3. Clicks line Chart
def clicks_line_chart(df):
    fig = px.line(
        df,
        x="Campaign",
        y="Clicks",
        markers=True,
        title="Campaign Click Analysis"
    )
    return fig

# 4. conversion bar chart
def conversion_chart(df):
    fig = px.bar(
        df,
        x="Campaign",
        y="Conversions",
        color="Campaign",
        title="Campaign Conversion Analysis"
    )
    return fig

# 5. Revenue vs spend scatter chart
def revenue_spend_chart(df):
    fig = px.scatter(
        df,
        x="Spend",
        y="Revenue",
        color="Campaign",
        size="Conversions",
        title="Revenue vs Spend"
    )
    return fig