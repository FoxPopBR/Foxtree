# tree.py
import pathlib
from modules.treemaker import TreeGenerator

def main():
    root_dir = pathlib.Path(__file__).resolve().parent
    generator = TreeGenerator(root_dir)
    tree = generator.generate_tree()

    with open("showtree.md", "w", encoding="utf-8") as file:
        file.write("<pre>\n")  # Adiciona a tag de início <pre>
        for line in tree:
            file.write(f"{line}\n")
        file.write("</pre>")  # Adiciona a tag de fim </pre>

if __name__ == "__main__":
    main()
