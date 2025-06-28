

import csv
import os
import time
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(current_dir, "..", "data_stream")
os.makedirs(data_folder, exist_ok=True)

shipment_id = 1000


product_types = {
    "product_101": (500, 530),
    "product_102": (140, 150),
    "product_103": (300, 330),
    "product_104": (60, 70),
    "product_105": (700, 800),
    "product_106": (250, 280),
}

while True:
    product = random.choice(list(product_types.keys()))
    low, high = product_types[product]
    value = round(random.uniform(low * 0.8, high * 1.2), 2)

    filename = os.path.join(data_folder, f"shipment_{shipment_id}.csv")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["shipment_id", "product_type", "value", "timestamp"])
        writer.writerow([
            f"SHP{shipment_id}",
            product,
            value,
            time.time()
        ])

    print(f"📦 Generated: shipment_{shipment_id}.csv — {product} worth ₹{value}")
    shipment_id += 1
    time.sleep(5)
