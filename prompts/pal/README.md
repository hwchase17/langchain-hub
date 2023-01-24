# Description of PAL Prompts

Prompts to be used with the [PAL](https://arxiv.org/pdf/2211.10435.pdf) chain. 
These prompts should convert a natural language problem into a series of code snippets to be run to give an answer.


## Inputs

This is a description of the inputs that the prompt expects.

1. `question`: The question to be answered.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains import PALChain

llm = ...
stop = ...
get_answer_expr = ...
prompt = load_prompt('lc://prompts/pal/<file-name>')
chain = PALChain(llm=llm, prompt=prompt, stop=stop, get_answer_expr=get_answer_expr)
```

