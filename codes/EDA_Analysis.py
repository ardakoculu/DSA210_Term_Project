# ================================================================================
# ExploratoryDataAnalysis(EDA).ipynb
# Extracted Python code from Jupyter notebook
# ================================================================================


# ===== CODE CELL 1 =====
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for visualizations
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Load the King County house sales data
house_data = pd.read_csv('../data/house_data.csv')
print('King County house data loaded successfully!')
print(f'Shape: {house_data.shape}')
print(f'\nDataset covers the period from May 2014 to May 2015')

# ===== CODE CELL 2 =====
# Display basic information
print('Dataset Information:')
print('='*70)
print(house_data.info())
print('\n' + '='*70)
print('First 5 rows:')
print(house_data.head())
print('\n' + '='*70)
print('Basic Statistics:')
print(house_data.describe())

# ===== CODE CELL 3 =====
# Check for missing values
print('Missing Values:')
missing = house_data.isnull().sum()
if missing.sum() > 0:
    print(missing[missing > 0])
else:
    print('No missing values found!')

# Check for duplicate rows
print(f'\nDuplicate rows: {house_data.duplicated().sum()}')

# Check data types
print('\nData Types:')
print(house_data.dtypes)

# ===== CODE CELL 4 =====
# Convert date column to datetime
house_data['date'] = pd.to_datetime(house_data['date'], format='%Y%m%dT%H%M%S')

# Extract temporal features
house_data['year'] = house_data['date'].dt.year
house_data['month'] = house_data['date'].dt.month
house_data['quarter'] = house_data['date'].dt.quarter

print('Date range:', house_data['date'].min(), 'to', house_data['date'].max())
print('\nSales by year:')
print(house_data['year'].value_counts().sort_index())
print('\nSales by month:')
print(house_data['month'].value_counts().sort_index())

# ===== CODE CELL 5 =====
# Create age of house
current_year = 2015  # Based on the dataset
house_data['house_age'] = current_year - house_data['yr_built']

# Create price per square foot
house_data['price_per_sqft'] = house_data['price'] / house_data['sqft_living']

# Create basement ratio
house_data['basement_ratio'] = house_data['sqft_basement'] / house_data['sqft_living']
house_data['basement_ratio'] = house_data['basement_ratio'].fillna(0)

# Create renovation indicator
house_data['was_renovated'] = (house_data['yr_renovated'] > 0).astype(int)

# Create lot to living ratio
house_data['lot_to_living_ratio'] = house_data['sqft_lot'] / house_data['sqft_living']

print('New features created:')
print(house_data[['house_age', 'price_per_sqft', 'basement_ratio', 'was_renovated', 'lot_to_living_ratio']].head())

# ===== CODE CELL 6 =====
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Price distribution
axes[0].hist(house_data['price'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
axes[0].set_xlabel('Price ($)')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Distribution of House Prices in King County')
axes[0].ticklabel_format(style='plain', axis='x')

# Log price distribution
axes[1].hist(np.log10(house_data['price']), bins=50, color='coral', edgecolor='black', alpha=0.7)
axes[1].set_xlabel('Log10(Price)')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Distribution of Log-Transformed Prices')

plt.tight_layout()
plt.savefig('../figures/01_price_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

print('Price Statistics:')
print(house_data['price'].describe())

# ===== CODE CELL 7 =====
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Bedrooms distribution
house_data['bedrooms'].value_counts().sort_index().plot(kind='bar', ax=axes[0, 0], color='steelblue')
axes[0, 0].set_xlabel('Number of Bedrooms')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Distribution of Bedrooms')
axes[0, 0].grid(axis='y', alpha=0.3)

# Bathrooms distribution
house_data['bathrooms'].value_counts().sort_index().head(15).plot(kind='bar', ax=axes[0, 1], color='coral')
axes[0, 1].set_xlabel('Number of Bathrooms')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Distribution of Bathrooms (Top 15)')
axes[0, 1].grid(axis='y', alpha=0.3)

# Grade distribution
house_data['grade'].value_counts().sort_index().plot(kind='bar', ax=axes[1, 0], color='green')
axes[1, 0].set_xlabel('Grade (Quality)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Distribution of House Grade')
axes[1, 0].grid(axis='y', alpha=0.3)

# Living area distribution
axes[1, 1].hist(house_data['sqft_living'], bins=50, color='purple', edgecolor='black', alpha=0.7)
axes[1, 1].set_xlabel('Square Feet')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Distribution of Living Area')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('../figures/02_key_features_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# ===== CODE CELL 8 =====
# Select numeric columns for correlation
numeric_cols = house_data.select_dtypes(include=[np.number]).columns
correlation_matrix = house_data[numeric_cols].corr()

# Create correlation heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, square=True, cbar_kws={'label': 'Correlation'})
plt.title('Correlation Matrix of House Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('../figures/03_correlation_matrix.png', dpi=300, bbox_inches='tight')
plt.show()

# Print top correlations with price
print('\nTop 10 Features Correlated with Price:')
price_corr = correlation_matrix['price'].sort_values(ascending=False)
print(price_corr.head(11))  # 11 because first is price itself

# ===== CODE CELL 9 =====
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# Price vs. Sqft_Living
sns.scatterplot(ax=axes[0], x='sqft_living', y='price', data=house_data, alpha=0.4, edgecolor=None, s=30)
axes[0].set_title('Price vs. Square Feet Living Area', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Square Feet Living')
axes[0].set_ylabel('Price (USD)')
axes[0].ticklabel_format(style='plain', axis='y')

# Price vs. Grade
sns.boxplot(ax=axes[1], x='grade', y='price', data=house_data, palette='Set2')
axes[1].set_title('Price vs. Grade', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Grade')
axes[1].set_ylabel('Price (USD)')
axes[1].ticklabel_format(style='plain', axis='y')

plt.tight_layout()
plt.show()

# ===== CODE CELL 10 =====
fig, axes = plt.subplots(2, 2, figsize=(18, 12))

# Price vs. Bedrooms
sns.boxplot(ax=axes[0, 0], x='bedrooms', y='price', data=house_data, palette='Blues')
axes[0, 0].set_title('Price vs. Number of Bedrooms', fontsize=14, fontweight='bold')
axes[0, 0].set_ylim(0, 2000000)
axes[0, 0].ticklabel_format(style='plain', axis='y')

# Price vs. Bathrooms
sns.boxplot(ax=axes[0, 1], x='bathrooms', y='price', data=house_data, palette='Greens')
axes[0, 1].set_title('Price vs. Number of Bathrooms', fontsize=14, fontweight='bold')
axes[0, 1].set_ylim(0, 2000000)
axes[0, 1].ticklabel_format(style='plain', axis='y')

# Price vs. Condition
sns.boxplot(ax=axes[1, 0], x='condition', y='price', data=house_data, palette='Oranges')
axes[1, 0].set_title('Price vs. Condition', fontsize=14, fontweight='bold')
axes[1, 0].set_ylim(0, 2000000)
axes[1, 0].ticklabel_format(style='plain', axis='y')

# Price vs. Waterfront
sns.boxplot(ax=axes[1, 1], x='waterfront', y='price', data=house_data, palette='Reds')
axes[1, 1].set_title('Price vs. Waterfront View', fontsize=14, fontweight='bold')
axes[1, 1].ticklabel_format(style='plain', axis='y')

plt.tight_layout()
plt.show()

# ===== CODE CELL 11 =====
plt.figure(figsize=(14, 12))
scatter = plt.scatter(house_data['long'], house_data['lat'], c=house_data['price'], 
                       cmap='viridis', alpha=0.6, s=20, edgecolor=None)
plt.colorbar(scatter, label='Price (USD)')
plt.title('Geospatial Distribution of House Prices in King County', fontsize=16, fontweight='bold')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()

# ===== CODE CELL 12 =====
# Save cleaned data for next notebook
house_data.to_csv('../data/house_data_cleaned.csv', index=False)
print('Cleaned data saved to house_data_cleaned.csv')
print(f'Total records: {len(house_data)}')
print(f'Total features: {len(house_data.columns)}')

# ===== CODE CELL 13 =====
# Load SEXRSA data
sexrsa_raw = pd.read_csv('SEXRSA.csv')
sexrsa_raw['observation_date'] = pd.to_datetime(sexrsa_raw['observation_date'])

print('=== ORIGINAL SEXRSA DATA ===')
print(f'Date Range: {sexrsa_raw["observation_date"].min()} to {sexrsa_raw["observation_date"].max()}')
print(f'Total Records: {len(sexrsa_raw)}')
print(f'\nFirst 5 records:')
print(sexrsa_raw.head())
print(f'\nLast 5 records:')
print(sexrsa_raw.tail())

# ===== CODE CELL 14 =====
# Extract year-month from house data to determine exact time span
house_data['date'] = pd.to_datetime(house_data['date'])
house_data['year_month'] = house_data['date'].dt.to_period('M')

min_date = house_data['date'].min()
max_date = house_data['date'].max()
min_year_month = house_data['year_month'].min()
max_year_month = house_data['year_month'].max()

print('=== HOUSE DATA TIME SPAN ===')
print(f'Minimum Date: {min_date}')
print(f'Maximum Date: {max_date}')
print(f'Year-Month Range: {min_year_month} to {max_year_month}')
print(f'Total Records: {len(house_data)}')
print(f'Unique Months: {house_data["year_month"].nunique()}')

# ===== CODE CELL 15 =====
# Create year-month column for SEXRSA
sexrsa_raw['year_month'] = sexrsa_raw['observation_date'].dt.to_period('M')

# Filter SEXRSA to match house data time span
sexrsa_filtered = sexrsa_raw[
    (sexrsa_raw['year_month'] >= min_year_month) & 
    (sexrsa_raw['year_month'] <= max_year_month)
].copy()

print('=== FILTERED SEXRSA DATA (CLEANED) ===')
print(f'Date Range: {sexrsa_filtered["observation_date"].min()} to {sexrsa_filtered["observation_date"].max()}')
print(f'Total Records: {len(sexrsa_filtered)}')
print(f'Unique Months: {sexrsa_filtered["year_month"].nunique()}')
print(f'\nFiltered SEXRSA Data:')
print(sexrsa_filtered[['observation_date', 'SEXRSA']].to_string())

# ===== CODE CELL 16 =====
print('=== SEXRSA INDEX STATISTICS (May 2014 - May 2015) ===')
print(f'Minimum Index: {sexrsa_filtered["SEXRSA"].min():.2f}')
print(f'Maximum Index: {sexrsa_filtered["SEXRSA"].max():.2f}')
print(f'Mean Index: {sexrsa_filtered["SEXRSA"].mean():.2f}')
print(f'Median Index: {sexrsa_filtered["SEXRSA"].median():.2f}')
print(f'Standard Deviation: {sexrsa_filtered["SEXRSA"].std():.2f}')

# Calculate index change
index_change = sexrsa_filtered['SEXRSA'].iloc[-1] - sexrsa_filtered['SEXRSA'].iloc[0]
pct_change = (index_change / sexrsa_filtered['SEXRSA'].iloc[0]) * 100

print(f'\nIndex Change (May 2014 to May 2015): {index_change:.2f} points')
print(f'Percentage Change: {pct_change:.2f}%')

# ===== CODE CELL 17 =====
plt.figure(figsize=(14, 7))
plt.plot(sexrsa_filtered['observation_date'], sexrsa_filtered['SEXRSA'], 
         marker='o', linewidth=2.5, markersize=8, color='#2E86AB', label='Seattle HPI')
plt.title('Seattle House Price Index Trend (May 2014 - May 2015)', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('SEXRSA Index Value', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(rotation=45)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

print(f'\nKey Insight: The Seattle HPI increased by {pct_change:.2f}% over the 13-month period.')

# ===== CODE CELL 18 =====
# Merge house data with filtered SEXRSA
merged_data = pd.merge(
    house_data, 
    sexrsa_filtered[['year_month', 'SEXRSA']], 
    on='year_month', 
    how='left'
)
merged_data.rename(columns={'SEXRSA': 'seattle_hpi'}, inplace=True)

print('=== MERGE RESULTS ===')
print(f'Total House Records: {len(house_data)}')
print(f'Total SEXRSA Records (Filtered): {len(sexrsa_filtered)}')
print(f'Merged Records: {len(merged_data)}')
print(f'Records with HPI Data: {merged_data["seattle_hpi"].notna().sum()}')
print(f'Records Missing HPI Data: {merged_data["seattle_hpi"].isna().sum()}')

print(f'\nSample of Merged Data:')
print(merged_data[['date', 'price', 'year_month', 'seattle_hpi']].head(10).to_string())

# ===== CODE CELL 19 =====
plt.figure(figsize=(14, 8))
scatter = plt.scatter(merged_data['seattle_hpi'], merged_data['price'], 
                     alpha=0.4, c=merged_data['seattle_hpi'], cmap='viridis', s=20)
cbar = plt.colorbar(scatter, label='Seattle HPI Index')
plt.title('House Price vs. Seattle HPI Index', fontsize=14, fontweight='bold')
plt.xlabel('Seattle HPI Index', fontsize=12)
plt.ylabel('House Price ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate correlation
correlation = merged_data['price'].corr(merged_data['seattle_hpi'])
print(f'\nPearson Correlation between House Price and Seattle HPI: {correlation:.4f}')

# ===== CODE CELL 20 =====
# Calculate monthly statistics
monthly_stats = merged_data.groupby('year_month').agg({
    'price': ['mean', 'median', 'count'],
    'seattle_hpi': 'first'
}).reset_index()
monthly_stats.columns = ['year_month', 'avg_price', 'median_price', 'count', 'hpi']
monthly_stats['year_month'] = monthly_stats['year_month'].dt.to_timestamp()

# Create dual-axis plot
fig, ax1 = plt.subplots(figsize=(14, 7))

# Left axis: Average price
color1 = '#2E86AB'
ax1.set_xlabel('Date', fontsize=12)
ax1.set_ylabel('Average House Price ($)', color=color1, fontsize=12)
ax1.plot(monthly_stats['year_month'], monthly_stats['avg_price'], 
        color=color1, marker='o', linewidth=2.5, markersize=8, label='Avg House Price')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, alpha=0.3)

# Right axis: HPI
ax2 = ax1.twinx()
color2 = '#A23B72'
ax2.set_ylabel('Seattle HPI Index', color=color2, fontsize=12)
ax2.plot(monthly_stats['year_month'], monthly_stats['hpi'], 
        color=color2, marker='s', linewidth=2.5, markersize=8, linestyle='--', label='Seattle HPI')
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('Monthly Average House Price vs. Seattle HPI (May 2014 - May 2015)', 
         fontsize=14, fontweight='bold')
fig.tight_layout()
plt.show()

print('\nMonthly Statistics:')
print(monthly_stats[['year_month', 'avg_price', 'median_price', 'count', 'hpi']].to_string())

# ===== CODE CELL 21 =====
# Create HPI quartiles
merged_data['hpi_quartile'] = pd.qcut(merged_data['seattle_hpi'].dropna(), 
                                       q=4, labels=['Q1 (Low)', 'Q2 (Low-Mid)', 'Q3 (Mid-High)', 'Q4 (High)'])

# Create box plot
fig, ax = plt.subplots(figsize=(12, 7))
merged_data.boxplot(column='price', by='hpi_quartile', ax=ax, patch_artist=True)
plt.title('House Price Distribution by Seattle HPI Quartile', fontsize=14, fontweight='bold')
plt.suptitle('')  # Remove default title
plt.xlabel('Seattle HPI Quartile', fontsize=12)
plt.ylabel('House Price ($)', fontsize=12)
plt.tight_layout()
plt.show()

print('\nPrice Statistics by HPI Quartile:')
quartile_stats = merged_data.groupby('hpi_quartile')['price'].describe()
print(quartile_stats)
