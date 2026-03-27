"""Generate ANTLR Python artifacts for the patched MASM grammar."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from urllib.request import urlretrieve


ROOT = Path(__file__).resolve().parent.parent
GRAMMAR_PATH = ROOT / "resources" / "grammars" / "masm" / "patched" / "Masm.g4"
OUTPUT_DIR = ROOT / "src" / "masma" / "infrastructure" / "antlr" / "generated" / "masm"
ANTLR_VERSION = "4.13.2"
ANTLR_JAR = ROOT / ".cache" / f"antlr-{ANTLR_VERSION}-complete.jar"
ANTLR_JAR_URL = f"https://www.antlr.org/download/antlr-{ANTLR_VERSION}-complete.jar"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ANTLR_JAR.parent.mkdir(parents=True, exist_ok=True)
    if not ANTLR_JAR.exists():
        urlretrieve(ANTLR_JAR_URL, ANTLR_JAR)

    generated_dir = OUTPUT_DIR / "generated_tmp"
    if generated_dir.exists():
        shutil.rmtree(generated_dir)

    subprocess.run(
        [
            "java",
            "-jar",
            str(ANTLR_JAR),
            "-Dlanguage=Python3",
            "-visitor",
            "-no-listener",
            "-o",
            str(generated_dir),
            str(GRAMMAR_PATH),
        ],
        cwd=ROOT,
        check=True,
    )

    for generated_file in generated_dir.glob("*.py"):
        target = OUTPUT_DIR / generated_file.name
        target.write_text(generated_file.read_text(encoding="utf-8"), encoding="utf-8")

    shutil.rmtree(generated_dir)
    init_path = OUTPUT_DIR / "__init__.py"
    if not init_path.exists():
        init_path.write_text('"""Generated ANTLR parser for Masm."""\n', encoding="utf-8")


if __name__ == "__main__":
    main()
