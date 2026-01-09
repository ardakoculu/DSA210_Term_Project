# DSA210 Term Project  
# House Price Prediction

---

## 1. Project Proposal

This project explores how various characteristics of a house influence its market price.
House prices are affected by many factors, and this study aims to understand how a combination of structural features and market conditions contributes to housing value.

Using real housing datasets, I analyze the relationship between multiple house features (such as bedrooms, bathrooms, living area size, condition, grade, and location-related attributes) and sale prices to determine which factors significantly influence market value. In addition, a regional housing price index is incorporated to account for broader housing market trends over time that may affect individual house prices.

The project uses the tools learned in DSA210 to perform exploratory data analysis (EDA), correlation analysis, hypothesis testing, and regression-based modeling for house price prediction.

---

## 2. Motivation

The real estate market is a critical component of the economy, and understanding the factors that influence house prices is of great interest to buyers, sellers, and real estate professionals. This project aims to analyze the relationship between a house's physical attributes and its market value. By analyzing a comprehensive dataset of residential properties, we can build a predictive model that not only estimates sale prices but also provides insight into which features are most impactful. The primary motivation is to answer a common question for homeowners and potential buyers: which home feature or features provide the most value?

---

## 3. Research Question

### Do house-specific characteristics and regional housing market trends have a statistically significant effect on house prices in King County, Washington?

From this, I will test the following hypotheses:

**Null Hypothesis (H₀):**  
House-specific features and regional housing market trends have no meaningful relationship with house prices in King County, Washington (correlation ≈ 0).

**Alternative Hypothesis (H₁):**  
House-specific features and regional housing market trends have a meaningful relationship with house prices in King County, Washington (correlation ≠ 0).

This question will be explored through exploratory data analysis, correlation analysis, hypothesis testing, and the development of regression-based and machine learning models to quantify these relationships.

---


## 4. Data Source

This project uses two datasets: a micro-level dataset of house sales in King County, Washington, and a macro-level dataset containing a regional housing price index to capture market trends over time.

### 4.1 Primary Dataset: King County House Sales (Washington)

This dataset contains individual residential house sale records in King County (Seattle metropolitan area), along with detailed property characteristics.

-   **Source:** [Kaggle - House Sales in King County, USA](https://www.kaggle.com/datasets/arathipraj/house-data)
-   **Local Path:** `data/house_data.csv`
-   **Content:** 21,613 observations and 21 features, including sale price, number of bedrooms and bathrooms, living area size, lot size, condition, grade, and location-related variables.
  
Time Period : May 2014 – May 2015

### 4.2 Supplementary Dataset: Seattle Housing Price Index (SEXRSA)

**Source:** [Federal Reserve Economic Data (FRED) - SEXRSA](https://fred.stlouisfed.org/series/SEXRSA )

- **Official Provider:** S&P Dow Jones Indices LLC
- **Index Name:** S&P/Case-Shiller WA-Seattle Home Price Index
- **Data Type:** Seasonally Adjusted (SA) Monthly Index
- **Base Period:** January 2000 = 100
- **Time Coverage:** January 1990 to Present
- **Frequency:** Monthly observations
- **Purpose:** Measures average change in residential real estate values in Seattle metropolitan area


---

## 3. Methodology

This project follows a standard data science workflow for predictive modeling:

1.  **Data Loading and Exploration:** Load the King County house sales dataset and examine its structure, distributions, and relationships.
2.  **Data Cleaning and Preprocessing:** Handle missing values, correct data types, and identify outliers.
3.  **Feature Engineering:** Create new features and transform existing ones to improve model performance.
4.  **Exploratory Data Analysis (EDA):** Visualize distributions and correlations to understand the data better.
5.  **Hypothesis Testing:** Conduct statistical tests to validate assumptions about key features.
6.  **Model Development:** Build and train multiple machine learning models (Linear Regression, Random Forest, Gradient Boosting).
7.  **Model Evaluation:** Evaluate models using appropriate metrics (R², RMSE, MAE) and select the best performer.
8.  **Feature Importance Analysis:** Identify which features contribute most to predictions.
9.  **Macro-Economic Integration:** Incorporate regional housing market index data to enhance model context and interpretability.

---

## 5. Data Collection Plan

1. Download both datasets directly from Kaggle as CSV files. 
2. Load the dataset into a Pandas DataFrame.  
3. Clean and preprocess the data by:
   - handling missing or invalid values,
   - correcting types (e.g., parsing dates, converting price to numeric),
   - filtering unrealistic datao r extreme outliers when necessary. (e.g., 0 bedrooms but high
   price).
4. Prepare the analysis dataset by:
   - selecting relevant house-level features and defining price as the target variable, 
   - aligning house sale dates with the Seattle regional housing price index, 
   - merging the regional index into the house-level dataset to account for market trends.
5. Save the cleaned and processed dataset in a `/data` folder for EDA, hypothesis testing and modeling.

---

## 6. Methodology

The project will follow the standard data science pipeline:

1.  **Data Cleaning and Preparation:** The raw dataset will be loaded, inspected for missing values and outliers, and cleaned. New features, such as `TotalBath`, will be engineered to better capture the data's underlying patterns.
2.  **Exploratory Data Analysis (EDA):** I will use descriptive statistics and visualizations (scatter plots, histograms, heatmaps) to explore the relationships between variables, particularly how `BedroomAbvGr` and the newly created `TotalBath` correlate with `SalePrice`.
3.  **Hypothesis Testing:** A formal statistical test (such as a t-test or ANOVA) will be conducted to determine if the observed differences in house prices across different numbers of bedrooms and bathrooms are statistically significant.
4.  **Machine Learning Modeling:** A multiple linear regression model will be trained to predict `SalePrice` based on the number of bedrooms, bathrooms, and other relevant features. The model's performance will be evaluated using metrics like R-squared and Mean Squared Error.

