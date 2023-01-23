from langchain.prompts.base import CommaSeparatedListOutputParser
from langchain.prompts.prompt import PromptTemplate


_DECIDER_TEMPLATE = """Given the below input question and list of potential tables, output a comma separated list of the table names that may be neccessary to answer this question.

Question: {query}

Table Names: {table_names}

Relevant Table Names:"""
PROMPT = PromptTemplate(
    input_variables=["query", "table_names"],
    template=_DECIDER_TEMPLATE,
    output_parser=CommaSeparatedListOutputParser(),
)
