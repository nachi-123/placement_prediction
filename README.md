<div align="center">
  <h1>🎓 Campus Placement Prediction System</h1>
  <p>An end-to-end Machine Learning web application to predict student placement outcomes.</p>

  <!-- Optional Badges -->
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" />
  <img alt="Flask" src="https://img.shields.io/badge/Flask-Web%20App-lightgrey?logo=flask" />
  <img alt="Machine Learning" src="https://img.shields.io/badge/Machine%20Learning-Scikit_Learn-orange?logo=scikit-learn" />
</div>

<br />

## 📑 Table of Contents

- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Dataset Details](#dataset-details)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [1. Model Training](#1-model-training)
  - [2. Running the Web App](#2-running-the-web-app)
- [Notes & Considerations](#notes--considerations)

---

## 📖 About the Project

This project provides a complete Machine Learning pipeline designed to predict whether a student will be successfully placed during campus recruitment based on various academic and demographic features. It includes a user-friendly web interface powered by Flask where users can input student details and instantly receive a prediction.

## 💻 Tech Stack

- **Backend / Web Framework**: Python, Flask
- **Data Science & ML**: Pandas, NumPy, Scikit-Learn
- **Frontend**: HTML5, CSS (via Jinja2 templates)
- **Containerization**: Docker (via `Dockerfile`)

## 🏗️ Project Architecture

The codebase follows a modular design, separating ingestion, transformation, and training into distinct components:

```text
src/
├── components/
│   ├── data_ingestion.py      # Reads data and splits into train/test sets
│   ├── data_transformation.py # Handles preprocessing & feature engineering
│   └── model_trainer.py       # Trains algorithms and outputs the best model
└── pipeline/
    ├── train_pipeline.py      # Orchestrates the training pipeline
    └── predict_pipeline.py    # Loads models for application inference
```

**Workflow Design**:

- **Training Flow**: `Data Ingestion` ➔ `Data Transformation` ➔ `Model Trainer`
- **Inference Flow**: `Flask UI Input` ➔ `Predict Pipeline` ➔ `Returned Prediction Output`

## 📊 Dataset Details

The system uses the **Campus Placement Dataset** (`notebook/data/Placement_Data_Full_Class.csv`).

**Input Features Evaluated**:

- `gender` (M/F)
- `ssc_p`, `ssc_b` (Secondary Education percentage & board)
- `hsc_p`, `hsc_b`, `hsc_s` (Higher Secondary percentage, board, & stream)
- `degree_p`, `degree_t` (Undergrad percentage & type)
- `workex` (Work Experience: Yes/No)
- `etest_p` (Employability test percentage)
- `specialisation` (MBA Specialization)
- `mba_p` (MBA percentage)

_Note: `sl_no` (serial number) is ignored as an identifier, and `salary` is dropped to prevent data leakage (since salary is a post-placement outcome)._

**Target Variable**: `status` (Placed / Not Placed)

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed on your system.
- **Git** installed to clone the repository.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nachi-123/placement_prediction.git
   cd campus_placement_prediction
   ```

2. **Create and activate a virtual environment:**
   _Windows (PowerShell):_

   ```powershell
   python -m venv pp
   .\pp\Scripts\Activate.ps1
   ```

   _Linux/Mac:_

   ```bash
   python3 -m venv pp
   source pp/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

### 1. Model Training

To train the model from scratch and generate new artifact files, run:

```bash
python train.py
```

This process automatically generates the following inside the `artifacts/` folder:

- `preprocessor.pkl` (Data transformations)
- `model.pkl` (Trained Machine Learning model)
- `target_encoder.pkl` (Target label encoders)

### 2. Running the Web App

Once the model artifacts are ready, start the Flask application:

```bash
python application.py
```

Open a web browser and navigate to: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

## 📝 Notes & Considerations

- The preprocessing steps are designed to be **dtype-driven**, meaning transformations dynamically handle columns based on their data types rather than relying on hardcoded column indices, ensuring robustness for feature updates.
- The project includes a `Dockerfile` if you prefer to build and run this application in an isolated container instance.

* Categorical and numerical pipelines are handled via ColumnTransformer.
* Model training uses classification algorithms and accuracy-based model selection.
