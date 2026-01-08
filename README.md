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

The real estate market is a critical component of the economy, and understanding the factors that influence house prices is of great interest to buyers, sellers, and real estate professionals. This project aims to analyze the relationship between a house's physical attributes and its market value. By analyzing a comprehensive dataset of residential properties, we can build a predictive model that not only estimates sale prices but also provides insight into which features are most impactful. The primary motivation is to answer a common question for homeowners and potential buyers: which home feature or features provide the most value?

---

## 3. Research Question

### Do the number of bedrooms and bathrooms have a statistically significant effect on house prices?

From this, I will test the following hypotheses:

**Null Hypothesis (H₀):**  
The number of bedrooms/bathrooms has no meaningful relationship with house price (correlation ≈ 0).

**Alternative Hypothesis (H₁):**  
The number of bedrooms/bathrooms does have a meaningful relationship with house price (correlation ≠ 0).

This question will be explored through exploratory data analysis, and the development of a machine learning model to quantify the relationships.

---


## 4. Data Source

The dataset used for this project is the **Ames Housing dataset**, which describes the sale of individual residential property in Ames, Iowa from 2006 to 2010. It is a well-known dataset in the data science community and is often used for regression tasks.

-   **Source:** [Kaggle - House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
-   **Local Path:** `data/housing.csv`
-   **Content:** 1,460 observations and 81 features, including 23 nominal, 23 ordinal, 14 discrete, and 20 continuous variables.

---

## 5. Data Collection Plan

1. Download the dataset directly from Kaggle as a CSV file.  
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

The project will follow the standard data science pipeline:

1.  **Data Cleaning and Preparation:** The raw dataset will be loaded, inspected for missing values and outliers, and cleaned. New features, such as `TotalBath`, will be engineered to better capture the data's underlying patterns.
2.  **Exploratory Data Analysis (EDA):** I will use descriptive statistics and visualizations (scatter plots, histograms, heatmaps) to explore the relationships between variables, particularly how `BedroomAbvGr` and the newly created `TotalBath` correlate with `SalePrice`.
3.  **Hypothesis Testing:** A formal statistical test (such as a t-test or ANOVA) will be conducted to determine if the observed differences in house prices across different numbers of bedrooms and bathrooms are statistically significant.
4.  **Machine Learning Modeling:** A multiple linear regression model will be trained to predict `SalePrice` based on the number of bedrooms, bathrooms, and other relevant features. The model's performance will be evaluated using metrics like R-squared and Mean Squared Error.


## 7. Expected Outcomes

I expect to find that:

- Houses with more bathrooms tend to have significantly higher prices  
- Bedrooms may have a weaker relationship than bathrooms  
- Square footage may be a major confounder (optional to include)  
- Regression will likely show a positive coefficient for both predictors  

It is also possible that the effect of bedrooms alone is small or nonlinear, which is valuable insight for the project.

