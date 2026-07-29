import plotly.express as px

def campaign_chart(df):
    fig = px.chart(
        df,
        x = "Campaign",
        y = "Spend",
        color = "Campaign",
        title = "Campaign wise spend"
    )
    return fig
    