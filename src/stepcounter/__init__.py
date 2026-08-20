"""StepCounter: Logs daily step counts and prints weekly averages and goals."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]