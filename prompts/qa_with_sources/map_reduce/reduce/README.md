# Description of QA with Sources Map Reduce Prompts

This prompt enables the user to perform question answering while providing sources.
It uses the map reduce chain for doing QA. This specific prompt reduces the answer generated during the question stage.

## Inputs

This is a description of the inputs that the prompt expects.

1. `summaries`: Summaries generated during the map step.
2. `question`: Original question to be answered.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

llm = ...
prompt = load_prompt('lc://prompts/qa_with_sources/map_reduce/reduce/<file-name>')
chain = load_qa_with_sources_chain(llm, chain_type="map_reduce", combine_prompt=prompt)
```

