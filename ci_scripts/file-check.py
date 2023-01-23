from pathlib import Path

from langchain.prompts import load_prompt

BASE_FOLDER = Path("prompts")
folders = BASE_FOLDER.glob("**")


def check_files(files):
    file_names = [f.name for f in files]
    if "README.md" not in file_names:
        raise ValueError(f"Expected to find a README.md file, but found {files}")
    other_files = [file for file in files if file.name != "README.md"]
    for other_file in other_files:
        if other_file.suffix in (".json", ".yaml"):
            load_prompt(other_file)
    # TODO: testing for python files


def check_all_folders():
    for folder in folders:
        folder_path = Path(folder)
        files = [x for x in folder_path.iterdir() if x.is_file()]
        if len(files) > 0:
            try:
                check_files(files)
            except Exception as e:
                raise ValueError(f"Found error with {folder}: {e}")


if __name__ == "__main__":
    check_all_folders()
