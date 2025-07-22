import pandas as pd

def prepare_data():
    # Simulate synthetic data
    data = {
        'aircraft_weight': [120000, 130000, 140000],
        'runway_length': [2500, 2600, 2400],
        'wind_speed': [10, 5, 15],
        'weather_condition': [1, 2, 0],  # Encoded: 0=Clear, 1=Rain, 2=Fog
        'actual_landing_distance': [1900, 2000, 2100]
    }

    df = pd.DataFrame(data)
    df.to_csv('data/landing_data.csv', index=False)
    print("✅ Data saved to data/landing_data.csv")

if __name__ == "__main__":
    prepare_data()
