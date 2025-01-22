from langchain_core.prompts import PromptTemplate

graph_preprocess_prompt = f"""Questo documento contiene delle informazioni su Piatti, Ingredienti, Ristoranti, Tecniche, Skills e Pianeti.
Ogni ristorante ha 1 menu contentente diversi piatti e delle skills (dette anche Certificazioni). Ogni piatto é composto da ingredienti e richiede determinate tecniche per essere realizzato.
Estrai solo le informazioni utili al riempimento di un database a grafo con queste entitá secondo questo schema:

Piatti: id (se presente), nome, ingredienti, tecniche richieste
Ristoranti: nome, pianeta, skills, menu, piatti
Menu: nome, piatti, ristoranti che lo adottano
Ingredienti: nome, sostanze contenute
Tecniche: nome, skills richieste (se presente)
Skills: nome, livello
Pianeti: nome, matrice della distanza dagli altri pianeti

Rispondi solo con i valori che conosci in JSON
----------------------------
INIZIO DOCUMENTO:
"""

graph_ingest_prompt = """
Questa é una guida su come strutturare il database
Ogni ristorante ha 1 menu contentente diversi piatti e delle skills (dette anche Certificazioni).
Ogni piatto é composto da ingredienti e richiede determinate tecniche per essere realizzato.\
Nodi:

Piatti
Proprietà: id, nome
Relazioni:
HA_INGREDIENTE → verso Ingredienti
RICHIEDE_TECNICA → verso Tecniche

Ristoranti
Proprietà: nome, pianeta
Relazioni:
LOCATO_IN → verso Pianeti
HA_MENU → verso Menu
HA_PIATTO → verso Piatti
HA_SKILL → verso Skills

Menu
Proprietà: nome
Relazioni:
HA_PIATTO → verso Piatti
RICHIEDE_TECNICA → verso Tecniche
HA_INGREDIENTE → verso Ingredienti

Ingredienti
Proprietà: nome
Relazioni:
UTILIZZATO_IN → verso Piatti
HA_SOSTANZA → verso Sostanze

Sostanze:
Proprietà: nome, valori

Tecniche
Proprietà: nome
Relazioni:
RICHIESTA_DA_PIATTO → verso Piatti
RICHIEDE_SKILL → verso Skills

Skills
Proprietà: nome, livello
Relazioni:
NECESSARIO_PER → verso Tecniche
POSSEDUTO_DA → verso Ristoranti

Pianeti
Proprietà: nome, distanze (dizionario o matrice delle distanze dagli altri pianeti)
Relazioni:
HA → verso Ristoranti
DISTANTE_DA → verso altri Pianeti
----------------------------
INIZIO DOCUMENTO:
"""


CYPHER_GENERATION_TEMPLATE = """Task:Generate Cypher statement to query a graph database.
Instructions:
Query must always be case insensitive using WHERE toLower().
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Schema:
{schema}
Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

The question is:
{question} 

Important: In the generated Cypher query, the RETURN statement must explicitly only include p.codice

"""
CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
)