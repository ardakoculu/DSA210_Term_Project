# DSA210_Term_Project
# DSA210_Term_Project
# The Impact of U.S. Federal Reserve Policy Rates on Borrowing Costs

## Project Proposal
In this project, I want to understand how **changes in the U.S. Federal Reserve’s policy rate (Federal Funds Rate)** show up in **borrowing costs** in the real world.  
More specifically, I will look at whether higher Fed policy rates are reflected in:

- **mortgage rates**, and  
- **corporate bond yields** (the cost of borrowing for firms).

The main goal is to see if there is a clear and measurable pass-through from the policy rate to these borrowing costs.  
Using data science techniques such as exploratory data analysis and basic statistical tests, I will try to quantify how strongly and how consistently mortgage rates and corporate bond yields move when the Fed changes its policy rate.

---

## Motivation
We constantly hear things like “The Fed hiked rates by 25 basis points” and then people say “borrowing will get more expensive.”  
But how directly and how quickly does this actually show up in things like:

- the rate on a typical U.S. mortgage, or  
- the yield that companies have to pay to issue bonds?

As someone interested in finance, I want to connect the **policy side** (Fed decisions) with the **market side** (borrowing costs faced by households and firms) using real data.  
This project is a way to take an idea we see in the news and test it with actual numbers from official sources, using the tools I’m learning in DSA210.

---

## Research Question
I will focus on one main research question:

> **Do higher Fed policy rates lead to increases in borrowing costs, such as mortgage rates or corporate bond yields?**

From this, a simple hypothesis pair I can test is:

- **H₀ (null):** Changes in the Federal Funds Rate are **not** associated with changes in mortgage rates or corporate bond yields (no meaningful relationship; correlation ≈ 0).  
- **H₁ (alternative):** Changes in the Federal Funds Rate **are** associated with changes in mortgage rates and/or corporate bond yields (there is a meaningful relationship, and ideally a positive one).

---

## Data to Be Used
All data will come from public, institutional sources:

| Source | Description | Frequency |
|--------|-------------|-----------|
| **Federal Reserve Economic Data (FRED)** | Effective Federal Funds Rate, mortgage rates (e.g. 30-year fixed mortgage rate), corporate bond yields (e.g. corporate bond indices or spreads) | Monthly |
| **OECD Data Portal** | U.S. financial and credit market indicators that can provide context (credit volumes, lending conditions) | Quarterly |
| **World Bank – Global Financial Development Database** | Broader financial indicators such as domestic credit to private sector and financial depth ratios (used mainly for background and robustness checks) | Annual |
| **IMF – International Financial Statistics (optional)** | Additional data on U.S. interest rates or bond yields, if needed | Monthly |

The core of the analysis will rely on **Fed Funds Rate + mortgage rates + corporate bond yields**. The other sources are there mainly to add context if necessary.

---

## Data Collection Plan
I’ll collect the datasets directly from each institution’s website (FRED, OECD, World Bank, and IMF) and download them in CSV or Excel format.  
Then I’ll put everything on a common timeline (most likely monthly) so dates match across sources, especially between the Fed Funds Rate and the borrowing cost series (mortgage and corporate bond yields).  

If there are missing values, I’ll handle them by filling them in or carrying the previous value forward, depending on what makes sense for that variable.  
After that, I’ll select the variables that are most relevant for this project — mainly:

- the policy rate,  
- one or more mortgage rate series,  
- one or more corporate bond yield series,  
- plus a few simple context variables if needed.

I’ll merge these into a single dataset keyed by date.  
Finally, I’ll save the cleaned version in a `/data` folder to use later for analysis and visualizations.

---

## Methodology (How I Plan to Analyze the Data)
I’ll follow the general data science workflow we saw in class:

1. **Exploratory Data Analysis (EDA)**  
   - Plot the Fed Funds Rate, mortgage rates, and corporate bond yields over time.  
   - Put them on the same timeline and visually check whether borrowing costs tend to move up when the policy rate increases.  
   - Look at basic summary statistics and distributions to understand the range and behavior of each variable.

2. **Correlation and Simple Statistical Tests**  
   - Calculate correlations between the Fed Funds Rate and:  
     - mortgage rates,  
     - corporate bond yields.  
   - Test whether these correlations are statistically different from zero, linking directly to the H₀ / H₁ above.

3. **Basic Modeling**  
   - Try a simple regression model where the **target** is a borrowing cost (for example, a mortgage rate or a corporate bond yield) and the **main input** is the Fed Funds Rate (possibly including lagged values to capture delayed effects).  
   - Check how much of the variation in borrowing costs can be explained by changes in the policy rate.

4. **Visualization and Interpretation**  
   - Use clear plots (line charts, scatter plots, and maybe a small correlation heatmap) to show how the variables move together.  
   - Try to connect major rate-hike or rate-cut episodes to visible changes in borrowing costs and discuss whether the data supports the idea of pass-through from the policy rate to real-world borrowing rates.

---

## Expected Outcomes
At this stage, I expect to see:

- a **positive relationship** between the Federal Funds Rate and mortgage rates,  
- a **positive relationship** between the Federal Funds Rate and corporate bond yields,  
- and possibly some **lag** between a change in the Fed rate and the adjustment in borrowing costs.

It’s also possible that the relationship is weaker or noisier than expected, especially in shorter time periods or during times when other factors (like market stress, expectations, or risk sentiment) dominate.  
Even in that case, the result will still be informative, because it will show that the link between policy rates and real-world borrowing costs is not always one-to-one and may depend on broader financial conditions.

---

