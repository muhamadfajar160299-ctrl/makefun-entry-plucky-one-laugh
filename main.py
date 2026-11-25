"""Write the one-line entry to the grader's output directory.

Reads ``entry.txt`` shipped beside this script and copies it, verbatim
apart from surrounding whitespace, to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
with mode 0644. Stdlib only; no network, no secrets, no other files.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.txt"


def main():
    try:
        line = SRC.read_text(encoding="utf-8").strip()
    except OSError as exc:
        raise SystemExit(f"cannot read {SRC}: {exc}") from exc
    if not line:
        raise SystemExit("entry.txt is empty")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", ""))
    if not str(out_dir):
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.txt"
    out.write_text(line + "\n", encoding="utf-8")
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
