# Description of API URL Prompts

Prompts used to construct an API URL to answer a specific question.

## Inputs

This is a description of the inputs that the prompt expects.

1. `api_docs`: The documentation for a given API.
2. `question`: The question being asked of the API.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains import APIChain

llm = ...
api_docs = ...
prompt = load_prompt('lc://prompts/api/api_url/<file-name>')
chain = APIChain.from_llm_and_api_docs(llm, api_docs, api_url_prompt=prompt)
```
