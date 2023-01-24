# Description of SQL Relevant Tables

Prompts designed to identify relevant SQL tables to use to answer a query.


## Inputs

This is a description of the inputs that the prompt expects.

1. `query`: Question to be answered.
2. `table_names`: Table names available as options to pull in.


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_prompt
from langchain.chains import SQLDatabaseSequentialChain

llm = ...
database = ...
prompt = load_prompt('lc://prompts/sql_query/relevant_tables/<file-name>')
chain = SQLDatabaseSequentialChain.from_llm(llm, database, decider_prompt=prompt)
```

