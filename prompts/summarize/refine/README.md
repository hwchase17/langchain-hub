# Description of Summarize Refine Prompt

Prompts designed to be used in summarization chains that use the `refine` method.


## Inputs

This is a description of the inputs that the prompt expects.

1. `existing_answer`: Existing summarization.
2. `text`: New text to be included in the summarization.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains.summarize import load_summarize_chain

llm = ...
prompt = load_from_hub('summarize/refine/<file-name>')
chain = load_summarize_chain(llm, chain_type="refine", refine_prompt=prompt)
```

