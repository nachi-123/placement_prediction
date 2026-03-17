## Student Placement Prediction System

End-to-end Machine Learning project for predicting student placement outcome.

Target:

- status (Placed / Not Placed)

Dataset:

- Campus Placement Dataset
- File used in this project: notebook/data/Placement_Data_Full_Class.csv

## Project Structure

The code keeps a modular pipeline design:

- src/components/data_ingestion.py
- src/components/data_transformation.py
- src/components/model_trainer.py
- src/pipeline/train_pipeline.py
- src/pipeline/predict_pipeline.py
- application.py

Training flow:

- data_ingestion -> data_transformation -> model_trainer

Inference flow:

- Flask form input -> predict_pipeline -> predicted status

## Features Used

Input features used for training and prediction:

- gender
- ssc_p
- ssc_b
- hsc_p
- hsc_b
- hsc_s
- degree_p
- degree_t
- workex
- etest_p
- specialisation
- mba_p

Ignored columns:

- sl_no (identifier)
- salary (post-placement leakage for status task)

Target column:

- status

## Setup

1. Create and activate virtual environment

Windows PowerShell:

```powershell
python -m venv pp
pp\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

## Train Model

```powershell
python train.py
```

This generates artifacts in the artifacts directory:

- artifacts/preprocessor.pkl
- artifacts/model.pkl
- artifacts/target_encoder.pkl

## Run Flask App

```powershell
python application.py
```

Open the app in browser:

- http://127.0.0.1:5000/

## Notes

- Preprocessing is dtype-driven (no hardcoded column indices).
- Categorical and numerical pipelines are handled via ColumnTransformer.
- Model training uses classification algorithms and accuracy-based model selection.
