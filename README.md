# E-commerce Analytics

A data analytics project for understanding online store performance: sales, customers, products, marketing, and operations. It turns raw transactional data into clean datasets, KPIs, and dashboards that support day-to-day decisions.

---

## Dashboard Preview

<p align="center">
  <img src="docs/screenshots/slideshow.gif" alt="E-Commerce Analytics dashboard slideshow" width="900">
</p>

<p align="center"><em>Auto-playing slideshow of the dashboard. Click any slide below to view it full size.</em></p>

<table>
  <tr>
    <td align="center" width="33%">
      <a href="docs/screenshots/01_executive_overview.png">
        <img src="docs/screenshots/01_executive_overview.png" alt="Executive Overview">
      </a>
      <br><b>1. Executive Overview</b>
      <br><sub>Total revenue, orders, customers, AOV and monthly revenue with a 3-month moving average</sub>
    </td>
    <td align="center" width="33%">
      <a href="docs/screenshots/02_customer_product_geo.png">
        <img src="docs/screenshots/02_customer_product_geo.png" alt="Customer segments, top countries and top products">
      </a>
      <br><b>2. Segments, Countries and Products</b>
      <br><sub>Customer segment donut, spending distribution, top 10 countries and top 10 products</sub>
    </td>
    <td align="center" width="33%">
      <a href="docs/screenshots/03_revenue_analytics.png">
        <img src="docs/screenshots/03_revenue_analytics.png" alt="Revenue Analytics">
      </a>
      <br><b>3. Revenue Analytics</b>
      <br><sub>Sales trends, order patterns and the monthly revenue trend</sub>
    </td>
  </tr>
</table>

### Dashboard pages

| Page | What it shows |
|------|---------------|
| Executive Overview | Headline KPIs and revenue performance over time |
| Revenue Analytics | Sales trends, order patterns, monthly revenue |
| Customer Intelligence | Segmentation and spending behavior |
| Product Intelligence | Top products and product performance |
| Geographic Analytics | Revenue by country |
| Customer Value Analysis | Customer lifetime value and segment value |
| Data Explorer | Browse and filter the underlying transactions |

> **Adding or updating the screenshots:** save your images in `docs/screenshots/` using the file names above, then regenerate the slideshow GIF with `python scripts/make_slideshow.py`.

---

## Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Project Structure](#project-structure)
4. [Tech Stack](#tech-stack)
5. [Getting Started](#getting-started)
6. [Data Sources](#data-sources)
7. [Data Model](#data-model)
8. [Pipeline](#pipeline)
9. [Metrics and KPIs](#metrics-and-kpis)
10. [Analyses](#analyses)
11. [Dashboards](#dashboards)
12. [Configuration](#configuration)
13. [Testing and Data Quality](#testing-and-data-quality)
14. [Deployment and Scheduling](#deployment-and-scheduling)
15. [Roadmap](#roadmap)
16. [Contributing](#contributing)
17. [Troubleshooting](#troubleshooting)
18. [License](#license)

---

## Overview

This project provides an end-to-end analytics workflow for an e-commerce business:

- **Ingest** data from the store platform, payment gateway, ad platforms, and web analytics.
- **Clean and model** it into a star schema (facts and dimensions).
- **Compute** business KPIs such as revenue, AOV, conversion rate, CAC, LTV, and retention.
- **Analyze** customer segments, product performance, funnels, cohorts, and forecasts.
- **Visualize** results in dashboards for stakeholders.

### Who is this for?

| Role | Use case |
|------|----------|
| Business / Management | Track revenue, margin, and growth |
| Marketing | Measure channel ROI, CAC, campaign performance |
| Product / Merchandising | Identify best sellers, slow movers, pricing opportunities |
| Operations | Monitor fulfillment time, returns, stock-outs |
| Data team | Maintain pipelines, models, and tests |

---

## Key Features

- Automated ETL/ELT pipeline with incremental loads
- Star-schema warehouse model (orders, order items, customers, products, dates, channels)
- Standardized KPI definitions in one place
- RFM customer segmentation
- Cohort retention and LTV analysis
- Conversion funnel analysis (session, product view, cart, checkout, purchase)
- Product and category performance, including ABC analysis
- Marketing attribution (first-touch, last-touch, linear)
- Sales forecasting (time-series)
- Market basket analysis (frequently bought together)
- Data quality checks and automated tests
- Interactive dashboards

---

## Project Structure

```
ecommerce-analytics/
├── README.md
├── requirements.txt
├── .env.example
├── config/
│   ├── settings.yaml          # Global settings
│   └── kpi_definitions.yaml   # Metric definitions
├── data/
│   ├── raw/                   # Untouched source extracts
│   ├── staging/               # Cleaned, typed data
│   ├── processed/             # Analytics-ready tables
│   └── external/              # Holidays, FX rates, benchmarks
├── sql/
│   ├── staging/               # Staging models
│   ├── marts/                 # Fact and dimension tables
│   └── metrics/               # KPI queries
├── src/
│   ├── ingestion/             # Extractors per source
│   ├── transformation/        # Cleaning and modeling
│   ├── analytics/             # RFM, cohorts, funnels, forecasting
│   ├── visualization/         # Chart and dashboard helpers
│   └── utils/                 # Logging, DB connections, helpers
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_customer_segmentation.ipynb
│   ├── 03_cohort_retention.ipynb
│   ├── 04_product_performance.ipynb
│   ├── 05_funnel_analysis.ipynb
│   └── 06_forecasting.ipynb
├── dashboards/                # BI files / app code
├── tests/                     # Unit and data-quality tests
├── scripts/                   # Run and maintenance scripts
└── docs/                      # Data dictionary, ERD, decisions
```

---

## Tech Stack

| Layer | Tools (adapt to your setup) |
|-------|-----------------------------|
| Language | Python 3.10+, SQL |
| Data processing | pandas, NumPy, SQLAlchemy |
| Warehouse | PostgreSQL / BigQuery / Snowflake / SQLite (for local dev) |
| Orchestration | Apache Airflow / cron / Prefect |
| Transformation | SQL models or dbt |
| Analysis and ML | scikit-learn, statsmodels, Prophet, mlxtend |
| Visualization | Plotly, Matplotlib, Streamlit / Power BI / Tableau / Metabase |
| Testing | pytest, Great Expectations |

---

## Getting Started

### Prerequisites

- Python 3.10 or newer
- A database or warehouse (SQLite works for local testing)
- Access credentials for your data sources

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-org>/ecommerce-analytics.git
cd ecommerce-analytics

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your credentials
```

### Quick Start

```bash
# Load sample data
python scripts/load_sample_data.py

# Run the full pipeline
python -m src.pipeline run --all

# Launch the dashboard
streamlit run dashboards/app.py
```

---

## Data Sources

| Source | Examples | Data provided |
|--------|----------|---------------|
| Store platform | Shopify, WooCommerce, Magento, custom | Orders, products, customers, inventory |
| Payments | Stripe, Razorpay, PayPal | Transactions, refunds, fees |
| Web analytics | Google Analytics 4, Mixpanel | Sessions, events, traffic source |
| Advertising | Google Ads, Meta Ads | Spend, impressions, clicks |
| Email / CRM | Mailchimp, Klaviyo | Campaigns, opens, clicks |
| Logistics | Courier / 3PL APIs | Shipments, delivery times, returns |

---

## Data Model

The warehouse follows a star schema.

### Fact tables

| Table | Grain | Key columns |
|-------|-------|-------------|
| `fact_orders` | One row per order | order_id, customer_id, order_date, status, total_amount, discount, shipping, tax, channel_id |
| `fact_order_items` | One row per order line | order_id, product_id, quantity, unit_price, line_total, cost |
| `fact_sessions` | One row per web session | session_id, customer_id, source, medium, device, started_at |
| `fact_events` | One row per user event | event_id, session_id, event_type, product_id, timestamp |
| `fact_marketing_spend` | Channel and campaign per day | date, channel_id, campaign_id, spend, impressions, clicks |
| `fact_returns` | One row per returned item | return_id, order_id, product_id, reason, refund_amount |

### Dimension tables

| Table | Description |
|-------|-------------|
| `dim_customers` | Customer attributes, signup date, location, acquisition channel |
| `dim_products` | SKU, name, category, brand, cost, price |
| `dim_date` | Calendar attributes, weekday, holiday flags, fiscal periods |
| `dim_channels` | Source, medium, campaign grouping |
| `dim_geography` | Country, state, city, pin/zip code |

### Entity relationship (simplified)

```
dim_customers ──< fact_orders >── dim_date
                     │
                     └──< fact_order_items >── dim_products
dim_channels ──< fact_sessions >── dim_customers
```

See `docs/data_dictionary.md` for full column definitions.

---

## Pipeline

```
Extract  ->  Load (raw)  ->  Stage (clean)  ->  Model (marts)  ->  Metrics  ->  Dashboards
```

1. **Extract**: Pull data via APIs, exports, or database replicas. Incremental by `updated_at`.
2. **Load**: Store untouched copies in `data/raw/` or raw schema.
3. **Stage**: Fix types, deduplicate, standardize currencies and timezones, handle nulls.
4. **Model**: Build facts and dimensions.
5. **Metrics**: Compute KPIs and aggregates.
6. **Serve**: Refresh dashboards and reports.

### Running individual steps

```bash
python -m src.pipeline extract --source shopify
python -m src.pipeline transform
python -m src.pipeline metrics
```

---

## Metrics and KPIs

All definitions live in `config/kpi_definitions.yaml` so every report uses the same logic.

### Sales

| Metric | Formula |
|--------|---------|
| Gross Revenue | Sum of order totals before refunds |
| Net Revenue | Gross revenue - refunds - discounts |
| Orders | Count of completed orders |
| Average Order Value (AOV) | Net revenue / Orders |
| Units per Order | Total units / Orders |
| Gross Margin % | (Revenue - COGS) / Revenue |

### Customer

| Metric | Formula |
|--------|---------|
| New vs Returning Customers | First-order date vs order date |
| Repeat Purchase Rate | Customers with 2+ orders / Total customers |
| Customer Lifetime Value (LTV) | Average revenue per customer x margin x expected lifespan |
| Churn Rate | Customers inactive for N days / Active base |
| Purchase Frequency | Orders / Unique customers |

### Marketing

| Metric | Formula |
|--------|---------|
| Conversion Rate | Orders / Sessions |
| Customer Acquisition Cost (CAC) | Marketing spend / New customers |
| Return on Ad Spend (ROAS) | Attributed revenue / Ad spend |
| LTV:CAC Ratio | LTV / CAC |
| Cart Abandonment Rate | 1 - (Purchases / Carts created) |

### Operations

| Metric | Formula |
|--------|---------|
| Fulfillment Time | Delivery date - Order date |
| Return Rate | Returned units / Units sold |
| Stock-out Rate | SKUs out of stock / Total active SKUs |
| Cancellation Rate | Cancelled orders / Total orders |

---

## Analyses

### 1. Exploratory Data Analysis
Revenue trends, seasonality, day-of-week and hour patterns, geographic distribution.

### 2. Customer Segmentation (RFM)
Scores customers on Recency, Frequency, and Monetary value.

| Segment | Description | Suggested action |
|---------|-------------|------------------|
| Champions | Recent, frequent, high spend | Loyalty rewards, early access |
| Loyal | Frequent buyers | Upsell, referrals |
| At Risk | Previously good, now inactive | Win-back campaigns |
| New | Recent first purchase | Onboarding emails |
| Hibernating | Long inactive, low value | Low-cost reactivation or suppress |

### 3. Cohort and Retention
Groups customers by first-purchase month and tracks repeat purchase rate and revenue over time.

### 4. Conversion Funnel
Session -> Product View -> Add to Cart -> Checkout -> Payment -> Purchase, segmented by device, source, and category to find drop-off points.

### 5. Product Performance
- Best and worst sellers by revenue, units, and margin
- ABC (Pareto) classification
- Price elasticity indicators
- Return rate by product and reason

### 6. Market Basket Analysis
Association rules (support, confidence, lift) for cross-sell and bundle ideas.

### 7. Marketing Attribution
Compares first-touch, last-touch, and linear models to evaluate channel contribution.

### 8. Forecasting
Time-series forecasts for daily and weekly revenue and orders, with holiday and promotion effects.

### 9. Pricing and Promotions
Discount impact on volume, margin, and repeat behavior.

---

## Dashboards

| Dashboard | Audience | Highlights |
|-----------|----------|------------|
| Executive Summary | Leadership | Revenue, orders, AOV, margin, YoY growth |
| Sales | Sales / Ops | Trends, category mix, regional performance |
| Customers | CRM / Marketing | New vs returning, RFM, retention, LTV |
| Marketing | Marketing | Spend, ROAS, CAC by channel and campaign |
| Funnel | Product / UX | Stage conversion, device and source splits |
| Products | Merchandising | Top and bottom SKUs, stock, returns |
| Operations | Logistics | Delivery times, cancellations, returns |

---

## Configuration

Environment variables (`.env`):

```env
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce
DB_USER=analytics
DB_PASSWORD=change_me

# Source APIs
SHOPIFY_STORE=your-store.myshopify.com
SHOPIFY_API_KEY=
STRIPE_API_KEY=
GA4_PROPERTY_ID=
GOOGLE_ADS_CUSTOMER_ID=

# App
TIMEZONE=Asia/Kolkata
CURRENCY=INR
LOG_LEVEL=INFO
```

Settings (`config/settings.yaml`):

```yaml
pipeline:
  incremental: true
  lookback_days: 3
analysis:
  rfm_quantiles: 5
  churn_threshold_days: 90
  forecast_horizon_days: 60
```

> Never commit `.env` or credentials. Add them to `.gitignore`.

---

## Testing and Data Quality

```bash
pytest tests/ -v
```

Automated checks include:

- Primary key uniqueness and not-null constraints
- Referential integrity between facts and dimensions
- Order totals equal the sum of line items minus discounts
- No negative quantities or prices
- Date ranges and freshness (data loaded within expected window)
- Reconciliation of revenue against the payment gateway

Failed checks should raise alerts (email or Slack) and block downstream refresh.

---

## Deployment and Scheduling

- **Daily run**: full incremental refresh at a low-traffic hour (for example 02:00 IST).
- **Hourly run** (optional): orders and sessions for near-real-time dashboards.
- **Orchestration**: Airflow DAG at `scripts/airflow_dag.py`, or a cron entry:

```cron
0 2 * * * /path/to/.venv/bin/python -m src.pipeline run --all >> logs/pipeline.log 2>&1
```

- **Environments**: `dev`, `staging`, `prod` with separate schemas.

---

## Roadmap

- [ ] Real-time event streaming
- [ ] Churn prediction model
- [ ] Product recommendation engine
- [ ] Customer LTV prediction (ML)
- [ ] A/B test analysis module
- [ ] Inventory demand forecasting
- [ ] Anomaly detection and alerting

---

## Contributing

1. Fork the repository and create a branch: `git checkout -b feature/your-feature`
2. Follow the code style (`black`, `ruff`) and add tests.
3. Update documentation for any new metric or table.
4. Open a pull request with a clear description.

---

## Troubleshooting

| Issue | Likely cause | Fix |
|-------|--------------|-----|
| Revenue mismatch with payment gateway | Refunds or timezone differences | Check refund handling and align timezones |
| Duplicate orders | Re-run of incremental load | Ensure upserts on `order_id` |
| Empty dashboard | Pipeline failed or stale data | Check `logs/` and freshness tests |
| API rate limit errors | Too many requests | Add backoff and reduce batch size |
| Wrong conversion rate | Bot or internal traffic | Filter known bots and internal IPs |

---

## License

Released under the MIT License. See `LICENSE` for details.

---

## Contact

For questions or support, open an issue or contact the analytics team.
