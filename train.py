from src.pipeline.train_pipeline import TrainPipeline
from src.exception import CustomException
import sys

if __name__ == "__main__":
    try:
        print("Starting Training Pipeline...")
        
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        
        print("Training Completed Successfully!")
    
    except Exception as e:
        raise CustomException(e, sys)