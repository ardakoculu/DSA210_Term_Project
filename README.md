# DSA210_Term_Project
Sabancı University DSA210 Fall 2025 Project
# The Impact of U.S. Federal Reserve Policy Rate Changes on Financial Markets and Economic Indicators

---

## 📘 Project Overview
This project investigates how **changes in the U.S. Federal Reserve’s policy rate (Federal Funds Rate)** influence the broader financial ecosystem, including **bond yields, stock market performance, and macroeconomic indicators** such as inflation and GDP growth.  

By integrating high-quality data from **reliable global institutions** such as the **Federal Reserve**, **OECD**, and **World Bank**, this study will examine how monetary policy decisions impact financial and economic stability.  
The project demonstrates the full **data science pipeline** — from data collection and cleaning to exploratory analysis, statistical testing, and visualization — as outlined in the DSA210 lectures.

---

## 🧠 Research Motivation & Hypothesis
Changes in the Federal Funds Rate have cascading effects across the economy. A rate increase tends to slow borrowing and investment, while a rate cut stimulates spending and risk-taking.  

**Research Question:**  
> How do changes in the Federal Reserve’s policy rates affect key U.S. financial and macroeconomic indicators over time?

**Hypothesis:**  
> Increases in the Federal Funds Rate are negatively correlated with stock market performance and GDP growth but positively correlated with bond yields and inflation control effectiveness.

This aligns with DSA210’s emphasis on defining a **clear, testable hypothesis** supported by real-world data.

---

## 📊 Data Sources
All datasets will be obtained from **public, authoritative economic databases** to ensure accuracy and reproducibility:

1. **Federal Reserve Economic Data (FRED)**  
   - Series: *Effective Federal Funds Rate (FEDFUNDS)*  
   - Frequency: Monthly  
   - Variables: date, interest rate (%)  
   - Source: [https://fred.stlouisfed.org](https://fred.stlouisfed.org)

2. **OECD Economic Outlook Database**  
   - Variables: GDP growth rate, inflation rate, unemployment rate  
   - Frequency: Quarterly  
   - Source: [https://data.oecd.org](https://data.oecd.org)

3. **World Bank Global Financial Development Database**  
   - Variables: stock market capitalization (% of GDP), credit to private sector, investment ratio  
   - Frequency: Annual  
   - Source: [https://databank.worldbank.org](https://databank.worldbank.org)

4. **IMF International Financial Statistics (optional enrichment)**  
   - Variables: government bond yields, financial sector indicators  
   - Source: [https://data.imf.org](https://data.imf.org)

---

## 🧩 Data Collection Plan
- Retrieve datasets via **official APIs or CSV exports** from FRED, OECD, and World Bank platforms.  
- Standardize temporal granularity (monthly or quarterly).  
- Clean and normalize numerical columns using z-score transformation.  
- Merge datasets on date or year fields to build a unified macro-financial dataset.  
- Store cleaned data in `/data/` directory for reproducibility.

---

## 🔍 Analysis Plan
1. **Exploratory Data Analysis (EDA):**  
   - Visualize historical trends of policy rates, GDP growth, and inflation.  
   - Compute rolling correlations between the Fed rate and financial indicators.  
   - Identify key periods of rate tightening or easing and their effects.

2. **Statistical & Correlation Analysis:**  
   - Test relationships between the policy rate and economic/financial indicators using correlation coefficients and hypothesis testing.  
   - Hypotheses:  
     - H₀: Fed rate changes have no significant impact on financial indicators.  
     - H₁: Fed rate changes significantly influence financial and macroeconomic performance.

3. **Regression & Prediction (later phase):**  
   - Build a **multiple linear regression** model to predict GDP growth and inflation using:  
     - Federal Funds Rate  
     - Bond yields  
     - Investment/GDP ratio  
   - Evaluate model performance via R², RMSE, and cross-validation.

4. **Visualization:**  
   - Use `matplotlib`, `seaborn`, and `altair` to create clear, policy-level visualizations (e.g., rate vs inflation plots, correlation heatmaps).  
   - Apply visualization best practices taught in DSA210 Week 2 (color scaling, minimalism, clarity).  

---

## 💡 Expected Findings
- A **negative correlation** between interest rate hikes and stock market or investment growth.  
- A **positive correlation** between interest rate hikes and bond yields.  
- Clear lag effects — rate changes influencing GDP and inflation with a delay.  
- Insight into how effective monetary policy decisions are in stabilizing inflation without overly suppressing growth.

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
- Some macroeconomic data (e.g., quarterly GDP) may limit short-term correlation precision.  
- External factors (pandemics, wars, fiscal policy changes) could bias results.  
- Future extensions may include **time-series forecasting (ARIMA)** or **policy-effect simulations** using ML models.

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
| Proposal Submission | 31 Oct | GitHub repo & README |
| Data Collection & EDA | 28 Nov | Collect, clean & visualize OECD, FRED, and World Bank data |
| ML Application | 2 Jan | Apply regression/ML models |
| Final Submission | 9 Jan | Submit full analysis and report |

---

## ✍️ Ethical Considerations
All datasets are obtained from **public, institutional sources** (FRED, OECD, World Bank, IMF) that comply with open-data and ethical research standards.  
AI tools (e.g., ChatGPT) were used solely for documentation structuring and will be disclosed in the final report, as required by the DSA210 integrity policy.

---

**End of Proposal**
