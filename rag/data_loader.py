# rag/data_loader.py

from pathlib import Path
import json


def load_documents(data_dir="data"):
    """
    Recursively load all markdown and json files
    from the data directory.
    """

    documents = []

    # Traverse all files recursively
    for file_path in Path(data_dir).rglob("*"):

        # Skip directories
        if file_path.is_dir():
            continue

        # -----------------------------
        # Markdown Files
        # -----------------------------
        if file_path.suffix == ".md":

            try:
                content = file_path.read_text(
                    encoding="utf-8"
                )

                documents.append({
                    "source": str(file_path),
                    "type": "markdown",
                    "content": content
                })

                print(f"Loaded Markdown: {file_path}")

            except Exception as e:
                print(f"Error loading {file_path}")
                print(e)

        # -----------------------------
        # JSON Files
        # -----------------------------
        elif file_path.suffix == ".json":

            try:
                content = json.loads(
                    file_path.read_text(
                        encoding="utf-8"
                    )
                )

                documents.append({
                    "source": str(file_path),
                    "type": "json",
                    "content": content
                })

                print(f"Loaded JSON: {file_path}")

            except Exception as e:
                print(f"Error loading {file_path}")
                print(e)

    return documents
