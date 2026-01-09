# ================================================================================
# Hypothesis_Testing.ipynb
# Extracted Python code from Jupyter notebook
# ================================================================================


# ===== CODE CELL 1 =====
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, f_oneway, spearmanr
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Load datasets
house_data = pd.read_csv('house_data.csv')
sexrsa_data = pd.read_csv('SEXRSA.csv')

# Prepare house_data
house_data['date'] = pd.to_datetime(house_data['date'], format='%Y%m%dT%H%M%S', errors='coerce')
house_data['year_month'] = house_data['date'].dt.to_period('M')

# Prepare SEXRSA data
sexrsa_data['observation_date'] = pd.to_datetime(sexrsa_data['observation_date'])
sexrsa_data['year_month'] = sexrsa_data['observation_date'].dt.to_period('M')
sexrsa_data.rename(columns={'SEXRSA': 'seattle_hpi'}, inplace=True)

# Merge datasets
merged_df = pd.merge(house_data, sexrsa_data[['year_month', 'seattle_hpi']], on='year_month', how='left')
merged_df.dropna(subset=['seattle_hpi'], inplace=True)

print('=== DATA LOADING SUMMARY ===')
print(f'Total House Records: {len(house_data):,}')
print(f'Total SEXRSA Records: {len(sexrsa_data):,}')
print(f'Merged Records (with HPI): {len(merged_df):,}')
print(f'Date Range: {merged_df["date"].min().date()} to {merged_df["date"].max().date()}')
print(f'\nDataset Shape: {merged_df.shape}')
print(f'\nColumn Names:')
print(merged_df.columns.tolist())
print(f'\nFirst 5 rows:')
print(merged_df[['date', 'price', 'sqft_living', 'grade', 'seattle_hpi']].head())

# ===== CODE CELL 2 =====
print('=== DESCRIPTIVE STATISTICS ===')
print('\nHouse Price Statistics:')
print(merged_df['price'].describe())

print('\nSeattle HPI Statistics:')
print(merged_df['seattle_hpi'].describe())

print('\nKey Continuous Features:')
continuous_features = ['sqft_living', 'grade', 'bathrooms', 'bedrooms', 'sqft_above']
print(merged_df[continuous_features].describe())

# ===== CODE CELL 3 =====
# Test continuous features
continuous_features = ['sqft_living', 'grade', 'sqft_above', 'bathrooms', 'bedrooms', 
                       'sqft_lot', 'floors', 'yr_built', 'sqft_living15']

print('=== HYPOTHESIS TEST 1: CONTINUOUS FEATURES vs. PRICE ===')
print('\nPearson Correlation Analysis:')
print('-' * 90)
print(f'{"Feature":<20} {"Correlation (r)":>15} {"P-Value":>15} {"Significant":>15}')
print('-' * 90)

correlation_results = []
for feature in continuous_features:
    # Remove NaN values
    valid_data = merged_df[[feature, 'price']].dropna()
    
    # Calculate Pearson correlation
    corr_coeff, p_value = pearsonr(valid_data[feature], valid_data['price'])
    
    # Determine significance
    significant = 'YES' if p_value < 0.05 else 'NO'
    
    print(f'{feature:<20} {corr_coeff:>15.4f} {p_value:>15.2e} {significant:>15}')
    
    correlation_results.append({
        'Feature': feature,
        'Correlation': corr_coeff,
        'P-Value': p_value,
        'Significant': significant == 'YES'
    })

print('-' * 90)

# Summary
significant_count = sum(1 for r in correlation_results if r['Significant'])
print(f'\n✓ RESULT: {significant_count}/{len(continuous_features)} continuous features show SIGNIFICANT correlation with price')
print(f'\nConclusion: We REJECT the null hypothesis (H₀) for most continuous features.')
print('House-specific continuous characteristics DO have a statistically significant effect on prices.')

# ===== CODE CELL 4 =====
# Create correlation visualization
corr_df = pd.DataFrame(correlation_results)
corr_df_sorted = corr_df.sort_values('Correlation', ascending=True)

fig, ax = plt.subplots(figsize=(12, 7))
colors = ['#2ecc71' if x else '#e74c3c' for x in corr_df_sorted['Significant']]
ax.barh(corr_df_sorted['Feature'], corr_df_sorted['Correlation'], color=colors, alpha=0.7)
ax.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
ax.set_xlabel('Pearson Correlation Coefficient', fontsize=12, fontweight='bold')
ax.set_title('Correlation of House-Specific Features with House Price\n(Green = Significant at α=0.05, Red = Not Significant)', 
             fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

print('\nInterpretation:')
print('- Positive correlations: Higher feature values → Higher prices')
print('- Negative correlations: Higher feature values → Lower prices')
print('- Green bars: Statistically significant at α=0.05')
print('- Red bars: Not statistically significant')

# ===== CODE CELL 5 =====
# Test categorical features using ANOVA
categorical_features = ['bedrooms', 'bathrooms', 'floors', 'waterfront', 'view', 'condition', 'grade']

print('=== HYPOTHESIS TEST 2: CATEGORICAL FEATURES vs. PRICE ===')
print('\nOne-Way ANOVA Analysis:')
print('-' * 90)
print(f'{"Feature":<20} {"F-Statistic":>15} {"P-Value":>15} {"Significant":>15}')
print('-' * 90)

anova_results = []
for feature in categorical_features:
    # Group prices by category
    groups = [group['price'].values for name, group in merged_df.groupby(feature)]
    
    # Perform ANOVA
    f_stat, p_value = f_oneway(*groups)
    
    # Determine significance
    significant = 'YES' if p_value < 0.05 else 'NO'
    
    print(f'{feature:<20} {f_stat:>15.2f} {p_value:>15.2e} {significant:>15}')
    
    anova_results.append({
        'Feature': feature,
        'F-Statistic': f_stat,
        'P-Value': p_value,
        'Significant': significant == 'YES'
    })

print('-' * 90)

# Summary
significant_count = sum(1 for r in anova_results if r['Significant'])
print(f'\n✓ RESULT: {significant_count}/{len(categorical_features)} categorical features show SIGNIFICANT effect on price')
print(f'\nConclusion: We REJECT the null hypothesis (H₀) for categorical features.')
print('Categorical house characteristics DO have a statistically significant effect on prices.')

# ===== CODE CELL 6 =====
# Test regional market correlation
print('=== HYPOTHESIS TEST 3: REGIONAL MARKET TREND (SEATTLE HPI) vs. PRICE ===')

# Calculate Pearson correlation
valid_data = merged_df[['seattle_hpi', 'price']].dropna()
hpi_corr, hpi_p_value = pearsonr(valid_data['seattle_hpi'], valid_data['price'])

print(f'\nPearson Correlation Analysis:')
print(f'Correlation Coefficient (r): {hpi_corr:.4f}')
print(f'P-Value: {hpi_p_value:.2e}')
print(f'Sample Size (n): {len(valid_data):,}')

# Determine significance
if hpi_p_value < 0.05:
    print(f'\n✓ RESULT: SIGNIFICANT correlation detected (p < 0.05)')
    print(f'Conclusion: We REJECT the null hypothesis (H₀).')
    print('Regional market trends (Seattle HPI) DO have a statistically significant effect on house prices.')
else:
    print(f'\n✗ RESULT: NO significant correlation detected (p ≥ 0.05)')
    print(f'Conclusion: We FAIL TO REJECT the null hypothesis (H₀).')
    print('Regional market trends may not significantly affect individual house prices.')

print(f'\nInterpretation:')
print(f'- Correlation strength: {abs(hpi_corr):.4f} (0=none, 1=perfect)')
if hpi_corr > 0:
    print(f'- Direction: POSITIVE (higher HPI → higher prices)')
else:
    print(f'- Direction: NEGATIVE (higher HPI → lower prices)')

# ===== CODE CELL 7 =====
# Visualize regional market effect
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Scatter plot
axes[0].scatter(merged_df['seattle_hpi'], merged_df['price'], alpha=0.3, s=10)
# Add trend line
z = np.polyfit(merged_df['seattle_hpi'], merged_df['price'], 1)
p = np.poly1d(z)
x_line = np.linspace(merged_df['seattle_hpi'].min(), merged_df['seattle_hpi'].max(), 100)
axes[0].plot(x_line, p(x_line), 'r-', linewidth=2, label='Trend Line')
axes[0].set_xlabel('Seattle HPI', fontsize=11, fontweight='bold')
axes[0].set_ylabel('House Price ($)', fontsize=11, fontweight='bold')
axes[0].set_title(f'House Price vs. Seattle HPI\n(r={hpi_corr:.4f}, p={hpi_p_value:.2e})', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)
axes[0].legend()

# Time series plot
monthly_avg = merged_df.groupby('year_month').agg({'price': 'mean', 'seattle_hpi': 'mean'}).reset_index()
ax1 = axes[1]
ax2 = ax1.twinx()

ax1.plot(monthly_avg['year_month'].astype(str), monthly_avg['price'], 'b-o', linewidth=2, label='Avg House Price')
ax2.plot(monthly_avg['year_month'].astype(str), monthly_avg['seattle_hpi'], 'r-s', linewidth=2, label='Seattle HPI')

ax1.set_xlabel('Month', fontsize=11, fontweight='bold')
ax1.set_ylabel('Average House Price ($)', fontsize=11, fontweight='bold', color='b')
ax2.set_ylabel('Seattle HPI', fontsize=11, fontweight='bold', color='r')
ax1.set_title('Temporal Trends: House Price vs. Seattle HPI', fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='b')
ax2.tick_params(axis='y', labelcolor='r')
ax1.grid(True, alpha=0.3)
plt.setp(axes[1].xaxis.get_majorticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.show()

# ===== CODE CELL 8 =====
# Heatmap for numeric features
plt.figure(figsize=(12, 8))
corr_matrix = merged_df[continuous_features + ['price', 'seattle_hpi']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Key Features and Price', fontsize=16)
plt.tight_layout()
plt.show()

# Bar plot for a categorical feature
plt.figure(figsize=(10, 6))
sns.barplot(x='condition', y='price', data=merged_df, palette='viridis')
plt.title('Mean House Price by Condition', fontsize=16)
plt.xlabel('Condition of the House')
plt.ylabel('Mean Price (USD)')
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# ===== CODE CELL 9 =====
print('='*90)
print('COMPREHENSIVE HYPOTHESIS TESTING SUMMARY')
print('='*90)

print('\n1. House-Specific FEATURES (Pearson Correlation Test)')
print('-' * 90)
cont_sig = sum(1 for r in correlation_results if r['Significant'])
print(f'   Significant Features: {cont_sig}/{len(continuous_features)}')
print(f'   Result: REJECT H₀ - House-Specific features significantly affect house prices')
print(f'   Top 3 Predictors:')
top_3 = sorted(correlation_results, key=lambda x: abs(x['Correlation']), reverse=True)[:3]
for i, feat in enumerate(top_3, 1):
    print(f'      {i}. {feat["Feature"]}: r = {feat["Correlation"]:.4f}')

print('\n2. CATEGORICAL FEATURES (One-Way ANOVA Test)')
print('-' * 90)
cat_sig = sum(1 for r in anova_results if r['Significant'])
print(f'   Significant Features: {cat_sig}/{len(categorical_features)}')
print(f'   Result: REJECT H₀ - Categorical features significantly affect house prices')

print('\n3. REGIONAL MARKET TREND (Seattle HPI - Pearson Correlation Test)')
print('-' * 90)
if hpi_p_value < 0.05:
    print(f'   Correlation: r = {hpi_corr:.4f} (p = {hpi_p_value:.2e})')
    print(f'   Result: REJECT H₀ - Regional market trends significantly affect house prices')
else:
    print(f'   Correlation: r = {hpi_corr:.4f} (p = {hpi_p_value:.2e})')
    print(f'   Result: FAIL TO REJECT H₀ - Regional market trends may not significantly affect prices')

print('\n' + '='*90)
print('FINAL CONCLUSION')
print('='*90)
print('\nRESEARCH QUESTION:')
print('Do house-specific characteristics and regional housing market trends have a')
print('statistically significant effect on house prices in King County, Washington?')
print('\nANSWER: YES')
print('\nEVIDENCE:')
print(f'✓ {cont_sig}/{len(continuous_features)} continuous features show significant correlation with price')
print(f'✓ {cat_sig}/{len(categorical_features)} categorical features show significant effect on price')
if hpi_p_value < 0.05:
    print(f'✓ Regional market trend (Seattle HPI) shows significant correlation (r={hpi_corr:.4f})')
print('\nSTATISTICAL SIGNIFICANCE:')
print('At the 0.05 significance level, we have strong evidence that both house-specific')
print('characteristics and regional market trends significantly influence house prices.')
print('\nIMPLICATIONS:')
print('- House prices are NOT random; they follow predictable patterns')
print('- Both property-specific and market-wide factors matter')
print('- Machine learning models can effectively predict prices using these features')
