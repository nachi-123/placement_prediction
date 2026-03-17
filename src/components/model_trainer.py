import os
import sys
from dataclasses import dataclass

from catboost import CatBoostClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
    target_encoder_file_path=os.path.join("artifacts","target_encoder.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            target_encoder = LabelEncoder()
            y_train_encoded = target_encoder.fit_transform(y_train)
            y_test_encoded = target_encoder.transform(y_test)
            models = {
                "Random Forest": RandomForestClassifier(random_state=42),
                "Decision Tree": DecisionTreeClassifier(random_state=42),
                "Gradient Boosting": GradientBoostingClassifier(random_state=42),
                "Logistic Regression": LogisticRegression(max_iter=1000),
                "KNN": KNeighborsClassifier(),
                "XGBClassifier": XGBClassifier(eval_metric='logloss', random_state=42),
                "CatBoostClassifier": CatBoostClassifier(verbose=False, random_state=42),
                "AdaBoost Classifier": AdaBoostClassifier(random_state=42),
            }
            params={
                "Decision Tree": {
                    'criterion':['gini', 'entropy', 'log_loss'],
                    'max_depth': [None, 5, 10, 20],
                },
                "Random Forest":{
                    'n_estimators': [50, 100, 200],
                    'max_depth': [None, 10, 20],
                },
                "Gradient Boosting":{
                    'learning_rate':[0.1, 0.01],
                    'subsample':[0.8, 1.0],
                    'n_estimators': [50, 100, 200],
                },
                "Logistic Regression":{
                    'C': [0.1, 1.0, 10.0],
                    'solver': ['lbfgs', 'liblinear'],
                },
                "KNN":{
                    'n_neighbors': [3, 5, 7, 9],
                    'weights': ['uniform', 'distance'],
                },
                "XGBClassifier":{
                    'learning_rate':[0.1, 0.01],
                    'n_estimators': [50, 100, 200],
                    'max_depth': [3, 5, 7],
                },
                "CatBoostClassifier":{
                    'depth': [4, 6, 8],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [50, 100, 200],
                },
                "AdaBoost Classifier":{
                    'learning_rate':[0.1, 0.01, 0.5],
                    'n_estimators': [50, 100, 200],
                }
                
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train_encoded,X_test=X_test,y_test=y_test_encoded,
                                             models=models,param=params, task_type="classification")
            
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            save_object(
                file_path=self.model_trainer_config.target_encoder_file_path,
                obj=target_encoder
            )

            predicted=best_model.predict(X_test)

            accuracy = accuracy_score(y_test_encoded, predicted)
            return accuracy
            



            
        except Exception as e:
            raise CustomException(e,sys)