'''
Created on 9/27/26 at 7:40 PM 
By yuvarajdurairaj
Module Name: logger_util
'''
import logging
import sys

from dotenv import load_dotenv

load_dotenv()


def get_app_logger(calling_module_name:str):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        handlers=[
                            logging.StreamHandler(sys.stdout)
                        ]
                        )
    logger = logging.getLogger(f"GENAI-EXEMPLARS.{calling_module_name}")
    return logger

