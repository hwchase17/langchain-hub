This prompt is a simple prompt that answers a question given some context. If the answer isn't provided in the context, then the prompt suggests the LLM to return `I don't know`.


## Usage

```
from langchain.prompts import load_from_hub
from langchain.llms import OpenAI
from langchain.prompts.loading import load_prompt

llm = OpenAI(temperature=0.9)
prompt = load_from_hub("vector_db_qa/prompt.py")
output = llm(prompt.format(context="...", question="..."))
print(output)
```

## Compatible Chains

1. `chains/vector_db_qa`