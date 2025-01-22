from langchain_neo4j import GraphCypherQAChain
from src.prompts import CYPHER_GENERATION_PROMPT
from src.settings import llm_small, graph
import pandas as pd

chain = GraphCypherQAChain.from_llm(
    llm_small, graph=graph, verbose=True, allow_dangerous_requests=True, return_direct=True, cypher_prompt=CYPHER_GENERATION_PROMPT
)

input_file = '../docs/domande.csv'
df = pd.read_csv(input_file)

df['row_id'] = range(1, len(df) + 1)

def genera_risposta(domanda):
    print(domanda)
    try:
        response = chain.invoke({"query": domanda}).get("result")
        print(response)
        codici = ",".join([str(c.get('p.codice')) for c in response])
        return codici
    except:
        return ""

df['result'] = df['domanda'].apply(genera_risposta)
output_df = df[['row_id', 'result']]
output_file = '../docs/risultati.csv'
output_df.to_csv(output_file, index=False)  # quoting=1 per includere doppi apici

