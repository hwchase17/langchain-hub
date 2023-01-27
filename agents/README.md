# Agents

This directory covers loading and uploading of agents. 
Each sub-directory covers a different agent, and has not only the serialized agent but also a README file describing that agent.

## Loading

All agents can be loaded from LangChain by specifying the desired path, and adding the `lc://` prefix. The path should be relative to the `langchain-hub` repo.

For example, to load the agent at the path `langchain-hub/agents/self-ask-with-search/agent.json`, the path you want to specify is `lc://agents/self-ask-with-search/agent.json`

Once you have that path, you can load it in the following manner:

```python
from langchain.agents import initialize_agent

llm = ...
tools = ...

agent = initialize_agent(tools, llm, agent_path="lc://agents/self-ask-with-search/agent.json")
```

## Uploading

To upload an agent to the LangChainHub, you must upload 2 files:
1. The agent. There are 2 supported file formats for agents: `json` and `yaml`. 
2. Associated README file for the agent. This provides a high level description of the agent.


### Supported file formats

#### `json`
To get a properly formatted json file, if you have an agent in memory in Python you can run:
```python
agent.save_agent("file_name.json")
```

Replace `"file_name"` with the desired name of the file.

#### `yaml`
To get a properly formatted yaml file, if you have an agent in memory in Python you can run:
```python
agent.save_agent("file_name.yaml")
```

Replace `"file_name"` with the desired name of the file.
