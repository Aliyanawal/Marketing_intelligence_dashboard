import pandas as pd

# Load the CSVs
daily = pd.read_csv("data/daily_totals.csv")
platform = pd.read_csv("data/platform_daily.csv")
campaign = pd.read_csv("data/campaign_totals.csv")

# Print the column names
print("Daily columns:", daily.columns.tolist())
print("Platform columns:", platform.columns.tolist())
print("Campaign columns:", campaign.columns.tolist())
