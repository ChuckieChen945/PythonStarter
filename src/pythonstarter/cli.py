"""PythonStarter CLI."""

import typer
from rich import print as rprint

from pythonstarter.component import logger, settings

app = typer.Typer()


@app.command()
def fire(name: str = "Chell") -> None:
    """Fire portal gun."""
    rprint(f"[bold red]Alert![/bold red] {name} fired [green]portal gun[/green] :boom:")
    logger.debug(f"Log settings: {settings}")
