#!/usr/bin/python3
"""Print names from hidden_4 that do not start with __."""

from importlib.machinery import SourcelessFileLoader
from importlib.util import module_from_spec, spec_from_loader


def main():
    """Entry point for script execution."""
    loader = SourcelessFileLoader("hidden_4", "/tmp/hidden_4.pyc")
    spec = spec_from_loader(loader.name, loader)
    hidden_4 = module_from_spec(spec)
    loader.exec_module(hidden_4)

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    main()
