from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
import os
import urllib.request as request
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path





class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local))}")
