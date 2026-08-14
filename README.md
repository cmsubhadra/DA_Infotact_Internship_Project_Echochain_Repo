# 🔄 EchoChain: Circular Economy & Secondary Market Lifecycle Analytics

## 📌 Project Overview

EchoChain is a Data Engineering and Business Intelligence project developed as part of the **Infotact Solutions Internship**. The project focuses on analyzing product lifecycle, Bill of Materials (BOM), warranty information, and secondary-market data to support circular-economy and resale analytics.

---

## 👥 Team Members

- C.M. Subhadra
- Nandhana K.S.

---

## 🎯 Problem Statement

Manufacturers track products mainly until the point of sale. After that, the product lifecycle becomes difficult to monitor. This limits visibility into environmental impact, landfill diversion, component reuse, warranty lifecycle, and secondary-market opportunities.

EchoChain aims to combine internal product data with secondary-market information to support better product lifecycle and circular-economy decisions.

---

## 🎯 Project Objectives

- Collect secondary-market marketplace data using Scrapy.
- Store product, BOM, warranty, and marketplace data using Databricks and Delta Lake.
- Build a structured Bronze data layer.
- Process and transform data using PySpark.
- Integrate internal product information with secondary-market data.
- Build business intelligence dashboards using Power BI.
- Support circular-economy and secondary-market lifecycle analytics.

---

## 🛠️ Technology Stack

- Python
- Scrapy
- Databricks Free Edition
- Apache Spark / PySpark
- Delta Lake
- Databricks SQL Warehouse
- Power BI Desktop
- SQL
- VS Code
- Git & GitHub

---

## 🏗️ Project Architecture

```text
Internal Product Data + Secondary-Market Data
                    │
                    ▼
             Scrapy / Python
                    │
                    ▼
               Databricks
                    │
                    ▼
              Delta Lake
             Bronze Layer
                    │
                    ▼
             PySpark / SQL
                    │
                    ▼
          Analytics-Ready Data
                    │
                    ▼
                Power BI
               Dashboard
               


## 📂 Repository Structure  

EchoChain/
│
├── data/
├── scrapy_project/
├── scripts/
├── databricks/
├── notebooks/
├── powerbi/
│
├── README.md
└── .gitignore  

```
---

## ✅ Week 1 Progress
             
Created the EchoChain project structure and local data folder in VS Code.
Prepared Products, BOM, Warranty, and Marketplace datasets.
Created a Python 3.11.3 virtual environment.
Installed and configured Scrapy 2.17.0.
Created the Scrapy project and Marketplace spider.
Generated marketplace_scraped.json with 26 marketplace records.
Created the Databricks Free Edition workspace.
Created Bronze tables for Products, BOM, Warranty, and Marketplace.
Established the initial Delta Lake Bronze storage foundation.
Created and verified the Databricks Serverless Starter Warehouse.
Configured the Databricks SQL connection for Power BI Desktop.
Connected Power BI Desktop to the Databricks SQL Warehouse.
Loaded bronze_bom and bronze_warranty into Power BI.
Verified the available BOM and Warranty fields for the initial BI model.

## 📊 Initial BI Data

The initial Power BI model was connected to the Databricks Bronze layer and included:

BOM data
Warranty data

The available fields were verified as the foundation for the upcoming data modelling and analytics stages.

## 📚 Learning Outcomes

This project provides practical experience in:

Python Programming
Web Scraping with Scrapy
Databricks
Delta Lake
Apache Spark / PySpark
Bronze Layer Data Architecture
Databricks SQL Warehouse
Power BI
Data Engineering
Business Intelligence
Git & GitHub Collaboration
Circular Economy Analytics


## 🚀 Project Status

🟢 Week 1 – Completed

🟡 Week 2 – In Progress

⚪ Week 3 – Upcoming

⚪ Week 4 – Upcoming





