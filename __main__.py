import sys
from .agents import ReadmeGenerationAgent


def main():
    if len(sys.argv) != 2:
        print("Usage: py -m project_readme_agent <project_folder_path>")
        return

    folder_path = sys.argv[1]
    agent = ReadmeGenerationAgent(folder_path)
    agent.generate_readme()

    print("\nREADME.md generated successfully!\n")


if __name__ == "__main__":
    main()
