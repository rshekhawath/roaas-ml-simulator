import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model():
    # Load data
    df = pd.read_csv('data/landing_data.csv')

    # Feature & target selection
    X = df[['aircraft_weight', 'runway_length', 'wind_speed', 'weather_condition']]
    y = df['actual_landing_distance']

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save model
    joblib.dump(model, 'model.joblib')
    print("✅ Model trained and saved as model.joblib")

if __name__ == '__main__':
    train_model()