from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich import print as rprint
from rich.text import Text

console = Console()

def print_success(message: str):
    console.print(f"[bold green]✅ {message}[/bold green]")

def print_error(message: str):
    console.print(f"[bold red]❌ {message}[/bold red]")

def print_warning(message: str):
    console.print(f"[bold yellow]⚠️ {message}[/bold yellow]")

def print_info(message: str):
    console.print(f"[bold cyan]{message}[/bold cyan]")

def print_header(title: str):
    console.print(Panel(f"[bold magenta]{title}[/bold magenta]", expand=True))