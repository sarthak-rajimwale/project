import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig

if __name__=='__main__':
    logging.info('Started')
    try:
        DataIngestion=DataIngestion()
        DataIngestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)