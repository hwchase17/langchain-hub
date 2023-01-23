# Description of LLM Math Chain

Prompt designed to optionally output iPython syntax to be run in order to better answer math questions.


## Inputs

This is a description of the inputs that the prompt expects.

1. `question`: User question to be answered.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains import LLMMathChain

llm = ...
prompt = load_from_hub('llm_math/<file-name>')
chain = LLMMathChain(llm=llm, prompt=prompt)
```

