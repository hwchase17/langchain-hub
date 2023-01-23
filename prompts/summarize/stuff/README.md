# Description of Summarization Stuff Prompts

Prompts designed to be used in summarization chains that use the `stuff` method.

## Inputs

This is a description of the inputs that the prompt expects.

1. `text`: Text to be summarized.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains.summarize import load_summarize_chain

llm = ...
prompt = load_from_hub('summarize/stuff/<file-name>')
chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
```

