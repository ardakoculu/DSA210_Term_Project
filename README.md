# DSA210_Term_Project
Sabancı University DSA210 Fall 2025 Project
# The Impact of U.S. Federal Reserve Policy Rate Changes on Financial Markets

---

## 📘 Project Overview
This project investigates how **changes in the U.S. Federal Reserve’s policy rate (Federal Funds Rate)** affect the structure and performance of financial markets — particularly **bond yields, stock indices, and credit indicators**.  

Using reliable data from institutions such as the **Federal Reserve**, **OECD**, and **World Bank**, the study explores how monetary tightening and easing influence investment behavior and market responses.  
It follows the **data science pipeline** taught in DSA210 — from data collection and cleaning to exploratory analysis, hypothesis testing, and visualization.

---

## 🧠 Research Motivation & Hypothesis
The Federal Funds Rate is one of the most influential tools in global finance.  
When the Fed raises rates, borrowing costs rise, investor risk appetite falls, and bond yields typically increase.  
Conversely, when the Fed lowers rates, capital becomes cheaper, encouraging borrowing and market expansion.  

**Research Question:**  
> How do changes in the Federal Reserve’s policy rates influence key U.S. financial indicators such as bond yields and market indices?

**Hypothesis:**  
> Increases in the Federal Funds Rate are negatively correlated with stock market performance and positively correlated with bond yields and credit tightening.

---

## 📊 Data Sources
All data will be drawn from **authoritative institutional databases** to ensure reliability and replicability:

1. **Federal Reserve Economic Data (FRED)**  
   - Series: *Effective Federal Funds Rate (FEDFUNDS)*  
   - Frequency: Monthly  
   - Variables: date, interest rate (%)  
   - Source: [https://fred.stlouisfed.org](https://fred.stlouisfed.org)

2. **OECD Economic Outlook Database**  
   - Variables: financial market indicators, credit volumes, investment ratios  
   - Frequency: Quarterly  
   - Source: [https://data.oecd.org](https://data.oecd.org)

3. **World Bank Global Financial Development Database**  
   - Variables: stock market capitalization, domestic credit to private sector, financial depth ratios  
   - Frequency: Annual  
   - Source: [https://databank.worldbank.org](https://databank.worldbank.org)

4. **IMF International Financial Statistics (optional)**  
   - Variables: government bond yields, short-term interest rates  
   - Source: [https://data.imf.org](https://data.imf.org)

---

## 🧩 Data Collection Plan
- Collect datasets via **official APIs or direct CSV downloads** from FRED, OECD, and World Bank sources.  
- Unify data on a **monthly or quarterly** basis.  
- Handle missing or inconsistent data using interpolation and normalization.  
- Store processed data within `/data` for transparent reproducibility.  

---

## 🔍 Analysis Plan
1. **Exploratory Data Analysis (EDA):**  
   - Plot long-term trends of the Fed Funds Rate alongside stock indices and bond yields.  
   - Identify relationships and shifts during rate hike or cut periods.  
   - Compute correlation matrices between financial indicators and interest rate levels.

2. **Statistical Testing:**  
   - Examine whether rate movements have statistically significant effects on financial market variables.  
   - Hypotheses:  
     - H₀: Federal rate changes do not significantly affect financial markets.  
     - H₁: Federal rate changes significantly influence financial market behavior.

3. **Regression & Predictive Modeling (for final phase):**  
   - Build a **multiple linear regression** model predicting financial indicator movement using:  
     - Federal Funds Rate  
     - Bond yield differentials  
     - Credit indicators (e.g., private sector credit share)  
   - Evaluate model fit using R² and residual analysis.

4. **Visualization:**  
   - Create visual summaries of rate–market relationships with `matplotlib`, `seaborn`, and `altair`.  
   - Use clear labeling and color scaling consistent with DSA210’s visualization best practices.

---

## 💡 Expected Findings
- **Negative correlation** between rate hikes and stock market indicators.  
- **Positive correlation** between policy rate increases and bond yields.  
- Periods of rapid tightening likely show stronger market reactions.  
- Observable lag effects where financial responses follow rate decisions by several months.

---

## ⚙️ Tools and Libraries
```
pandas
numpy
matplotlib
seaborn
altair
scikit-learn
pandas_datareader
```

---

## ⚠️ Limitations & Future Work
- Financial markets are influenced by multiple concurrent factors (policy announcements, geopolitical risks, global liquidity).  
- Data granularity may limit real-time interpretation of rapid rate changes.  
- Future research could integrate **time-series forecasting (ARIMA)** or **policy event detection** for improved predictive insight.

---

## 📁 Repository Structure
```
DSA210_Project_ArdaKoculu/
│
├── data/                # Collected & cleaned datasets
├── notebooks/           # Jupyter notebooks for EDA & ML
├── README.md            # Project description (this file)
└── requirements.txt     # Python dependencies
```

---

## 📅 Timeline
| Phase | Deadline | Task |
|-------|-----------|------|
| Proposal Submission | 31 Oct | Create GitHub repo & README |
| Data Collection & EDA | 28 Nov | Collect and visualize FRED, OECD, and World Bank data |
| ML Application | 2 Jan | Apply regression/ML models |
| Final Submission | 9 Jan | Submit full analysis and presentation |

---

## ✍️ Ethical Considerations
All datasets are sourced from **public, open-data institutions** (FRED, OECD, World Bank, IMF).  
AI tools (e.g., ChatGPT) were used solely for documentation drafting and project structuring, as disclosed under DSA210 academic integrity guidelines.

---

**End of Proposal**
