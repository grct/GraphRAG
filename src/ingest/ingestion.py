from langchain_community.document_loaders import DirectoryLoader
from langchain_core.documents import Document

from src.prompts import graph_ingest_prompt, graph_preprocess_prompt
from src.settings import llm, graph, llm_small
from langchain_experimental.graph_transformers import LLMGraphTransformer


# Lista PDF parsati in txt
docs = DirectoryLoader("parsed").load()
# Txt processati in JSON con solo info rilevanti
processed_docs = []

for d in docs:
    # LLM Piccolo estrae JSON dal pdf parsato
    p = llm_small.invoke(
        # Aggiungo il prompt di pre-processing
        graph_preprocess_prompt+d.page_content.lower()
    )
    # Trasformo in doc di langchain + aggiungo prompt ingestion grafi
    processed_docs.append(
        Document(graph_ingest_prompt+p.content)
    )


print("Inizio graph")
graph_transformer = LLMGraphTransformer(
    llm=llm,
    allowed_nodes=["Piatti","Ristoranti", "Menu", "Ingredienti","Tecniche", "Skills", "Pianeti"],
    allowed_relationships=["HA_INGREDIENTE", "RICHIEDE_TECNICA", "RICHIEDE_SKILL", "HA_PIATTO", "HA_MENU", "HA_SKILL", "SI_TROVA_SU", "HA_SOSTANZA", "RICHIESTA_DA_PIATTO"],
)


for d in processed_docs:
    try:
        graph_documents = graph_transformer.convert_to_graph_documents(documents=[d])
        graph.add_graph_documents(graph_documents)
        print("Graph ingested")
    except:
        print(f"Errore: {d.id}")

