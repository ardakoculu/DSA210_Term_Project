# DSA210_Term_Project
Sabancı University DSA210 Fall 2025 Project
# The Impact of U.S. Federal Reserve Policy Rate Changes on Financial Markets and Economic Indicators

---

## 📘 Project Overview
This project investigates how changes in the **U.S. Federal Reserve’s policy rate (Federal Funds Rate)** affect key aspects of the financial system — including **stock indices, bond yields, and sector-level performance**.  
By analyzing real historical data from the **Federal Reserve (FRED)** and **Yahoo Finance**, the project aims to uncover how markets react to tightening and easing monetary policies.  

This topic directly relates to the **core data science pipeline** taught in DSA210 — data collection, cleaning, exploratory analysis, statistical testing, and visualization — applied to a real-world economic question.

---

## 🧠 Research Motivation & Hypothesis
Interest rates are central to macroeconomic control. When the Fed raises rates, borrowing costs rise, risk-taking decreases, and market liquidity contracts — often leading to lower stock valuations. Conversely, rate cuts encourage borrowing and stimulate growth.

**Hypothesis:**  
> Increases in the Federal Funds Rate are negatively correlated with U.S. stock market returns and positively correlated with bond yields.

This reflects the DSA210 emphasis on formulating a **clear, testable hypothesis** based on real-world phenomena:contentReference[oaicite:6]{index=6}.

---

## 📊 Data Sources
All data will be publicly available and collected through APIs or repositories:

1. **Federal Reserve (FRED)**  
   - Series: “Effective Federal Funds Rate (FEDFUNDS)”  
   - Variables: date, rate (%)  
   - Collected via `pandas_datareader`

2. **Stock Market Data (Yahoo Finance)**  
   - Indices: S&P 500 (`^GSPC`), NASDAQ (`^IXIC`), Dow Jones (`^DJI`)  
   - Variables: daily closing prices, returns  

3. **Bond Yields (FRED)**  
   - Series: “10-Year Treasury Constant Maturity Rate (DGS10)” and “2-Year Treasury Yield (DGS2)”  
   - Variables: date, yield (%)  

4. **Optional Enrichment (Macroeconomic Indicators)**  
   - Source: World Bank or OECD  
   - Variables: inflation, GDP growth (for control variables)

---

## 🧩 Data Collection Plan
- Use **Python** with `pandas_datareader` and `yfinance` to fetch datasets.  
- Merge data by **month** to align time periods.  
- Clean missing values using interpolation.  
- Normalize scales (z-score transformation) to ensure comparability:contentReference[oaicite:7]{index=7}.  
- Store processed files in a `/data` directory for reproducibility.

---

## 🔍 Analysis Plan
Following the DSA210 workflow:contentReference[oaicite:8]{index=8}:

1. **Exploratory Data Analysis (EDA):**  
   - Visualize historical trends of Fed rate vs market indices.  
   - Generate histograms, scatter plots, and rolling correlations.  
   - Identify lag effects (do markets react immediately or after a delay?).  

2. **Statistical Analysis:**  
   - Compute correlation coefficients between rate changes and market movements.  
   - Test hypotheses using Pearson correlation and t-tests.  

3. **Regression / ML (for later stages):**  
   - Build a linear regression model predicting market returns using:  
     - Federal Funds Rate  
     - Bond yields  
     - Inflation (optional control variable)  
   - Evaluate model performance with R² and residual plots.

4. **Visualization:**  
   - Use `matplotlib`, `seaborn`, and `altair` for publication-quality figures.  
   - Apply color encoding and normalization principles taught in class:contentReference[oaicite:9]{index=9}.  

---

## 💡 Expected Findings
- Stock indices negatively correlate with rate increases.  
- Bond yields move in the same direction as rates.  
- Financial sector may show moderate resilience.  
- Stronger reactions during periods of rapid tightening (e.g., 2022–2023).  

---

## ⚙️ Tools and Libraries
