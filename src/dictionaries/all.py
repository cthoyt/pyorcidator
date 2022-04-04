import json
import os, json
from pathlib import Path

HERE = Path(__file__).parent.resolve()

dicts = {
    path.stem: json.loads(path.read_text())
    for path in HERE.glob("*.json")
}
