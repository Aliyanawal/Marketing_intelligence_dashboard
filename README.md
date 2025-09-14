# Marketing Intelligence Dashboard

An interactive BI dashboard that helps business stakeholders understand how marketing activity impacts business outcomes. Built with **Python, Streamlit, Plotly, and AgGrid**.

---

## 🚀 Features

- **KPI Summary Panel:**  
  Displays total revenue, total spend, overall ROAS, average CPA, top and underperforming platforms, and top campaigns.  
- **Interactive Filters:**  
  Filter data by platform, campaign, and date range.  
- **Daily Trends:**  
  Line chart showing daily revenue and spend.  
- **Platform Analysis:**  
  ROAS per platform visualized with color coding.  
- **Top Campaigns Table:**  
  Interactive table (AgGrid) to explore top campaigns by ROAS, impressions, clicks, and spend.  
- **Recommendations:**  
  Automatically provides insights and suggestions based on performance.

---

## 📊 Tech Stack

- Python 3.12
- [Streamlit](https://streamlit.io/) – for dashboard UI
- [Pandas](https://pandas.pydata.org/) – for data processing
- [Plotly](https://plotly.com/python/) – for interactive charts
- [st-aggrid](https://pypi.org/project/streamlit-aggrid/) – for interactive tables

---

## 📂 Folder Structure
LifeSight/
├─ data/
│ ├─ Facebook.csv
│ ├─ Google.csv
│ ├─ TikTok.csv
│ ├─ Business.csv
│ ├─ daily_totals.csv
│ ├─ platform_daily.csv
│ └─ campaign_totals.csv
├─ venv/ (Python virtual environment)
├─ dashboard.py
└─ README.md


---

## ⚡ How to Run Locally

1. **Clone the repo (or use your local copy)**:
   ```bash
   git clone https://github.com/Aliyanawal/Marketing_intelligence_dashboard.git
   cd Marketing_intelligence_dashboard

2. **Create and activate a virtual environment:**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows

3. **Install dependencies:**:
    ```bash
    pip install -r requirements.txt

3. **Run the dashboard**:
    ```bash
    streamlit run dashboard.py
    
## 📈 Insights & Product Thinking

ROAS highlights the most efficient marketing platforms.

Interactive campaign table allows prioritization of high-performing campaigns.

Automatically surfaces top and underperforming campaigns and platforms.

Recommendations included for optimization based on spend and ROAS.


---

### 4️⃣ Add dataset info
```markdown
The data folder contains CSV files with campaign metrics:


daily_totals.csv:Aggregated daily metrics for all platforms
platform_daily.csv:Platform-level daily metrics (Facebook, Google, TikTok, Business)
campaign_totals.csv:Metrics for individual campaigns including ROAS, spend, impressions, clicks

Metrics include: impressions, clicks, spend, attributed revenue, # of orders, new customers, total revenue, CTR, CPC, ROAS.
## Dataset

The `data` folder contains CSV files:
- `daily_totals.csv`
- `platform_daily.csv`
- `campaign_totals.csv`

These contain campaign metrics such as impressions, clicks, spend, attributed revenue, ROAS, etc.


## Hosted Dashboard

You can view the live dashboard here: [LifeSight Dashboard](YOUR_STREAMLIT_DEPLOY_URL)









    

