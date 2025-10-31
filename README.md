# DSA210_Term_Project
Sabancı University DSA210 Fall 2025 Project
# The Impact of U.S. Federal Reserve Policy Rate Changes on Financial Markets and Economic Indicators

---

## 📘 Project Overview
This project examines how **U.S. Federal Reserve policy rate changes** influence key components of the American financial system — including **stock market indices, bond yields, and sector performance.**  
The Federal Funds Rate is one of the most critical levers in the global economy, guiding everything from borrowing costs to investment flows.  

By combining historical data on the Fed’s policy decisions with major U.S. market indicators, this study aims to uncover the strength, direction, and timing of these relationships.  
The overall goal is to produce a clear, data-driven picture of how markets react to periods of tightening (rate hikes) and easing (rate cuts).

---

## 🧭 Motivation
Every Federal Reserve rate decision can shift global capital markets within minutes.  
When the Fed raises rates, borrowing becomes expensive, corporate investments often slow, and stock prices may drop.  
When the Fed cuts rates, liquidity increases, risk appetite rises, and stock markets tend to recover.  

This project seeks to quantify these relationships using **data science methods** — exploring how changes in the **Federal Funds Rate** correlate with **market indices, bond yields, and sector performance** over time.

---

## 📊 Data Sources
All data will be **publicly available** and collected through APIs or online datasets.

1. **Federal Reserve Interest Rate Data (FRED):**  
   - Source: [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/)  
   - Series: “Effective Federal Funds Rate (FEDFUNDS)”  
   - Variables: date, rate (%)

2. **Stock Market Data (Yahoo Finance via `yfinance`):**  
   - Indices: S&P 500 (`^GSPC`), NASDAQ Composite (`^IXIC`), and Dow Jones Industrial Average (`^DJI`)  
   - Variables: adjusted close, returns  

3. **Bond Yield Data (FRED / Yahoo Finance):**  
   - 10-Year Treasury Constant Maturity Rate (DGS10)  
   - 2-Year Treasury Yield (DGS2)  

4. **Sector ETFs (optional extension):**  
   - Financial Sector (XLF), Technology (XLK), Energy (XLE), Consumer Discretionary (XLY)  
   - Source: Yahoo Finance  

---

## 🧩 Data Collection Plan
- Fetch Fed Funds Rate data directly from **FRED API** using `pandas_datareader`.  
- Collect stock and bond data using the **`yfinance`** library.  
- Merge datasets by **month or quarter** to align macro and market indicators.  
- Handle missing values through interpolation and standardize scales for comparison.  
- Store all processed data as `.csv` files inside a `/data` folder.

---

## 🔍 Analysis Plan
1. **Exploratory Data Analysis (EDA):**  
   - Plot historical trends of the Fed Funds Rate vs S&P 500 returns and bond yields.  
   - Compute correlation coefficients and visualize with heatmaps.  
   - Identify reaction patterns around rate hike and cut periods.  

2. **Statistical Testing:**  
   - Perform correlation and regression analyses to test whether Fed rate changes significantly affect market variables.  
   - Hypotheses:  
     - H₀: Fed rate changes have no significant impact on market indices or bond yields.  
     - H₁: Fed rate changes significantly influence these financial indicators.  

3. **Regression / Machine Learning (later phase):**  
   - Apply **multiple linear regression** to predict market index changes using:  
     - Federal Funds Rate,  
     - Bond yields,  
     - Inflation or GDP growth (optional macro control variables).  
   - Evaluate using R², residuals, and predictive error metrics.  

---

## 💡 Expected Findings
- **Negative correlation** between Fed rate increases and stock market performance.  
- **Positive correlation** between policy rate and bond yields.  
- Evidence of **sector-specific differences** — e.g., financial stocks may initially benefit from moderate rate hikes.  
- Possible **lag effect** — markets may react a few months after a policy change.

---

## ⚙️ Tools and Libraries
