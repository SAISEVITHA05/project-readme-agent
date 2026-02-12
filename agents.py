from .tools import read_project_files, save_readme
from .models import call_llm


class ReadmeGenerationAgent:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def build_prompt(self, files_content):
        file_summaries = ""
        for path, content in files_content.items():
            file_summaries += f"\n---\nFile: {path}\n{content[:2000]}\n"

        return f"""
You are an expert AI that generates professional README.md files.

Below are the project files:

{file_summaries}

Generate a complete README.md including:
1. Project Title
2. Description
3. Folder Structure
4. Installation
5. Usage
6. Features
7. Technologies Used
8. Assumptions & Limitations

Make it clear and beginner-friendly.
"""

    def generate_readme(self):
        files = read_project_files(self.folder_path)

        if not files:
            content = "# Project\n\nNo readable files found."
            save_readme(content)
            return content

        prompt = self.build_prompt(files)
        readme_content = call_llm(prompt)
        save_readme(readme_content)
        return readme_content
