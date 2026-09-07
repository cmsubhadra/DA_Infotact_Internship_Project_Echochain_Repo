# 🔄 EchoChain: Circular Economy & Secondary Market Lifecycle Analytics

## 📌 Project Overview

EchoChain is a Data Engineering and Business Intelligence project developed as part of the **Infotact Solutions Internship**.

The project focuses on analyzing product lifecycle, Bill of Materials (BOM), warranty information, component reliability, and secondary-market data to support **circular-economy, resale, refurbishment, and product lifecycle decisions**.

The project combines internal product data with secondary-market marketplace data and processes the data through a Databricks Lakehouse architecture before presenting the final analytics through Power BI.

---

## 👥 Team Members

- **C.M. Subhadra**
- **Nandhana K.S.**

---

## 🎯 Problem Statement

Manufacturers mainly track products until the point of sale. After that, the post-sale lifecycle becomes a data blind spot.

This limits visibility into:

- Product resale opportunities
- Secondary-market value
- Product condition
- Component lifecycle
- Component reliability
- Warranty-related failures
- Failure-related costs
- Component reuse and refurbishment opportunities
- Circular-economy performance

EchoChain aims to combine internal product information with secondary-market data to provide better visibility into the product lifecycle beyond the initial sale.

---

## 🎯 Project Objectives

- Collect secondary-market marketplace data using **Scrapy**.
- Store product, BOM, warranty, and marketplace data using **Databricks and Delta Lake**.
- Build a structured **Bronze data layer**.
- Clean and validate data using **PySpark**.
- Create a structured **Silver data layer**.
- Perform fuzzy matching between marketplace listings and internal products.
- Build a **Gold analytics layer**.
- Calculate resale, depreciation, reliability, failure-cost, and circularity metrics.
- Build interactive business intelligence dashboards using **Power BI**.
- Support circular-economy and secondary-market lifecycle analytics.

---

## 🛠️ Technology Stack

- **Python**
- **Scrapy**
- **Databricks Free Edition**
- **Apache Spark / PySpark**
- **Delta Lake**
- **Databricks SQL Warehouse**
- **Power BI Desktop**
- **DAX**
- **SQL**
- **VS Code**
- **Git & GitHub**

---

## 🏗️ Project Architecture

```text
Internal Product Data + Secondary-Market Data
                    │
                    ▼
              Python / Scrapy
                    │
                    ▼
                Databricks
                    │
                    ▼
          Delta Lake – Bronze Layer
                    │
                    ▼
             PySpark / SQL
                    │
                    ▼
          Delta Lake – Silver Layer
                    │
                    ▼
       Fuzzy Matching + Data Processing
                    │
                    ▼
           Delta Lake – Gold Layer
                    │
                    ▼
                Power BI
                    │
                    ▼
          Executive Dashboards
```

---

## 🔄 Project Workflow

1. Prepared internal Products, BOM, Warranty, and Marketplace datasets.
2. Established the marketplace data collection process using Scrapy.
3. Generated marketplace data in JSON format.
4. Uploaded the datasets into Databricks.
5. Created Bronze Delta tables.
6. Cleaned and validated the datasets using PySpark.
7. Created Silver-layer tables.
8. Established product-level relationships between Products, BOM, Warranty, and Marketplace data.
9. Implemented fuzzy matching between marketplace listings and internal products.
10. Created the Gold analytics dataset.
11. Calculated product lifecycle and circularity metrics.
12. Connected the Gold analytics dataset to Power BI.
13. Built the final executive dashboard.
14. Added interactive filters, navigation, and lifecycle analysis.
15. Validated and finalized the dashboard for project submission.

---

## 📂 Repository Structure

```text
EchoChain/
│
├── data/
│
├── databricks/
│
├── powerbi_Nandhana/
│
├── PowerBi_Subhadra/
│
├── scrapy_project/
│
├── venv/
│
├── .gitignore
│
├── EchoChain_Week1_Progress_Report.docx
├── EchoChain_Week2_Progress_Report.docx
├── EchoChain_Week3_Progress_Report.docx
│── EchoChain_Week4_Progress_Report.docx
│
└── README.md
```

> **Note:** The `venv/` directory is a local Python virtual environment and should normally be excluded from version control using `.gitignore`.

---

# 📅 Weekly Progress

## ✅ Week 1 – Data Acquisition & Environment Setup

- Created the EchoChain project structure and local data folder in VS Code.
- Prepared Products, BOM, Warranty, and Marketplace datasets.
- Created a Python 3.11.3 virtual environment.
- Installed and configured Scrapy 2.17.0.
- Created the Scrapy project and Marketplace spider.
- Generated `marketplace_scraped.json` with **26 marketplace records**.
- Created the Databricks Free Edition workspace.
- Created Bronze tables for Products, BOM, Warranty, and Marketplace.
- Established the initial Delta Lake Bronze storage foundation.
- Created and verified the Databricks Serverless Starter Warehouse.
- Configured the Databricks SQL connection for Power BI Desktop.
- Connected Power BI Desktop to the Databricks SQL Warehouse.
- Loaded `bronze_bom` and `bronze_warranty` into Power BI.
- Verified the available BOM and Warranty fields for the initial BI model.

The initial Power BI model was connected to the Databricks Bronze layer and included:

- BOM data
- Warranty data

The available fields were verified as the foundation for the upcoming data modelling and analytics stages.

---

## ✅ Week 2 – Data Transformation & Data Modeling

### Data Engineering

- Created separate Databricks notebooks for Silver-layer processing.
- Created and validated the `silver_products` table.
- Created and validated the `silver_bom` table.
- Created and validated the `silver_warranty` table.
- Created and validated the `silver_marketplace` table.
- Checked schemas, missing values, duplicate records, and data types.
- Standardized SKU and component identifiers for reliable relationships.
- Validated warranty `failure_rate` values.
- Confirmed that no records had `failure_rate` greater than 1.
- Prepared cleaned Silver tables for downstream matching and analytics.

### Power BI Data Modeling

- Connected Power BI Desktop to the Databricks environment.
- Prepared the Power BI model using:
  - `silver_products`
  - `silver_bom`
  - `silver_warranty`
  - `silver_marketplace`
- Created the Products → BOM relationship using `sku`.
- Created the Products → Warranty relationship using `sku`.
- Created the Products → Marketplace relationship using `sku` and `matched_sku`.
- Used `silver_products` as the central product-level table.
- Prepared product-level filtering to verify that related BOM, Warranty, and Marketplace data responded correctly.

---

## ✅ Week 3 – Advanced Analytics & Gold Layer

### Data Engineering

- Implemented fuzzy matching between marketplace listings and internal product/SKU data.
- Used token-based similarity, Levenshtein similarity, and model/size matching to identify the best product match.
- Combined matching signals using a weighted matching score.
- Selected the best matching SKU for each marketplace listing.
- Created the Gold base dataset by combining fuzzy-matching results with marketplace and product information.
- Calculated secondary-market depreciation using original price and secondary-market price.
- Combined BOM and Warranty information for component-level lifecycle analysis.
- Created component-level metrics and aggregated them to the SKU level.
- Calculated **Total Component Cost**.
- Calculated **Weighted Failure Cost**.
- Calculated **Component Reliability Score**.
- Calculated **Resale Retention Score**.
- Calculated the **Circularity Score** using resale retention and component reliability.
- Created and validated the final Gold analytics dataset.
- Saved the final Gold analytics table.

### Power BI

- Created a new Power BI report for the Gold-layer analytics.
- Connected the final `gold_echochain_analytics` table to Power BI.
- Created a DAX measure for **Average Secondary Market Depreciation**.
- Created a DAX measure for **Average Circularity Score**.
- Created KPI visuals for the key analytical metrics.

---

## ✅ Week 4 – Finalization & Executive Dashboard

### Data Engineering

- Reviewed and validated the final Gold-layer analytics dataset used for the dashboard.
- Verified the product-level marketplace, resale, depreciation, circularity, reliability, and component-cost metrics required for final reporting.
- Validated the final analytical data before connecting it to the completed Power BI report.
- Prepared the final project data and dashboard outputs for submission.

### Power BI & Business Intelligence

- Finalized the EchoChain Power BI report and executive dashboard.
- Created the **Executive Overview** page with key KPIs for:
  - Circularity Score
  - Secondary Market Depreciation
  - Resale Retention
- Created the **Secondary Market Lifecycle Analytics** page for:
  - Product performance
  - Resale value
  - Failure-cost analysis
  - Drill-down visuals
- Created the **Component Lifecycle Analysis** page with:
  - Component Reliability
  - Weighted Failure Cost
  - Total Component Cost analysis by product
- Added navigation between dashboard pages.
- Added interactive filters for product-level analysis.
- Reviewed dashboard layout, visual titles, subtitles, aggregations, and interactive elements.
- Validated the final analytical outputs.
- Completed the final dashboard and submitted the project deliverables.

---

# 📊 Final Power BI Dashboard

The final EchoChain Power BI dashboard provides an integrated view of product circularity, secondary-market performance, resale value, component reliability, component cost, and failure-related costs.

### Dashboard Pages

#### 1. Executive Overview

Provides an overall business view.

#### 2. Secondary Market Lifecycle Analytics

Provides detailed product and marketplace analysis.

#### 3. Component Lifecycle Analysis

Provides component-related insights.

---

# 📈 Key Project Results

| Metric | Result |
|---|---:|
| Average Circularity Score | **65.08** |
| Average Secondary Market Depreciation | **57.14%** |
| Average Resale Retention Score | **42.86%** |

The final dashboard brings together product lifecycle, secondary-market, component, reliability, and circularity analytics into a single Power BI reporting solution.

---

# 🗄️ Data Layers

### Bronze Layer

Contains the initial/raw datasets stored in Delta Lake:

- Products
- BOM
- Warranty
- Marketplace

### Silver Layer

Contains cleaned and validated datasets:

- `silver_products`
- `silver_bom`
- `silver_warranty`
- `silver_marketplace`

### Gold Layer

Contains the final analytics-ready dataset:

```text
gold_echochain_analytics
```

The Gold layer combines product, marketplace, BOM, and warranty information with calculated lifecycle and circularity metrics.

---

# 📚 Learning Outcomes

This project provided practical experience in:

- Python Programming
- Web Scraping with Scrapy
- Databricks
- Delta Lake
- Apache Spark / PySpark
- Bronze, Silver, and Gold Data Architecture
- Data Cleaning and Validation
- Fuzzy Matching
- Databricks SQL Warehouse
- Power BI
- DAX
- Data Engineering
- Business Intelligence
- Git & GitHub Collaboration
- Circular Economy Analytics
- Secondary Market Analytics
- Product Lifecycle Analytics

---

# 🚀 Project Status

🟢 **Week 1 – Completed**  
🟢 **Week 2 – Completed**  
🟢 **Week 3 – Completed**  
🟢 **Week 4 – Completed**

### 🏁 Project Status: Completed

EchoChain successfully combines data engineering, marketplace data processing, lifecycle analytics, and business intelligence to provide insights into product resale, circularity, component reliability, and secondary-market performance.