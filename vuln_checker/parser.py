import re
from typing import List, Dict
import argparse
import json

def parse_requirements(file_path: str) -> List[Dict]:
    pattern = re.compile(r'^([a-zA-Z0-9_\-]+)\s*([=<>~!]+)\s*([^\s]+)$')
    requirements = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            match = pattern.match(line)
            if match:
                package, operator, version = match.groups()
                requirements.append({
                    "version": version,
                    "operator": operator,
                    "package": {
                        "name": package,
                        "ecosystem": "PyPI"
                    }
                })
    return requirements

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse requirements file")
    parser.add_argument("file_path", help="Path to requirements.txt")
    args = parser.parse_args()

    reqs = parse_requirements(args.file_path)
    print(json.dumps(reqs, indent=2, ensure_ascii=False))