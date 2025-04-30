from datetime import datetime as dt
from pathlib import Path

import click
from loguru import logger

from persona_craft_ai import settings
from pipelines import (
    digital_data_etl
)

@click.command(
    help="""
Welcome to the Persona Craft AI CLI!
This CLI tool is designed to help you run the Persona Craft AI application with ease.
    """
)

@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable caching for the pipeline run.",
)
@click.option(
    "--run-etl",
    is_flag=True,
    default=False,
    help="Whether to run the ETL pipeline.",
)
@click.option(
    "--etl-config-filename",
    default="digital_data_person_1.yaml",
    help="Filename of the ETL config file.",
)
@click.option(
    "--export-settings",
    is_flag=True,
    default=False,
    help="Whether to export your settings to ZenML or not.",
)

def main(
    no_cache: bool = False,
    run_etl: bool = False,
    etl_config_filename: str = "digital_data_person_1.yaml",
    export_settings: bool = False,
) -> None:
    assert (
        run_etl
        or export_settings
    ), "Please specify an action to run."
    root_dir = Path(__file__).resolve().parent.parent

    if export_settings:
        logger.info("Exporting settings to ZenML secrets.")
        settings.export()

    pipeline_args = {
        "enable_cache": not no_cache,
    }


    if run_etl:
        run_args_etl = {}
        pipeline_args["config_path"] = root_dir / "configs" / etl_config_filename
        assert pipeline_args["config_path"].exists(), f"Config file not found: {pipeline_args['config_path']}"
        pipeline_args["run_name"] = f"digital_data_etl_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        digital_data_etl.with_options(**pipeline_args)(**run_args_etl)


if __name__ == "__main__":
    main()
    