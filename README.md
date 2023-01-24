# LangChainHub

[Warning: very beta, may change drastically]

Taking inspiration from Hugging Face Hub, LangChainHub is collection of all artifacts useful for working with LangChain primitives such as prompts, chains and agents. 
The goal of this repository is to be a central resource for sharing and discovering high quality prompts, chains and agents that combine together to form complex LLM applications.

We are starting off the hub with a collection of prompts, and we look forward to the LangChain community adding to this collection. We hope to expand to chains and agents shortly.

## Contributing

Since we are using GitHub to organize this Hub, adding artifacts can best be done in one of two ways:

1. Create a fork and then open a PR against the repo.
2. Create an issue on the repo with details of the artifact you would like to add.

Each of the different types of artifacts (listed below) will have different instructions on how to upload them.
Please refer to the appropriate documentation to do so.

## 📖 Prompts

At a high level, prompts are organized by use case inside the `prompts` directory.
To load a prompt in LangChain, you should use the following code snippet:

```python
from langchain.prompts import load_prompt

prompt = load_prompt('lc://prompts/path/to/file.json')
```

In addition to prompt files themselves, each sub-directory also contains a README explaining how best to use that prompt in the appropriate LangChain chain.

For more detailed information on how prompts are organized in the Hub, and how best to upload one, please see the documentation [here](./prompts/README.md).

## 🔗 Chains

Coming soon!


## 🤖 Agents

Coming soon!
