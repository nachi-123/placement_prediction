import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            target_encoder_path = os.path.join('artifacts', 'target_encoder.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)

            if os.path.exists(target_encoder_path):
                target_encoder = load_object(file_path=target_encoder_path)
                preds = target_encoder.inverse_transform(preds.astype(int))

            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        gender: str,
        ssc_p: float,
        ssc_b: str,
        hsc_p: float,
        hsc_b: str,
        hsc_s: str,
        degree_p: float,
        degree_t: str,
        workex: str,
        etest_p: float,
        specialisation: str,
        mba_p: float):

        self.gender = gender
        self.ssc_p = ssc_p
        self.ssc_b = ssc_b
        self.hsc_p = hsc_p
        self.hsc_b = hsc_b
        self.hsc_s = hsc_s
        self.degree_p = degree_p
        self.degree_t = degree_t
        self.workex = workex
        self.etest_p = etest_p
        self.specialisation = specialisation
        self.mba_p = mba_p

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "ssc_p": [self.ssc_p],
                "ssc_b": [self.ssc_b],
                "hsc_p": [self.hsc_p],
                "hsc_b": [self.hsc_b],
                "hsc_s": [self.hsc_s],
                "degree_p": [self.degree_p],
                "degree_t": [self.degree_t],
                "workex": [self.workex],
                "etest_p": [self.etest_p],
                "specialisation": [self.specialisation],
                "mba_p": [self.mba_p],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

