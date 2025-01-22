import os

from langchain_ibm import ChatWatsonx
from langchain_openai import ChatOpenAI
from langchain_neo4j import Neo4jGraph

llm_small = ChatOpenAI(model="gpt-4o-mini")

llm = ChatOpenAI(model="gpt-4o")

graph = Neo4jGraph()

