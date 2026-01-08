# DSA210 Term Project  
## House Price Prediction
## Do the Number of Bedrooms and Bathrooms Affect House Prices?

---

## 1. Project Proposal

This project explores whether the number of bedrooms and bathrooms in a house has a measurable effect on its market price.  
Housing markets are influenced by many factors, but one of the most common and intuitive questions is whether having more rooms actually increases the value of a home, and by how much.

Using real housing datasets, I will analyze the relationship between house features (bedrooms, bathrooms, living area size) and sale prices to determine whether these features significantly influence market value.  
The project will use the tools learned in DSA210 to perform exploratory data analysis (EDA), correlation analysis, and simple regression modeling.

---

## 2. Motivation

Housing is one of the largest financial markets in the world, and house-pricing models are widely used by banks, real-estate companies, and homeowners.  
Understanding how different home attributes affect price helps us see which housing features matter most.

This project will allow me to:

- explore a rich real-world dataset,
- run meaningful statistical tests,
- apply EDA and visualization techniques from class,
- and build an interpretable model.

It is also a topic that is simple enough to complete but rich enough to generate interesting insights.

---

## 3. Research Question

### Does the number of bedrooms and bathrooms have a statistically significant effect on house prices?

From this, I will test the following hypotheses:

**Null Hypothesis (H₀):**  
The number of bedrooms/bathrooms has no meaningful relationship with house price (correlation ≈ 0).

**Alternative Hypothesis (H₁):**  
The number of bedrooms/bathrooms does have a meaningful relationship with house price (correlation ≠ 0).

---

## 4. Data to Be Used

I will use publicly available housing datasets, such as:

| Source | Description |
|--------|-------------|
| **Kaggle – Housing Data (Ames Housing / King County House Prices)** | Contains house price, bedrooms, bathrooms, living area, lot area, etc. |
| **UCI Machine Learning Repository** | Real estate attributes and sale prices |
| **Open MLS / public county records** | Additional datasets if needed |

These datasets include the exact variables needed:

- price  
- bedrooms  
- bathrooms  
- sqft_living (optional)  
- sqft_lot (optional)

Most are already formatted as CSV files, making them easy to load and clean.

---

## 5. Data Collection Plan

1. Download the dataset directly from Kaggle or UCI as a CSV file.  
2. Load the dataset into a Pandas DataFrame.  
3. Clean the data by:
   - removing missing or invalid values,
   - correcting types (e.g., converting price to numeric),
   - filtering unrealistic data (e.g., 0 bedrooms but high price).  
4. Select the variables relevant to the research question:
   - price  
   - bedrooms  
   - bathrooms  
5. Save the cleaned dataset in a `/data` folder for EDA and modeling.

---

## 6. Methodology

I will follow the data science workflow introduced in class:

### Step 1 — Exploratory Data Analysis (EDA)

- Summary statistics (mean, median, ranges)
- Distribution of prices, bedrooms, bathrooms
- Scatter plots (price vs bedrooms, price vs bathrooms)
- Correlation heatmap
- Boxplots to compare price differences across bedroom counts

### Step 2 — Statistical Testing

- Test whether the relationship between bedrooms/bathrooms and price is statistically significant
- Perform correlation tests
- Connect the results to the H₀ / H₁ hypotheses

### Step 3 — Simple Regression Modeling

- Build a linear regression model predicting **price** from:
  - bedrooms
  - bathrooms
  - (optional) sqft_living  
- Interpret coefficients to see how much each feature affects price

### Step 4 — Visualization

- Clean line plots, scatter plots, and heatmaps
- Interpret the visual patterns
- Make conclusions based on visual + statistical evidence

---

## 7. Expected Outcomes

I expect to find that:

- Houses with more bathrooms tend to have significantly higher prices  
- Bedrooms may have a weaker relationship than bathrooms  
- Square footage may be a major confounder (optional to include)  
- Regression will likely show a positive coefficient for both predictors  

It is also possible that the effect of bedrooms alone is small or nonlinear, which is valuable insight for the project.

