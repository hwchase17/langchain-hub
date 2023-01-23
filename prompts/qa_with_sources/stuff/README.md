# Description of QA with Sources Stuff Prompts

Prompts to use in question answering with sources chains that use the `stuff` method.


## Inputs

This is a description of the inputs that the prompt expects.

1. `summaries`: Concatenated summaries of all the documents.
2. `question`: Question to be answered.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

llm = ...
prompt = load_from_hub('qa_with_sources/stuff/<file-name>')
chain = load_qa_with_sources_chain(llm, chain_type="stuff", prompt=prompt)
```

