# 🚚 Logistics Pulse Copilot

Detect fraud and policy violations in real-time logistics using LSTM models, Pathway streaming, and LangGraph + Gemini for policy checks.

---

## 📁 Project Structure

```
shipment-fraud-rag/
├── data/                    # Product price CSVs
├── data_stream/            # Real-time shipment data (CSV input stream)
├── models_lstm/            # Trained LSTM models & scalers
├── src/
│   ├── pathway_ingest.py   # Pathway logic to detect shipment anomalies
├── main.py                 # LangGraph pipeline for violation checking
├── violates.py             # Streamlit UI for clause checking
├── lstm.py                 # LSTM model training & prediction
├── anomalies.jsonl         # Output anomalies detected
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker setup
├── start.md                # Team intro and pitch
├── models_lstm.zip         # Zipped models
├── backend/                # Backend folder placeholder
├── frontend/               # React frontend folder placeholder
└── README.md
```

---

## 🌟 Features

- 📈 **Price prediction** using LSTM model for each product
- 📦 **Real-time shipment anomaly detection** with Pathway
- 📄 **Clause violation detection** using LangGraph + Gemini + Pinecone
- 🌐 **Streamlit interface** to upload and index PDF policy documents
- 🔍 Detect if a shipment or price deviation violates SLA or policy

---

## ⚙️ Tech Stack

- **Python** with TensorFlow, Pathway, LangGraph
- **Pinecone** for semantic clause storage
- **Gemini 1.5 Flash** (via LangChain)
- **Streamlit** for UI
- **React** frontend
- **Docker** for containerization

---

## 🧠 How It Works

### 1. 📉 LSTM Model
- Each product's CSV file is used to train an LSTM.
- Predicted next prices are appended back into the CSV.

### 2. 📦 Shipment Distance Anomaly
- Shipment data is streamed in `data_stream/`
- If the distance deviation > 10 km → marked as anomaly
- Written to `anomalies.jsonl`

### 3. 📄 Policy Violation Checker
- Upload PDF of policies via Streamlit
- Pinecone stores chunks from PDF
- Alert (question) checked using Gemini LLM
- Returns violation explanation & clause

---

## 🛠️ Run Locally

### 🔧 Step 1: Set Up Python Env

```bash
cd shipment-fraud-rag
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 🚨 Step 2: Start Pathway Distance Anomaly Detection

This will watch `data_stream/` for new shipments and append anomalies to `anomalies.jsonl`.

```bash
python src/pathway_ingest.py
```

### 🧠 Step 3: Check SLA Violations via Streamlit UI

```bash
streamlit run violates.py
```

### 🐳 Optional: Run Entire Flow in Docker

```bash
docker build -t shipment-anomaly-detector .
docker run -v $(pwd)/data_stream:/app/data_stream -v $(pwd)/anomalies.jsonl:/app/anomalies.jsonl shipment-anomaly-detector
```

---

## 🧑‍💻 Authors

Built by **Team Coders123** for Geekroom Code Cubicle 4.0 🚀
- Aditya Karn
- Adarsh Dubey
- Ansh Singh
- Aditya Gupta

---

