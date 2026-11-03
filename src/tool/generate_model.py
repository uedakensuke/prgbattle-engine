import argparse
import subprocess
import os
from pathlib import Path

def generate_model(input_path: str):
    dir = os.path.dirname(input_path)
    fname = os.path.basename(input_path)
    output_path = os.path.join(dir, os.path.splitext(fname)[0] + ".py")
    subprocess.run(
        [
            "datamodel-codegen",
            "--input",
            input_path,
            "--input-file-type",
            "jsonschema",
            "--output",
            output_path,
            "--formatters",
            "black",
            "isort",
        ],
        check=True,
    )
    print("created:", output_path)


def main():
    dir = os.path.dirname(__file__)
    default_input = os.path.join(dir, "..", "..", "schema", "schema.json")
    default_input_path = Path(default_input).resolve()

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default=default_input_path)
    args = parser.parse_args()
    generate_model(args.input)


if __name__ == "__main__":
    main()
