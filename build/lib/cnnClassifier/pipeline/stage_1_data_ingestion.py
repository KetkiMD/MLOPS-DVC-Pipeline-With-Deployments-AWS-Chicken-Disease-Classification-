from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
import os
import urllib.request as request
from pathlib import Path
from dataclasses import dataclass
from cnnClassifier.entity import DataIngestionConfig
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        # Assuming you've manually extracted the zip file, no need to call download_file() and extract_zip_file()
        logger.info("Manually ensure the zip file is extracted to the correct location.")
        logger.info(f"Configured unzip directory: {data_ingestion_config.unzip_dir}")

if __name__=='__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
