import pandas as pd
import streamlit as st
import plotly.express as px
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

# --- Load Data ---
daily = pd.read_csv("data/daily_totals.csv")
platform = pd.read_csv("data/platform_daily.csv")
campaign = pd.read_csv("data/campaign_totals.csv")

# --- Convert date columns if exist ---
if 'date' in daily.columns:
    daily['date'] = pd.to_datetime(daily['date'])
if 'date' in platform.columns:
    platform['date'] = pd.to_datetime(platform['date'])

# ====== SUMMARY / KPI PANEL ======
st.sidebar.header("Summary Insights")

# Overall KPIs
total_revenue = daily['total revenue'].sum()
total_spend = daily['spend'].sum()
overall_roas = total_revenue / total_spend if total_spend != 0 else 0
total_new_customers = daily['new customers'].sum() if 'new customers' in daily.columns else 0
avg_cpa = total_spend / total_new_customers if total_new_customers != 0 else 0  # Cost per acquisition

# Display KPIs
st.sidebar.metric("Total Revenue", f"${total_revenue:,.0f}")
st.sidebar.metric("Total Spend", f"${total_spend:,.0f}")
st.sidebar.metric("Overall ROAS", f"{overall_roas:.2f}")
st.sidebar.metric("Average CPA", f"${avg_cpa:.2f}")

# Platform-level insights
platform_roas = platform.groupby('platform').apply(
    lambda df: df['attributed revenue'].sum() / df['spend'].sum() if df['spend'].sum() != 0 else 0
).sort_values(ascending=False)

top_platform = platform_roas.idxmax()
top_platform_roas = platform_roas.max()
bottom_platform = platform_roas.idxmin()
bottom_platform_roas = platform_roas.min()

st.sidebar.markdown(f"**Top Platform:** {top_platform} with ROAS {top_platform_roas:.2f}")
st.sidebar.markdown(f"**Underperforming Platform:** {bottom_platform} with ROAS {bottom_platform_roas:.2f}")

# Top Campaign insight
campaign_roas = campaign.groupby('campaign').apply(
    lambda df: df['attributed revenue'].sum() / df['spend'].sum() if df['spend'].sum() != 0 else 0
)
top_campaign = campaign_roas.idxmax()
top_campaign_roas = campaign_roas.max()
bottom_campaign = campaign_roas.idxmin()
bottom_campaign_roas = campaign_roas.min()

st.sidebar.markdown(f"**Top Campaign:** {top_campaign} (ROAS {top_campaign_roas:.2f})")
st.sidebar.markdown(f"**Underperforming Campaign:** {bottom_campaign} (ROAS {bottom_campaign_roas:.2f})")

# Optional recommendations
st.sidebar.markdown("---")
st.sidebar.markdown("**Recommendations:**")
if bottom_platform_roas < 1:
    st.sidebar.markdown(f"- Consider optimizing spend on {bottom_platform}.")
if bottom_campaign_roas < 1:
    st.sidebar.markdown(f"- Review strategy for {bottom_campaign}, it may be underperforming.")
if overall_roas > 2:
    st.sidebar.markdown(f"- Overall ROAS is strong, maintain budget allocation accordingly.")

# --- Sidebar Filters ---
st.sidebar.header("Filters")

platform_options = platform['platform'].unique().tolist()
selected_platforms = st.sidebar.multiselect("Select Platform(s)", platform_options, default=platform_options)

campaign_options = campaign['campaign'].unique().tolist()
selected_campaigns = st.sidebar.multiselect("Select Campaign(s)", campaign_options, default=campaign_options)

# Default date range filter
if 'date' in daily.columns:
    min_date = daily['date'].min()
    max_date = daily['date'].max()
    selected_dates = st.sidebar.date_input("Select Date Range", [min_date, max_date])
else:
    selected_dates = [None, None]

# --- Filter Data ---
daily_filtered = daily.copy()
if selected_dates[0] and 'date' in daily.columns:
    daily_filtered = daily_filtered[(daily_filtered['date'] >= pd.to_datetime(selected_dates[0])) &
                                    (daily_filtered['date'] <= pd.to_datetime(selected_dates[1]))]

platform_filtered = platform[platform['platform'].isin(selected_platforms)]
campaign_filtered = campaign[campaign['campaign'].isin(selected_campaigns)]

# --- KPIs ---
st.title("Marketing Intelligence Dashboard")
total_revenue = daily_filtered['total revenue'].sum()
total_spend = daily_filtered['spend'].sum()
overall_roas = total_revenue / total_spend if total_spend > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Spend", f"${total_spend:,.0f}")
col3.metric("Overall ROAS", f"{overall_roas:.2f}")

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["Daily Trends", "Platform Analysis", "Top Campaigns"])

# --- Daily Trends with Plotly ---
with tab1:
    st.subheader("Daily Revenue vs Spend")
    fig = px.line(daily_filtered, x='date', y=['total revenue', 'spend'],
                  labels={'value':'Amount ($)', 'date':'Date', 'variable':'Metric'},
                  title="Daily Revenue and Spend")
    st.plotly_chart(fig, use_container_width=True)

# --- Platform Analysis with ROAS coloring ---
with tab2:
    st.subheader("ROAS by Platform")
    if 'attributed revenue' in platform_filtered.columns:
        platform_filtered['ROAS'] = platform_filtered['attributed revenue'] / platform_filtered['spend']
    fig2 = px.bar(platform_filtered, x='platform', y='ROAS', color='ROAS', 
                  color_continuous_scale='RdYlGn', text='ROAS',
                  title="ROAS per Platform")
    st.plotly_chart(fig2, use_container_width=True)

# --- Top Campaigns Interactive Table ---
with tab3:
    st.subheader("Top Campaigns by ROAS")
    if 'attributed revenue' in campaign_filtered.columns:
        campaign_filtered['ROAS'] = campaign_filtered['attributed revenue'] / campaign_filtered['spend']
    top_campaigns = campaign_filtered.sort_values('ROAS', ascending=False).head(20)

    # --- AgGrid interactive table ---
    gb = GridOptionsBuilder.from_dataframe(top_campaigns[['campaign', 'platform', 'ROAS', 'impression', 'clicks', 'spend', 'attributed revenue']])
    gb.configure_default_column(editable=False, sortable=True, filter=True)
    gb.configure_grid_options(domLayout='normal')
    gridOptions = gb.build()

    AgGrid(top_campaigns[['campaign', 'platform', 'ROAS', 'impression', 'clicks', 'spend', 'attributed revenue']], gridOptions=gridOptions, height=400)
