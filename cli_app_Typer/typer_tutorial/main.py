"""Module Docstring"""
from loguru import logger
import typer

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@logger.catch
def main(name: str, lastname: str = "", formal: bool = False):
    """Say hi to NAME, optionally with a --lastname. If --formal is used, say hi very formally."""
    if formal:
        typer.echo(f"Good day Ms. {name} {lastname}")
    else:
        typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
