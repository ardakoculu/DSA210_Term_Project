# DSA210_Term_Project
# The Impact of U.S. Federal Reserve Policy Rate Changes on Financial Markets

## Project Proposal
This project aims to analyze how **changes in the U.S. Federal Reserve’s policy rate (Federal Funds Rate)** influence major **financial market indicators** such as bond yields, stock market indices, and credit-related variables.  

The purpose is to identify whether monetary tightening (rate hikes) and easing (rate cuts) produce measurable patterns in financial markets.  
By applying data science techniques, including exploratory data analysis and correlation testing, the project will determine the strength and direction of relationships between policy rates and financial variables over time.

---

## Motivation
The Federal Funds Rate is one of the most influential policy tools in the world.  
When the rate changes, financial markets react. Bond yields shift, stock indices adjust, and credit conditions tighten or loosen.
As a finance enthusiast, I’m driven to understand how these shifts actually appear in real economic data.
This project aims to understand these relationships using real financial and economic data.  
The idea is to connect what we hear in the news (“Fed raised rates by 25 bps…”) with real numbers from official sources and try to understand the link between policy decisions and market reactions using the tools I learn in DSA210.

---

## Research Questions
I plan to focus on a few main questions:
1. How much do changes in the Federal Funds Rate pass through to U.S. Treasury yields across different maturities (short-term and long-term)?
2. Do higher Fed policy rates lead to increases in borrowing costs, such as mortgage rates or corporate bond yields?
3. Do changes in the Federal Funds Rate have a measurable effect on stock-market performance across major U.S. indices, such as the S&P 500, NASDAQ, and Russell 2000?

From these questions, one simple statistical hypothesis pair I can test is:

- **H₀ (null):** Changes in the Federal Funds Rate are not associated with changes in the financial indicators (no meaningful relationship; correlation ≈ 0).  
- **H₁ (alternative):** Changes in the Federal Funds Rate are associated with changes in the financial indicators (there **is** a meaningful relationship).

---

## Data to Be Used
All data will come from public, institutional sources:

| Source | Description | Frequency |
|--------|-------------|-----------|
| **Federal Reserve Economic Data (FRED)** | Effective Federal Funds Rate, U.S. Treasury yields, mortgage rates, corporate bond yields, stock indices (S&P 500, NASDAQ 100, Russell 2000) | Monthly |
| **OECD Data Portal** | U.S. financial and credit market indicators | Quarterly |
| **World Bank – Global Financial Development Database** | Market capitalization, domestic credit to private sector, financial depth ratios | Annual |
| **IMF – International Financial Statistic** | U.S. government bond yields and short-term interest rates | Monthly |

---

## Data Collection Plan
I’ll collect the datasets directly from each institution’s website (FRED, OECD, World Bank, and IMF) and download them in CSV or Excel format.  
Then I’ll put everything on a common timeline (most likely monthly or quarterly) so the dates match across sources.  
If there are missing values, I’ll deal with them by filling them in or carrying the previous value forward, depending on what makes sense for that variable.  
After that, I’ll select the variables that are most relevant for the project, mainly the policy rate, bond yields, and financial/credit indicators (plus a few macro variables if needed) and merge them into a single dataset.  
Finally, I’ll save the cleaned version in a `/data` folder to use for analysis and visualizations later.

---

## Methodology (How I Plan to Analyze the Data)
At a high level, I plan to follow the data science workflow we saw in class:

1. **Exploratory Data Analysis (EDA)**  
   - Plot the Fed Funds Rate over time.  
   - Plot bond yields and financial indicators over time.  
   - Put them on the same timeline to get a visual feeling for whether they move together.

2. **Correlation and Simple Statistical Tests**  
   - Calculate correlations between the policy rate and each financial indicator.  
   - Check whether these correlations are statistically different from zero (this connects to the H₀ / H₁ above).  

3. **Basic Modeling**  
   - Try a simple regression model where a financial variable (for example, a bond yield) is the target and the Fed rate and maybe some other indicators are the inputs.  
   - Evaluate how well the model explains the variation in that variable.

4. **Visualization and Interpretation**  
   - Use clear plots (line charts, scatter plots, heatmaps) to summarize what I find.  
   - Try to connect the visuals to real episodes of tightening and easing (for example, recent years when the Fed raised rates quickly).

---

## Expected Outcomes
At this stage I expect:

- to see a **positive relationship** between the Federal Funds Rate and government bond yields,  
- some **negative relationship** between higher rates and stock/financial indicators (markets slowing in tightening periods),  
- and possibly a delay between the policy move and the market reaction.

It is also possible that some indicators do **not** react strongly, or that the relationship is weaker than I expect. In that case, the result is still useful, because it shows that other factors (like global events, expectations, or risk sentiment) might be more important than the raw policy rate itself.

---

