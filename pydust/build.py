import sys

from pydust import buildzig


def build():
    """The main entry point from Poetry's build script."""
    buildzig.zig_build(["install", f"-Dpython-exe={sys.executable}"])
