# Prompts

This directory covers loading and uploading of prompts. 
Each sub-directory covers a different use case, and has not only relevant prompts for that use case but also a README file describing how to best use that prompt.

## Loading

All prompts can be loaded from LangChain by specifying the desired path, and adding the `lc://` prefix. The path should be relative to the `langchain-hub` repo.

For example, to load the prompt at the path `langchain-hub/prompts/qa/stuff/basic/prompt.yaml`, the path you want to specify is `lc://prompts/qa/stuff/basic/prompt.yaml`

Once you have that path, you can load it in the following manner:

```python
from langchain.prompts import load_prompt

prompt = load_prompt('lc://prompts/qa/stuff/basic/prompt.yaml')
```

## Uploading

To upload a prompt to the LangChainHub, you must upload 2 files:
1. The prompt. There are 3 supported file formats for prompts: `json`, `yaml`, and `python`. The suggested options are `json` and `yaml`, but we provide `python` as an option for more flexibility. Please see the below sections for instructions for uploading each format.
2. Associated README file for the prompt. This provides a high level description of the prompt, usage patterns of the prompt and chains that the prompt is compatible with. For more details, check out langchain-hub/readme_template.
   If you are uploading a prompt to an existing directory, it should already have a README file and so this should not be necessary.


The prompts on the hub are organized by use case. The use cases are reflected in the directory structure and names, and each separate directory represents a different use case. You should upload your prompt file to a folder in the appropriate use case section.


If adding a prompt to an existing use case folder, then make sure that the prompt:
1. services the same use case as the existing prompt(s) in that folder, and
2. has the same inputs as the existing prompt(s).

A litmus test to make sure that multiple prompts belong in the same folder: the existing README file for that folder should also apply to the new prompt being added.


### Supported file formats

#### `json`
To get a properly formatted json file, if you have prompt in memory in Python you can run:
```python
prompt.save("file_name.json")
```

Replace `"file_name"` with the desired name of the file.

#### `yaml`
To get a properly formatted yaml file, if you have prompt in memory in Python you can run:
```python
prompt.save("file_name.yaml")
```

Replace `"file_name"` with the desired name of the file.


#### `python`
To get a properly formatted Python file, you should upload a Python file that exposes a `PROMPT` variable.
This is the variable that will be loaded.
This variable should be an instance of a subclass of BasePromptTemplate in LangChain.
