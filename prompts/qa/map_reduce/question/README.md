# Description of QA Map Reduce Prompt

Prompts designed to be used in the initial question (map) step of a map-reduce chain to do question answering over a series of documents.


## Inputs

This is a description of the inputs that the prompt expects.

1. `context`: The document to be asking a question over.
2. `question`: The question being asked of the document.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains.question_answering import load_qa_chain

llm = ...
prompt = load_from_hub('qa/map_reduce/question/<file-name>')
chain = load_qa_chain(llm, chain_type="map_reduce", question_prompt=prompt)
```

