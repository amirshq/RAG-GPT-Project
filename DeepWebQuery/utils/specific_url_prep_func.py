# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urlparse
# import re
from typing import List
import yaml
from utils.app_utils import Apputils
from utils.prepare_url_vectordb import PrepareURLVectorDB
import time
import traceback


class URLPrep:
    """
    A class to check URLs within a given text for their content type.

    Attributes:
        url (str): The requested url by the user.
    """

    def __init__(self, url: str) -> None:
        """
        Initializes the URLCheck instance with the provided text.

        Parameters:
            url (str): The requested url by the user.
        """
        self.url = url
        with open("configs/app_config.yml") as cfg:
            app_config = yaml.load(cfg, Loader=yaml.FullLoader)
            self.chunk_size = app_config["RAG"]["chunk_size"]
            self.chunk_overlap = app_config["RAG"]["chunk_overlap"]
            self.persist_directory = app_config["RAG"]["persist_directory"]
            self.persist_directory = f"{self.persist_directory}chroma_{int(time.time())}"
            # create a new one for the new url.
            Apputils.create_directory(self.persist_directory)
            self.embedding_model_engine = app_config["RAG"]["embedding_model_engine"]

    def prepare_vector_db(self):
        """NOTE: ___Cannot handle both youtube links and webpages or multiple urls for now___"""
        try:
            prepare_url_vectordb_instance = PrepareURLVectorDB(
                url=self.url,
                persist_directory=self.persist_directory,
                embedding_model_engine=self.embedding_model_engine,
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap)
            db_stat = prepare_url_vectordb_instance.prepare_and_save_vectordb()
            return db_stat
        except BaseException as e: 
            print(f"Caught exception in URLPrep class: {e}")
            traceback.print_exc()
            return False


def search_the_requested_url(user_requested_url: str) -> List[str]:
    """
    Searches for URLs in the user's query and checks their content types.

    Parameters:
        user_full_query (str): The user's query containing potential URLs.

    Returns:
        List[str]: A list of content types for each URL found in the query.
    """
    url_checker_instance = URLPrep(url=user_requested_url)
    status_bool = url_checker_instance.prepare_vector_db()
    return status_bool
