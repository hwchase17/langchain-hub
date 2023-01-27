# Chains

This directory covers loading and uploading of chains. 
Each sub-directory covers a different chain, and has not only the serialized agent but also a README file describing that agent.

## Loading

All chains can be loaded from LangChain by specifying the desired path, and adding the `lc://` prefix. The path should be relative to the `langchain-hub` repo.

For example, to load the chain at the path `langchain-hub/chains/hello-world/chain.json`, the path you want to specify is `lc://chains/hello-world/chain.json`

Once you have that path, you can load it in the following manner:

```python
from langchain.chains import load_chain

chain = load_chain("lc://chains/hello-world/chain.json")
```

Extra arguments (kwargs) may be needed depending on the type of chain.

## Uploading

To upload an chain to the LangChainHub, you must upload 2 files:
1. The chain. There are 2 supported file formats for agents: `json` and `yaml`. 
2. Associated README file for the chain. This provides a high level description of the chain.


### Supported file formats

#### `json`
To get a properly formatted json file, if you have a chain in memory in Python you can run:
```python
chain.save("file_name.json")
```

Replace `"file_name"` with the desired name of the file.

#### `yaml`
To get a properly formatted yaml file, if you have a chain in memory in Python you can run:
```python
chain.save("file_name.yaml")
```

Replace `"file_name"` with the desired name of the file.
