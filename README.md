# 🛬 ROAAS ML Simulator

Simulated AI/ML pipeline to predict aircraft landing distance and prevent runway overruns, inspired by the Runway Overrun Awareness and Alerting System (ROAAS) from the aviation safety domain.

## ✈️ Objective

The goal is to demonstrate how AI/ML can be applied to aviation safety by predicting landing distances based on aircraft parameters, weather, and runway data—simulating the real-world ROAAS system.

## 🧠 Key Features

- End-to-end ML pipeline in Python
- Simulated flight landing dataset
- Feature engineering & model training (Random Forest, XGBoost)
- Real-time inference simulation
- CI/CD integration with GitHub Actions
- Containerized with Docker
- Cloud deployment via Azure ML (mock)

## 🧰 Tech Stack

| Category       | Tools & Frameworks                       |
|----------------|------------------------------------------|
| Language       | Python                                   |
| ML Libraries   | Scikit-learn, XGBoost, Pandas, NumPy     |
| Visualization  | Matplotlib, Seaborn                      |
| Pipeline       | Custom Python ETL / Airflow (optional)   |
| CI/CD          | GitHub Actions, Docker                   |
| Cloud          | Azure ML SDK (mock)                      |

## 📁 Folder Structure

```
roaas-ml-simulator/
├── data/            → Synthetic aircraft landing data
├── notebooks/       → EDA and model notebooks
├── src/
│   ├── model/       → Model training and inference
│   ├── pipeline/    → Data ingestion and transformation
│   └── utils/       → Helper functions
├── tests/           → Unit tests
├── .github/workflows/ → CI pipeline
```

## ⚙️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/rshekhawath/roaas-ml-simulator.git
cd roaas-ml-simulator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run training
python src/model/train.py

# 4. Run inference
python src/model/infer.py --input sample.json
```

## 🧪 CI/CD

This repo uses **GitHub Actions** to:
- Run tests on every push
- Lint Python code
- Build Docker image

## 🐳 Docker Usage

```bash
# Build Docker image
docker build -t roaas-ml .

# Run container
docker run -it roaas-ml
```

## ☁️ Azure Deployment (Mock)

Mock config included to simulate cloud deployment via `azure-deploy.yml`

## 📊 Future Plans

- Add RESTful API for inference
- Visual dashboards with Power BI/Tableau
- Include weather runway integration
- DO-178C compliance stubs

## 📝 License

MIT License

## 🤝 Credits

Inspired by real-world work at Collins Aerospace for aviation safety and predictive ML systems.
