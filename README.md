# LangChainHub

Taking inspiration from Hugging Face Hub, this is collection of all artifacts useful for working with LangChain chains.
To start, this focuses on prompts.
This is intended to be a central place to upload and share prompts.
It is intended to be very community driven and we hope that people will contribute their own prompts.
Please see below for instructions on loading and uploading prompts.

## Loading

All prompts can be loaded from LangChain by specifying the desired path.
The path should be relative to the `prompts` folder here.
For example, if there is a file at `prompts/qa/basic.py`, the path you want to specify is `qa/basic.py`

Once you have that path, you can load it in the following manner:

```python
from langchain.prompts import load_from_hub
prompt = load_from_hub("qa/basic.py")
```
