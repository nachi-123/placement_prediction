from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.exception import CustomException
import sys

class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            print("Step 1: Data Ingestion started")
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()
            print("Data Ingestion completed")

            print("Step 2: Data Transformation started")
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_path, test_path)
            print("Data Transformation completed")

            print("Step 3: Model Training started")
            model_trainer = ModelTrainer()
            model_trainer.initiate_model_trainer(train_arr, test_arr)
            print("Model Training completed")

        except Exception as e:
            raise CustomException(e, sys)