# Description of QA Refine Prompts

Prompts designed to be used to refine original answers during question answering chains using the `refine` method.


## Inputs

This is a description of the inputs that the prompt expects.

1. `question`: Original question to be answered.
2. `existing_answer`: Existing answer from previous documents.
3. `context_str`: New piece of context to use to refine the existing answer.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains.question_answering import load_qa_chain

llm = ...
prompt = load_prompt('lc://prompts/qa/refine/<file-name>')
chain = load_qa_chain(llm, chain_type="refine", refine_prompt=prompt)
```

