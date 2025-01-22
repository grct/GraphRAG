import os
from pprint import pprint

from llama_parse import LlamaParse

parser = LlamaParse(
    api_key=os.environ["LLAMA"],  # can also be set in your env as LLAMA_CLOUD_API_KEY
    num_workers=9,  # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    result_type="markdown",
    language="it",
    fast_mode=False
)

# a = parser.get_json_result("\Cartelle/Dev/Python/GraphRAG/docs/Menu/Anima Cosmica.pdf")

from llama_index.core import SimpleDirectoryReader

file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(
    "\Cartelle/Dev/Python/GraphRAG/docs/Menu", file_extractor=file_extractor
)

i = 0
for d in documents.iter_data():
    print(i)
    with open(f"{i}.txt", "w", encoding="utf-8") as file:
        for z in d:
            file.write(z.text+'\n')
    i+=1