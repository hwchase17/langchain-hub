# Description of Conversation Prompt

Prompt designed to simulate having a conversation and allow for a conversational response to be returned.


## Inputs

This is a description of the inputs that the prompt expects.

1. `history`: History of the conversation up to that point.
2. `input`: New user input.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains import ConversationChain

llm = ...
prompt = load_prompt('lc://prompts/conversation/<file-name>')
chain = ConversationChain(llm=llm, prompt=prompt)
```

