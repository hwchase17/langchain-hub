# Description of QA with Sources Refine Prompts

Prompts used to do question answering with sources in chains that use the `refine` method.

## Inputs

This is a description of the inputs that the prompt expects.

1. `question`: Original question to be answered.
2. `existing_answer`: Existing answer from previous documents.
3. `context_str`: New piece of context to use to refine the existing answer.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

llm = ...
prompt = load_prompt('lc://prompts/qa_with_sources/refine/<file-name>')
chain = load_qa_with_sources_chain(llm, chain_type="refine", refine_prompt=prompt)
```

