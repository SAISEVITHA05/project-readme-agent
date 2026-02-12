import os
import re


def call_llm(prompt):
    files = re.findall(r"File:\s*(.+)", prompt)
    clean_files = [os.path.basename(f) for f in files]

    project_name = "Float Lab Project"

    folder_structure = "\n".join(f"- {f}" for f in clean_files)

    return (
        f"# {project_name}\n\n"
        "## Description\n"
        "This project contains C programs designed to test and analyze bit-level and floating-point\n"
        "operations. It appears to be an academic lab assignment focused on low-level programming\n"
        "and systems understanding.\n\n"
        "This README was generated automatically by an AI agent.\n\n"
        "## Folder Structure\n"
        f"{folder_structure}\n\n"
        "## Installation\n"
        "Ensure you have a C compiler such as gcc installed.\n\n"
        "To compile:\n"
        "    make\n\n"
        "## Usage\n"
        "After compiling, run:\n"
        "    ./btest\n"
        "    ./fshow\n"
        "    ./ishow\n\n"
        "## Features\n"
        "- Bit manipulation testing\n"
        "- Floating-point representation analysis\n"
        "- Makefile-based build system\n\n"
        "## Technologies Used\n"
        "- C Programming Language\n"
        "- GNU Make\n"
        "- Command Line Tools\n\n"
        "## Assumptions & Limitations\n"
        "- Designed for academic lab purposes\n"
        "- README generated using heuristic analysis (offline mode)\n"
    )
