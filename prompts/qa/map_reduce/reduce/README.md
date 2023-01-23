<!-- Add a template for READMEs that capture the utility of prompts -->

# Description of {{prompt}}

{{High level text description of the prompt, including use cases.}}

## Compatible Chains

Below is a list of chains we expect this prompt to be compatible with.

1. {{Chain Name}}: {{Path to chain in module}}
2. ...

## Inputs

This is a description of the inputs that the prompt expects.

1. {{input_var}}: {{Description}}
2. ...


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains.question_answering import load_qa_chain

llm = ...
prompt = load_from_hub('qa/map_reduce/reduce/<file-name>')
chain = load_qa_chain(llm, chain_type="map_reduce", combine_prompt=prompt)
```

