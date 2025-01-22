from llama_index.core import SimpleDirectoryReader
from src.settings import parser, parsing_path

file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(
    parsing_path, file_extractor=file_extractor
)

i = 0
for d in documents.iter_data():
    print(i)
    with open(f"{i}.txt", "w", encoding="utf-8") as file:
        for z in d:
            file.write(z.text+'\n')
    i+=1