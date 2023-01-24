# Description of Summarize Map Reduce Prompts

Prompts designed to be used the in the map step of chains doing summarization with `map-reduce` method.


## Inputs

This is a description of the inputs that the prompt expects.

1. `text`: Text to be summarized.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains.summarize import load_summarize_chain

llm = ...
prompt = load_prompt('lc://prompts/summarize/map_reduce/map/<file-name>')
chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt=prompt)
```

