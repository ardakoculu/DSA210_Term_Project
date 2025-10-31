# DSA210_Term_Project
Sabancı University DSA210 Fall 2025 Project
# Project Proposal: The Impact of U.S. Federal Reserve Policy Rate Changes on Financial Markets

## 1. Project Proposal
This project aims to analyze how **changes in the U.S. Federal Reserve’s policy rate (Federal Funds Rate)** influence major **financial market indicators** such as bond yields, stock market indices, and credit-related variables.  

The purpose is to identify whether monetary tightening (rate hikes) and easing (rate cuts) produce measurable patterns in financial markets.  
By applying data science techniques — including exploratory data analysis and correlation testing — the project will determine the strength and direction of relationships between policy rates and financial variables over time.

---

## 2. Data to Be Used
All data will be sourced from **institutional and publicly available** databases to ensure reliability and transparency.

| Source | Description | Frequency |
|--------|--------------|------------|
| **Federal Reserve Economic Data (FRED)** | Effective Federal Funds Rate (FEDFUNDS) | Monthly |
| **OECD Data Portal** | U.S. financial and credit market indicators (e.g., lending, financial accounts) | Quarterly |
| **World Bank Global Financial Development Database** | Market capitalization, private sector credit, financial depth ratios | Annual |
| **IMF International Financial Statistics (optional)** | U.S. government bond yields and short-term rates | Monthly |


---

## 3. Data Collection Plan
1. **Download data** directly from the official portals (FRED, OECD, World Bank, IMF) as CSV or Excel files.  
2. **Unify frequencies** by converting all datasets to a common time format (monthly or quarterly) and aligning by date.  
3. **Clean and preprocess** the data by:  
   - Handling missing values with interpolation or forward fill.  
   - Selecting only relevant columns (policy rate, bond yields, credit indicators).  
4. **Merge** datasets using their time index to build one integrated financial dataset.  
5. **Store** the cleaned and merged files in a `/data` folder for analysis in later stages.

---

**End of Proposal**

