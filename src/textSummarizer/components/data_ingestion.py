import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger

from src.textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file_path):
            filename,headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file_path
            )
            logger.info(f"File is downloaded")
        else:
            logger.info(f"File already exists")
    
    def extract_zip_file(self):
        """
        zip_file_path : str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path=self.config.unzip_dir_path
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file_path,'r') as zip_ref:
            zip_ref.extractall(unzip_path)