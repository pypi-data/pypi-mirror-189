import typer

import nef_pipelines
from nef_pipelines import nef_app

app = typer.Typer()
import_app = typer.Typer()

if nef_app.app:
    nef_app.app.add_typer(app, name="pdbx", help="-  read pdb [sequences]")

    app.add_typer(import_app, name="import", help="-  import pdb [sequences]")

    # import of specific importers must be after app creation to avoid circular imports
    import nef_pipelines.transcoders.pdbx.importers.sequence  # noqa: F401
