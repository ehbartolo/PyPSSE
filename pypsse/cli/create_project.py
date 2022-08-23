"""CLI to create a new PyPSSE project"""

from pypsse.pypsse_project import pypsse_project
import click
import toml
import os

@click.argument(
    "path",
)

@click.option(
    "-p", "--project",
    required=True,
    help="project name",
)
@click.option(
    "-F", "--psse-project-folder",
    default=None,
    required=False,
    type=click.Path(exists=True),
    help="PSS/E project folder path",
)
@click.option(
    "-f", "--simulation-file",
    required=False,
    show_default=True,
    default="",
    help="Simulation settings toml file path",
)
@click.option(
    "-e", "--export-settings-file",
    default="",
    help="Export settings toml file path",
)
@click.option(
    "-s", "--profile-store",
    default="",
    help="Path to a valid Profiles.hdf5 file (Contains profiles for time series simulations)",
)
@click.option(
    "-m", "--profile-mapping",
    default="",
    help="Path to a valid Profile_mapping.toml file (used to map profile to PSSE elements)",
)
@click.option(
    "-a", "--autofill",
    help="Attempt to auto fill settings. (Verify manually settings file is correct)",
    is_flag=True,
    default=True,
    show_default=True,
)
@click.option(
    "-o", "--overwrite",
    help="Overwrite project is it already exists",
    is_flag=True,
    default=True,
    show_default=True,
)
@click.command()
def create_project(path=None, project=None, psse_project_folder=None, simulation_file=None, export_settings_file=None,
                   profile_store=None, profile_mapping=None, overwrite=None, autofill=None):
    """Create PyPSSE project."""
    if os.path.exists(path):
        sSettings = toml.load(simulation_file) if simulation_file else {}
        eSettings = toml.load(export_settings_file) if export_settings_file else {}
        #TODO: Validate settings
        a = pypsse_project()
        a.create(
            path,
            project,
            psse_project_folder,
            sSettings,
            eSettings,
            profile_store,
            profile_mapping,
            overwrite,
            autofill
        )
    return