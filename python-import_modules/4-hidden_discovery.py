#!/usr/bin/python3
"""Print names from hidden_4 that do not start with __."""

from pathlib import Path
from importlib.machinery import SourcelessFileLoader
from importlib.util import module_from_spec, spec_from_loader


def main():
    """Entry point for script execution."""
    script_dir = Path(__file__).resolve().parent
    candidates = (
        script_dir / "hidden_4.pyc",
        Path.cwd() / "hidden_4.pyc",
        Path("/tmp/hidden_4.pyc"),
    )

    for candidate in candidates:
        if candidate.exists():
            loader = SourcelessFileLoader("hidden_4", str(candidate))
            break
    else:
        return

    spec = spec_from_loader(loader.name, loader)
    hidden_4 = module_from_spec(spec)
    loader.exec_module(hidden_4)

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    main()
