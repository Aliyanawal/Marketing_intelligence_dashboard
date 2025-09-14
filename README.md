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

### 4️⃣ <img width="1915" height="915" alt="Screenshot 2025-09-14 112539" src="https://github.com/user-attachments/assets/33a5a06f-0f72-44bb-b791-5ecd5e276dd2" />
<img width="1918" height="899" alt="Screenshot 2025-09-14 112626" src="https://github.com/user-attachments/assets/99795413-6756-45f1-94c5-2f0d2a55a72d" />
<img width="1898" height="890" alt="Screenshot 2025-09-14 112618" src="https://github.com/user-attachments/assets/83011b73-b1b1-40b3-9eb8-22c7080a0932" />
<img width="1899" height="900" alt="Screenshot 2025-09-14 112605" src="https://github.com/user-attachments/assets/d6bfefc0-046a-4f8b-90c8-97c7031353c1" />
<img width="1904" height="896" alt="Screenshot 2025-09-14 112553" src="https://github.com/user-attachments/assets/a0a7a393-8aef-49e3-a80f-284b8826a3ba" />
<img width="1915" height="915" alt="Screenshot 2025-09-14 112539" src="https://github.com/user-attachments/assets/d6fb0cd3-1fee-4e69-9beb-37fb8d7b8d39" />
dataset info

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

You can view the live dashboard here: [LifeSight Dashboard](https://github.com/Aliyanawal/Marketing_intelligence_dashboard)









    

