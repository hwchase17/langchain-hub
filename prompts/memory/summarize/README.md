# Description of Summarize Memory Prompt

Prompt designed to summarize conversation history.


## Inputs

This is a description of the inputs that the prompt expects.

1. `summary`: Existing summary of conversation up to this point.
2. `new_lines`: New lines of conversation to be added into the summary.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory

llm = ...
prompt = load_from_hub('memory/summarize/<file-name>')
memory = ConversationSummaryMemory(llm=llm, prompt=prompt)
chain = ConversationChain(llm=llm, memory=memory)
```

