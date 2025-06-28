import os
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

DATA_DIR = "data"
MODEL_DIR = "models_lstm"
SEQUENCE_LENGTH = 5

for filename in os.listdir(DATA_DIR):
    if filename.endswith(".csv"):
        product_id = filename.replace(".csv", "")
        csv_path = os.path.join(DATA_DIR, filename)
        model_path = os.path.join(MODEL_DIR, f"{product_id}_lstm.h5")
        scaler_path = os.path.join(MODEL_DIR, f"{product_id}_scaler.save")

        if not os.path.exists(model_path) or not os.path.exists(scaler_path):
            continue

        df = pd.read_csv(csv_path)
        if len(df) < SEQUENCE_LENGTH:
            continue

        recent_prices = df['price'].values[-SEQUENCE_LENGTH:].reshape(-1, 1)
        model = load_model(model_path, compile=False)
        scaler = joblib.load(scaler_path)

        scaled_input = scaler.transform(recent_prices)
        X = np.array([scaled_input])
        predicted_scaled = model.predict(X)
        predicted_price = scaler.inverse_transform(predicted_scaled)[0][0]

        new_row = {"price": round(predicted_price, 2)}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(csv_path, index=False)

        print(f"{product_id}: ₹{predicted_price:.2f} appended.")
