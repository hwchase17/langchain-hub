# RouterChain

## Description

The custom chain seeks to provide a reverse proxy LLM based model to route and dispatch requests to specialized downstream models based on vector store match. 
The chain includes support for memory and threshold management in case of hallucinations. 

## Chain type

RouterChain

## Input Variables

question: Any question that can be answered by one or more downstream chains

### Reference

See [LangchainModelRouter](https://github.com/keshy/Langchain_model_router) full sample of how this can be used here