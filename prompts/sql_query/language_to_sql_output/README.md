# Description of Language-To-SQL Prompts

Prompts designed to convert language to relevant SQL query to execute.


## Inputs

This is a description of the inputs that the prompt expects.

1. `input`: Question to be answered.
2. `table_info`: Relevant information about the tables present in the schema.
3. `dialect`: Dialect of SQL to write the query in
4. `top_k`: Number of rows to return for most queries (used to avoid returning too much and overloading the context window).


## Usage

Below is a code snippet for how to use the prompt.

```python
from langchain.prompts import load_from_hub
from langchain.chains import SQLDatabaseChain

llm = ...
database = ...
prompt = load_from_hub('sql_query/language_to_sql_output/<file-name>')
chain = SQLDatabaseChain(llm=llm, database=database, prompt=prompt)
```

