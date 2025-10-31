# DSA210_Term_Project
Sabancı University DSA210 Fall 2025 Project
# The Impact of Interest Rate Changes on Financial Markets and Economic Indicators
**Fall 2025 – Project Proposal**  
**Author:** Arda Koçulu  
**Date:** 31 October 2025  

---

## Project Overview
This project investigates how **interest rate changes** — one of the most powerful monetary policy tools — influence various aspects of the financial system and the economy.  
By combining historical data on **central bank interest rates**, **stock market indices**, and **bond yields**, the study aims to measure the extent and direction of relationships between these key indicators.  

The overall goal is to identify how different sectors and markets respond to tightening or easing monetary conditions.  
Ultimately, the project will provide a data-driven overview of how financial markets adapt to changes in interest rate policies.

---

## Motivation
Interest rate policy is a central mechanism through which monetary authorities regulate inflation, stabilize currencies, and influence investment behavior.  
Even small rate changes can ripple through the economy — affecting borrowing costs, investment strategies, bond prices, and stock valuations.  

This project explores these dynamics using real-world data, seeking to quantify how rate changes shape financial and economic trends.

---

## Data Sources
This study will use **publicly available datasets** from credible sources:

1. **Interest Rate Data:**  
   - Central Bank of Turkey (TCMB) or Federal Reserve (FRED API)  
   - Variables: policy interest rate, discount rate, date  

2. **Stock Market Indices:**  
   - Yahoo Finance via `yfinance` library  
   - Indices: S&P 500, NASDAQ, BIST 100, and optionally sectoral ETFs (Finance, Tech, Energy)  
   - Variables: closing price, daily/weekly/monthly returns  

3. **Bond Yields:**  
   - U.S. Treasury Yield Curve or Turkish Government Bonds (Kaggle or FRED)  
   - Variables: 2-year and 10-year yields  

4. **Macroeconomic Indicators (optional enrichment):**  
   - World Bank or OECD Data  
   - Variables: GDP growth, inflation rate, unemployment rate  

---

## Data Collection Plan
- Use **Python** with libraries such as `pandas`, `yfinance`, and `requests` to pull and clean data.  
- Align datasets on a **monthly or quarterly** time scale for comparability.  
- Handle missing or irregular data using interpolation and normalization methods.  
- Store cleaned data in a `/data` folder in CSV format.  

---

## 🔍 Analysis Plan
1. **Exploratory Data Analysis (EDA):**  
   - Visualize trends of interest rate vs market indices and bond yields.  
   - Calculate and plot correlation matrices.  
   - Investigate lag effects between policy changes and market responses.

2. **Statistical Testing:**  
   - Conduct hypothesis tests to check whether interest rate changes significantly affect stock indices or bond yields.  
   - Example hypothesis:  
     - H₀: Interest rate changes have no significant effect on market indicators.  
     - H₁: Interest rate changes significantly affect market indicators.

3. **Regression / Machine Learning (later stage):**  
   - Build a **linear regression** or **multiple regression** model to predict stock or bond movements using interest rates and macro variables.  
   - Evaluate model performance using R² and residual analysis.

---

## Expected Findings
- Negative correlation between interest rate increases and stock market performance.  
- Positive correlation between interest rates and bond yields.  
- Sector-specific differences — financial sectors may show delayed or opposite responses.  

---

## ⚙️ Tools and Libraries

