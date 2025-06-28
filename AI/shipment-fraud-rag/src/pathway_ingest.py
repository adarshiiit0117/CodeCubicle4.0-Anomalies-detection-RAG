import os
import pathway as pw
import numpy as np
from tensorflow.keras.models import load_model
from collections import defaultdict, deque

# Product IDs used
VALID_PRODUCTS = [
    "product_101",
    "product_102",
    "product_103",
    "product_104",
    "product_105",
    "product_106",
]


MODELS = {}
for product in VALID_PRODUCTS:
    path = f"models_lstm/{product}_lstm.h5"
    if os.path.exists(path):
        try:
            MODELS[product] = load_model(path, compile=False)
            print(f"[✓] Loaded model for {product}")
        except Exception as e:
            print(f"[!] Failed to load model for {product}: {e}")


PRICE_HISTORY = defaultdict(lambda: deque(maxlen=5))

class ShipmentSchema(pw.Schema):
    shipment_id: str
    product_type: str
    value: float
    timestamp: float


shipments = pw.io.csv.read(
    "data_stream",
    schema=ShipmentSchema,
    mode="streaming",
    autocommit_duration_ms=3000,
)


@pw.udf
def predict_price(product_type: str, value: float) -> float:
    model = MODELS.get(product_type)
    if model is None:
        return -1.0


    PRICE_HISTORY[product_type].append(value)

   
    if len(PRICE_HISTORY[product_type]) < 5:
        return -1.0

    try:
        seq = np.array(PRICE_HISTORY[product_type]).reshape((1, 5, 1))
        prediction = float(model.predict(seq)[0][0])
        return prediction
    except Exception as e:
        print(f"[ERR] Prediction failed for {product_type}: {e}")
        return -1.0


with_predictions = shipments.with_columns(
    predicted_price=predict_price(shipments.product_type, shipments.value)
)


@pw.udf
def detect_anomaly(pred: float, actual: float) -> bool:
    if pred <= 0:
        return False
    return actual < 0.75 * pred or actual > 1.25 * pred

with_flags = with_predictions.with_columns(
    is_anomalous=detect_anomaly(with_predictions.predicted_price, with_predictions.value)
)


@pw.udf
def alert_console(shipment_id, product_type, value, predicted):
    low = 0.75 * predicted
    high = 1.25 * predicted
    print(f"⚠️ Anomaly! [{shipment_id}] {product_type} → ₹{value} vs predicted ₹{predicted:.2f} (expected: ₹{low:.2f} – ₹{high:.2f})")
    return True

anomalies = with_flags.filter(with_flags.is_anomalous)
pw.apply(alert_console, anomalies.shipment_id, anomalies.product_type, anomalies.value, anomalies.predicted_price)


pw.io.jsonlines.write(anomalies, "anomalies.jsonl")


pw.run()
