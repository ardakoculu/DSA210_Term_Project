# ================================================================================
# Machine_Learning(ML)_Model.ipynb
# Extracted Python code from Jupyter notebook
# ================================================================================


# ===== CODE CELL 1 =====
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (14, 6)
print('All libraries imported successfully')

# ===== CODE CELL 2 =====
house_data = pd.read_csv('house_data.csv')
sexrsa_data = pd.read_csv('SEXRSA.csv')

house_data['date'] = pd.to_datetime(house_data['date'], format='%Y%m%dT%H%M%S', errors='coerce')
house_data['year_month'] = house_data['date'].dt.to_period('M')

sexrsa_data['observation_date'] = pd.to_datetime(sexrsa_data['observation_date'])
sexrsa_data['year_month'] = sexrsa_data['observation_date'].dt.to_period('M')
sexrsa_data.rename(columns={'SEXRSA': 'seattle_hpi'}, inplace=True)

df = pd.merge(house_data, sexrsa_data[['year_month', 'seattle_hpi']], on='year_month', how='left')
df.dropna(subset=['seattle_hpi'], inplace=True)

print(f'Total Records: {len(df):,}')
print(f'Date Range: {df["date"].min().date()} to {df["date"].max().date()}')

# ===== CODE CELL 3 =====
df_model = df.copy()

continuous_features = ['sqft_living', 'grade', 'sqft_above', 'bathrooms', 'bedrooms', 
                       'sqft_lot', 'floors', 'yr_built', 'sqft_living15', 'seattle_hpi']
categorical_features = ['waterfront', 'view', 'condition']

X = df_model[continuous_features + categorical_features].copy()
y = df_model['price'].copy()

X = X.fillna(X.mean())
X = pd.get_dummies(X, columns=categorical_features, drop_first=True)

print(f'Features: {X.shape[1]}')
print(f'Target Statistics:\n{y.describe()}')

# ===== CODE CELL 4 =====
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f'Training Set: {X_train.shape[0]:,} samples')
print(f'Testing Set: {X_test.shape[0]:,} samples')
print(f'Features: {X_train.shape[1]}')

# ===== CODE CELL 5 =====
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Lasso Regression': Lasso(alpha=1000.0),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
}

trained_models = {}
print('Training models...')
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    trained_models[name] = model
    print(f'✓ {name} trained')

print('\nAll models trained successfully!')

# ===== CODE CELL 6 =====
def calculate_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return {'MSE': mse, 'RMSE': rmse, 'MAE': mae, 'R2': r2, 'MAPE': mape}

results = {}
predictions = {}

print('Evaluating models...')
print('-' * 100)
print(f'{"Model":<25} {"R² Score":>12} {"RMSE":>15} {"MAE":>15} {"MAPE":>10}')
print('-' * 100)

for name, model in trained_models.items():
    y_pred = model.predict(X_test_scaled)
    metrics = calculate_metrics(y_test, y_pred)
    results[name] = metrics
    predictions[name] = y_pred
    print(f'{name:<25} {metrics["R2"]:>12.4f} ${metrics["RMSE"]:>14,.0f} ${metrics["MAE"]:>14,.0f} {metrics["MAPE"]:>9.2f}%')

print('-' * 100)

best_model_name = max(results, key=lambda x: results[x]['R2'])
print(f'\nBest Model: {best_model_name} (R² = {results[best_model_name]["R2"]:.4f})')

# ===== CODE CELL 7 =====
results_df = pd.DataFrame(results).T.round(4)
results_df_sorted = results_df.sort_values('R2', ascending=False)

print('\nDetailed Results:')
print(results_df_sorted.to_string())

print('\nModels Ranked by R² Score:')
for i, (model_name, row) in enumerate(results_df_sorted.iterrows(), 1):
    print(f'{i}. {model_name}: R² = {row["R2"]:.4f}')

# ===== CODE CELL 8 =====
best_model = trained_models[best_model_name]
y_pred_best = predictions[best_model_name]

predictions_df = pd.DataFrame({
    'Actual_Price': y_test.values,
    'Predicted_Price': y_pred_best
})

predictions_df['Error'] = predictions_df['Actual_Price'] - predictions_df['Predicted_Price']
predictions_df['Absolute_Error'] = np.abs(predictions_df['Error'])
predictions_df['Percentage_Error'] = (predictions_df['Error'] / predictions_df['Actual_Price'] * 100).round(2)

predictions_df.to_csv('regression_predictions_FINAL.csv', index=False)

print('Predictions CSV Summary:')
print(f'Total Predictions: {len(predictions_df):,}')
print(f'\nFirst 10 predictions:')
print(predictions_df.head(10).to_string())
print(f'\nError Statistics:')
print(f'  Mean Absolute Error: ${predictions_df["Absolute_Error"].mean():,.0f}')
print(f'  Mean Percentage Error: {predictions_df["Percentage_Error"].mean():.2f}%')
print(f'\nSaved: regression_predictions_FINAL.csv')
