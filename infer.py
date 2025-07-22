import joblib
import pandas as pd
import json
import sys

def load_input(file_path):
    with open(file_path, 'r') as f:
        return pd.DataFrame([json.load(f)])

def predict_landing_distance(input_df):
    model = joblib.load('model.joblib')
    prediction = model.predict(input_df)
    return prediction[0]

if __name__ == "__main__":
    input_path = sys.argv[1]
    df_input = load_input(input_path)
    result = predict_landing_distance(df_input)
    print(f"Predicted Landing Distance: {result:.2f} meters")
