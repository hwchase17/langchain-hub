# Description of Vector DB Question Answering Prompt

Prompts to be used in vector DB question answering chains.


## Inputs

This is a description of the inputs that the prompt expects.

1. `context`: Documents pulled from the DB to do question answering over.
2. `question`: Question to ask of the documents.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains import VectorDBQA

llm = ...
vectorstore = ...
prompt = load_from_hub('vector_db_qa/<file-name>')
chain = VectorDBQA.from_llm(llm, prompt=prompt, vectorstore=vectorstore)
```

