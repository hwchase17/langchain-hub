# Description of QA Stuff Prompts

Prompts to use when doing question answering with chains using the `stuff` method.


## Inputs

This is a description of the inputs that the prompt expects.

1. `context`: Context to answer the question, is usually a concatenation of all relevant documents.
2. `question`: Question to be answered.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains.question_answering import load_qa_chain

llm = ...
prompt = load_prompt('lc://prompts/qa/stuff/<file-name>')
chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
```

