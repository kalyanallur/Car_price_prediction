import os 
import sys
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from exception import CustomException
from logger import logging
import pickle
import numpy as np
from src.utils import savefile

class DataTransformation:

    def __init__(self) :
        preprocessor_dir = os.path.join(os.getcwd(),"pickles")
        os.makedirs(preprocessor_dir, exist_ok=True)
        self.preprocessor_path = os.path.join(preprocessor_dir,"preprocessor.pkl")

    def preprocess(self):
        try:
            cat_columns = ['abtest', 'vehicleType', 'gearbox', 'fuelType']
            num_column = [ 'yearOfRegistration', 'powerPS', 'kilometer','monthOfRegistration']

            cat_transformation =Pipeline([("encoding", OneHotEncoder()),
                                        ("scaling", StandardScaler(with_mean=False))])
            num_transformation = Pipeline([("scaling",StandardScaler())])

            preprocessor = ColumnTransformer(transformers=[("num", num_transformation, num_column),
                                                        ("cat", cat_transformation, cat_columns)])
            
            savefile(self.preprocessor_path, preprocessor)
            logging.info("preprocessor pickel has been dumped..")
            return preprocessor
        
        except Exception as e:
            logging.info("exception while building preprocessor...")
            raise CustomException(e)
        

    def transform_data(self, train_df, test_df):
        try:
            x_train = train_df.drop("price", axis = 1)
            x_test = test_df.drop("price", axis = 1)
            y_train=train_df["price"]
            y_test = test_df["price"]

            obj =self.preprocess()
            x_train = obj.fit_transform(x_train)
            x_test = obj.transform(x_test)
            transformed_train_df = np.concatenate([x_train,np.array(y_train).reshape(-1,1)], axis = 1)
            transformed_test_df = np.concatenate([x_test,np.array(y_test).reshape(-1,1)],axis = 1)
            logging.info("data transformed successfully")
            return transformed_train_df,transformed_test_df
        
        except Exception as e:
            logging.info("exception while transforming data...")
            raise CustomException(e)