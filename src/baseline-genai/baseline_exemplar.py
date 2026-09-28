'''
Created on 9/26/26 at 9:03 PM 
By yuvarajdurairaj
Module Name: baseline_exemplar
'''
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from utils.logger_util import get_app_logger
import polars as pl
from polars import DataFrame

load_dotenv()

logger = get_app_logger(__name__)

def main():
    pl.Config.set_tbl_cols(200)
    pl.Config.set_tbl_rows(50)

    ollama_qwen_chat = ChatOllama(model="qwen3-coder:30b",temperature=0.0)
    human_message = HumanMessage(content="Explain Encoder Self attention algorithm", name=os.getlogin())
    messages = [human_message]

    plain_response = ollama_qwen_chat.invoke("Explain Encoder Self attention algorithm")
    logger.info(plain_response)

    structured_response = ollama_qwen_chat.invoke(messages)
    logger.info(structured_response)

    tavily_search = TavilySearch(max_results=10)
    web_search_results = tavily_search.invoke("How to define Nodes, Edges, StateMessage in LangGraph with Exemplar")
    ws_results_data = web_search_results.get("results", [])
    ws_df: DataFrame = pl.DataFrame(ws_results_data)
    ws_df = ws_df.sort("score",descending=True)

    logger.info(ws_df.head())



if __name__ == '__main__':
    main()
