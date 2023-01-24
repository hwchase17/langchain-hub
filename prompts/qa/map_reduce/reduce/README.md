# Description of QA Map Reduce Prompt

Prompts designed to be used to reduce the answers generated during the map step.


## Inputs

This is a description of the inputs that the prompt expects.

1. `summaries`: Summaries generated during the map step.
2. `question`: Original question to be answered.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains.question_answering import load_qa_chain

llm = ...
prompt = load_prompt('lc://prompts/qa/map_reduce/reduce/<file-name>')
chain = load_qa_chain(llm, chain_type="map_reduce", combine_prompt=prompt)
```

