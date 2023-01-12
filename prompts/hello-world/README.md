# Hello World
> A simple prompt as an example


## Configuration
- input_variables: []
  - There are no inputs
- output_parser: null
  - There is no output parsing needed
- template: 'Say hello world.'
  - Just a simple hello.
template_format: f-string
  - We use standard f-string formatting here.

## Usage

Ex:
```python3
from langchain.prompts import load_from_hub
from langchain.llms import OpenAI
from langchain.prompts.loading import load_prompt

llm = OpenAI(temperature=0.9)
# prompt = load_from_hub("hello-world/prompt.yaml")
output = llm(prompt.format())
print(output)
```
