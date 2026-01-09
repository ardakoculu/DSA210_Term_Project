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

---

## Expected Outcomes

### 1. Statistical Validation
The project successfully validates that **house-specific characteristics have statistically significant effects on house prices** in King County. Through comprehensive hypothesis testing, we confirmed:
- All 9 continuous features show significant correlations (p < 0.05)
- All 7 categorical features show significant effects (p < 0.05)
- Regional market trends (Seattle HPI) do NOT significantly affect individual prices

### 2. Predictive Model Performance
The Gradient Boosting model achieves strong predictive performance suitable for real-world applications:
- **R² = 0.7177** - Explains 71.77% of house price variance
- **RMSE = $206,589** - Typical prediction error
- **MAE = $127,474** - Average absolute error (12% of mean price)
- **MAPE = 8.98%** - Percentage error

This level of accuracy is appropriate for:
- Fair market value estimation
- Identifying overpriced/underpriced properties
- Supporting real estate investment decisions
- Informing property valuation models

### 3. Feature Importance Insights
Clear identification of price drivers:
- **Living space (sqft_living)** is the dominant factor
- **Construction quality (grade)** is the second most important
- **Location and condition** significantly influence pricing
- **Bedroom/bathroom counts** have moderate effects

### 4. Market Understanding
Practical insights about King County real estate:
- Property characteristics dominate pricing decisions
- Regional market indices have limited direct predictive power
- Waterfront and premium neighborhoods command significant premiums
- Quality and size are the primary value drivers

---

## Future Work

### 1. Enhanced Feature Engineering
**Objective:** Improve model performance by incorporating additional features

**Proposed Enhancements:**
- **Neighborhood-level features:** Schools quality ratings, crime rates, amenities proximity
- **Temporal features:** Seasonal effects, market cycle indicators, time-on-market
- **Interaction features:** sqft_living × grade, waterfront × location, condition × age
- **Engineered metrics:** Price per square foot, property age, renovation status
- **Geographic features:** Distance to downtown Seattle, proximity to transit, walkability scores

**Expected Impact:** R² could improve to 0.75-0.80 with neighborhood-level data

### 2. Advanced Modeling Techniques
**Objective:** Explore more sophisticated algorithms

**Proposed Models:**
- **XGBoost & LightGBM:** More advanced gradient boosting variants
- **Neural Networks:** Deep learning for complex non-linear relationships
- **Ensemble Methods:** Voting classifiers combining multiple models
- **Bayesian Methods:** Uncertainty quantification in predictions
- **Time Series Models:** ARIMA for temporal trend analysis

**Expected Impact:** Potential 2-5% improvement in R² score

### 3. Location-Specific Sub-Models
**Objective:** Develop specialized models for different neighborhoods

**Proposed Approach:**
- Cluster King County into geographic regions (Seattle, Bellevue, Redmond, etc.)
- Train separate models for each region
- Account for neighborhood-specific price drivers
- Improve predictions for premium vs. standard neighborhoods

**Expected Impact:** Better predictions for location-sensitive pricing

### 4. Temporal Analysis
**Objective:** Understand how prices change over time

**Proposed Analysis:**
- Analyze seasonal patterns in house sales
- Identify market cycles and trends
- Study how economic conditions affect prices
- Incorporate interest rate and unemployment data
- Develop time-series forecasting models

**Expected Impact:** Better understanding of market dynamics

### 5. External Economic Integration
**Objective:** Incorporate macroeconomic indicators

**Proposed Data Sources:**
- **Interest rates:** Federal Reserve data on mortgage rates
- **Unemployment:** Local unemployment rates
- **GDP growth:** Regional economic growth indicators
- **Housing starts:** New construction data
- **Inventory levels:** Market supply indicators

**Expected Impact:** Better context for market trends

### 6. Real Estate Professional Tools
**Objective:** Develop practical applications for real estate industry

**Proposed Tools:**
- **Automated Valuation Model (AVM):** Web interface for price estimation
- **Market Analysis Dashboard:** Interactive visualization of price trends
- **Investment Analysis Tool:** Identify undervalued properties
- **Comparative Market Analysis (CMA):** Automated property comparisons
- **Price Prediction API:** REST API for integration with real estate platforms

**Expected Impact:** Practical applications for industry professionals

### 7. Model Validation and Testing
**Objective:** Ensure model reliability and generalization

**Proposed Validation:**
- **Out-of-sample testing:** Validate on data from different time periods
- **Cross-validation:** Rigorous 10-fold cross-validation
- **Sensitivity analysis:** Test model robustness to parameter changes
- **Stress testing:** Evaluate performance under extreme conditions
- **Backtesting:** Test predictions on historical data

**Expected Impact:** Increased confidence in model reliability

### 8. Data Expansion
**Objective:** Improve model with more comprehensive data

**Proposed Data:**
- **Longer time period:** Extend beyond May 2014 - May 2015
- **More regions:** Include other Washington counties or states
- **Property details:** HOA fees, property taxes, utilities
- **Market data:** Comparable sales, market absorption rates
- **Demographic data:** Population density, income levels, education

**Expected Impact:** More robust and generalizable models

### 9. Interpretability Improvements
**Objective:** Better understand model decisions

**Proposed Methods:**
- **SHAP values:** Explain individual predictions
- **LIME:** Local interpretable model-agnostic explanations
- **Partial dependence plots:** Show feature effects
- **Accumulated local effects:** Alternative to partial dependence
- **Feature interaction analysis:** Understand feature combinations

**Expected Impact:** Better stakeholder understanding

### 10. Deployment and Monitoring
**Objective:** Move model to production environment

**Proposed Implementation:**
- **Model serving:** Deploy via REST API or web service
- **Performance monitoring:** Track prediction accuracy over time
- **Data drift detection:** Identify when model needs retraining
- **Automated retraining:** Periodic model updates with new data
- **A/B testing:** Compare model versions in production

**Expected Impact:** Continuous improvement and reliability


## Conclusion

This project successfully demonstrates that **machine learning can effectively predict house prices** in King County using property-specific characteristics. The Gradient Boosting model achieves reliable predictions (R² = 0.7177) suitable for real estate valuation and market analysis.

The identified future work provides a clear roadmap for enhancing model performance, expanding functionality, and developing practical applications for real estate professionals. By incorporating neighborhood-level features, advanced modeling techniques, and external economic indicators, the model can achieve even higher accuracy and provide more comprehensive market insights.

The project establishes a solid foundation for ongoing research and development in real estate price prediction and market analysis.

---

