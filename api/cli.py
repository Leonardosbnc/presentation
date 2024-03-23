import typer
from sqlmodel import Session, select

from .config import settings
from .db import engine
from .models import Info

main = typer.Typer(name="Presentation CLI", add_completion=False)


@main.command()
def shell():
    """Opens interactive shell"""
    _vars = {
        "settings": settings,
        "engine": engine,
        "select": select,
        "session": Session(engine),
        "Info": Info,
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython

        start_ipython(argv=["--ipython-dir=/tmp", "--no-banner"], user_ns=_vars)
    except ImportError:
        import code

        code.InteractiveConsole(_vars).interact()


@main.command()
def create_personal_info(value: str, category: str):
    """Create an info"""
    raw_info = dict(value=value, category=int(category))
    info_instance = Info.model_validate(raw_info)

    with Session(engine) as session:
        session.add(info_instance)
        session.commit()

    print('created info: ', value)
