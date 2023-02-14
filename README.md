# LangChainHub

[Warning: very beta, may change drastically]

[Google Form](https://forms.gle/aAhZ6nEUybdzVbYq6) for submitting new prompts.

## Introduction

Taking inspiration from Hugging Face Hub, LangChainHub is collection of all artifacts useful for working with LangChain primitives such as prompts, chains and agents. 
The goal of this repository is to be a central resource for sharing and discovering high quality prompts, chains and agents that combine together to form complex LLM applications.

We are starting off the hub with a collection of prompts, and we look forward to the LangChain community adding to this collection. We hope to expand to chains and agents shortly.

## Contributing

Since we are using GitHub to organize this Hub, adding artifacts can best be done in one of three ways:

1. Create a fork and then open a PR against the repo.
2. Create an issue on the repo with details of the artifact you would like to add.
3. Add an artifact with the appropriate Google form:
   - [Prompts](https://forms.gle/aAhZ6nEUybdzVbYq6)

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

At a high level, chains are organized by use case inside the `chains` directory.
To load a chain in LangChain, you should use the following code snippet:

```python
from langchain.chains import load_chain

chain = load_chain('lc://chains/path/to/file.json')
```

In addition to chain files themselves, each sub-directory also contains a README explaining what that chain contains.

For more detailed information on how chains are organized in the Hub, and how best to upload one, please see the documentation [here](./chains/README.md).


## 🤖 Agents

At a high level, Agents are organized by use case inside the `agents` directory.
To load a agent in LangChain, you should use the following code snippet:

```python
from langchain.agents import initialize_agent

llm = ...
tools = ...

agent = initialize_agent(tools, llm, agent="lc://agents/self-ask-with-search/agent.json")
```

In addition to agent files themselves, each sub-directory also contains a README explaining what that agent contains.

For more detailed information on how agents are organized in the Hub, and how best to upload one, please see the documentation [here](./agents/README.md).



## 👷 Agent Executors

Coming soon!
