# from cnnClassifier.config.configuration import ConfigurationManager
# from cnnClassifier.components.data_ingestion import DataIngestion
# from cnnClassifier import logger

# STAGE_NAME= "Data Ingestion stage"

# class DataIngestionTraingPipeline:
#     def __init__(self) -> None:
#         pass

#     def main(self):
#         config=ConfigurationManager()
#         data_ingestion_config=config.get_data_ingestion_config()
#         data_ingestion=DataIngestion(config=data_ingestion_config)
#         data_ingestion=download_file()
#         data_ingestion.extract_zip_file()

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTraingPipeline:
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
        obj=DataIngestionTraingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e



