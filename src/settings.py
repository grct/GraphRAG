import os

from langchain_ibm import ChatWatsonx
from langchain_openai import ChatOpenAI
from langchain_neo4j import Neo4jGraph
from llama_parse import LlamaParse

llm_small = ChatOpenAI(model="gpt-4o-mini")
llm = ChatOpenAI(model="gpt-4o")

parser = LlamaParse(
    api_key=os.environ["LLAMA"],  # can also be set in your env as LLAMA_CLOUD_API_KEY
    num_workers=9,  # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    result_type="markdown",
    language="it",
    fast_mode=False
)
parsing_path = "\Cartelle/Dev/Python/GraphRAG/docs/Menu"

graph = Neo4jGraph()


