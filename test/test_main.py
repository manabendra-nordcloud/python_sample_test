import importlib.util
import runpy
from pathlib import Path
import builtins
import pytest


def load_main_module():
    """Dynamically load the `src/main.py` module for testing."""
    path = Path(__file__).resolve().parents[1] / "src" / "main.py"
    spec = importlib.util.spec_from_file_location("main_module_for_test", str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_add_ints():
    main = load_main_module()
    assert main.add(2, 3) == 5


def test_add_floats():
    main = load_main_module()
    assert main.add(1.2, 2.3) == pytest.approx(3.5)


def test_add_negative():
    main = load_main_module()
    assert main.add(-1, 1) == 0


def test_cli(monkeypatch, capsys):
    # Simulate user entering two numbers via input()
    inputs = iter(["2", "3"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))

    # Run the script as __main__ and capture stdout
    here = Path(__file__).resolve().parent
    main_path = str(here.parent / "src" / "main.py")
    runpy.run_path(main_path, run_name="__main__")

    captured = capsys.readouterr()
    assert "Sum: 5.0" in captured.out
