import os
import pandas as pd
from exception import CustomException
from logger import logging
from sklearn.model_selection import train_test_split
from data_transformation import DataTransformation

class Data_ingestion :


    def __init__(self):
        data_directory = os.path.join(os.getcwd(), "Artifacts")
        os.makedirs(data_directory, exist_ok=True)
        self.data_path = os.path.join(data_directory,"data.csv")
        self.train_df_path = os.path.join(data_directory,"train_df.csv")
        self.test_df_path = os.path.join(data_directory,"test.csv")


    def get_data(self, csv_path):
        try:
            df = pd.read_csv(csv_path)
            logging.info("Data file loaded...")
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42) 
            train_df.to_csv(self.train_df_path,index =False )
            test_df.to_csv(self.test_df_path,index =False )
            logging.info(f"""data splitted as test and train parts successfully with 
                         train shape: {train_df.shape}
                         test shape:  {test_df.shape}""")
            df.to_csv(self.data_path, index=False)
            return train_df, test_df

        except Exception as e:
            logging.info("error while loading the data file.....")
            raise CustomException(e)

obj = Data_ingestion()
train_df, test_df = obj.get_data(r"C:\Users\HP\Desktop\Used cars prediction\data\cars_data.csv")

transformer_obj = DataTransformation()
transformed_train_df,transformed_test_df = transformer_obj.transform_data(train_df, test_df)