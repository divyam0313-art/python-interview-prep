"""Loads every questions/*/solution.py and exposes their public names."""
import importlib.util
import pathlib

_root = pathlib.Path(__file__).resolve().parent.parent / "questions"
for _file in sorted(_root.glob("*/solution.py")):
    _spec = importlib.util.spec_from_file_location(_file.parent.name, _file)
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    globals().update({k: v for k, v in vars(_mod).items() if not k.startswith("__")})
