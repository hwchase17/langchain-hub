# Description of API Response Prompts

Prompts used to convert the result of an API into natural language.

## Inputs

This is a description of the inputs that the prompt expects.

1. `api_docs`: Docs for the API being hit.
2. `question`: Question to be answered.
3. `api_url`: URL that was hit.
4. `api_response`: The response returned from hitting said URL.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains import APIChain

llm = ...
api_docs = ...
prompt = load_from_hub('api/api_response/<file-name>')
chain = APIChain.from_llm_and_api_docs(llm, api_docs, api_response_prompt=prompt)
```

