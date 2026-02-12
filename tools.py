import os
from .config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE, README_OUTPUT_FILE


def is_valid_file(file_path):
    return (
        os.path.isfile(file_path)
        and os.path.getsize(file_path) <= MAX_FILE_SIZE
        and os.path.splitext(file_path)[1] in ALLOWED_EXTENSIONS
    )


def read_project_files(folder_path):
    project_files = {}

    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            if is_valid_file(full_path):
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        if content:
                            project_files[full_path] = content
                except Exception:
                    project_files[full_path] = "[Could not read file]"

    return project_files


def save_readme(content):
    with open(README_OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)
