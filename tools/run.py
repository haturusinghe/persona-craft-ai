from datetime import datetime as dt
from pathlib import Path

import click
from loguru import logger

from persona_craft_ai import settings
from pipelines import (
    digital_data_etl,
    feature_engineering,
    generate_datasets,
    end_to_end_data
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
@click.option(
    "--run-feature-engineering",
    is_flag=True,
    default=False,
    help="Whether to run the feature engineering pipeline.",
)
@click.option(
    "--run-generate-instruct-datasets",
    is_flag=True,
    default=False,
    help="Whether to run the instruct dataset generation pipeline.",
)
@click.option(
    "--run-generate-preference-datasets",
    is_flag=True,
    default=False,
    help="Whether to run the preference dataset generation pipeline.",
)
@click.option(
    "--run-end-to-end-data",
    is_flag=True,
    default=False,
    help="Whether to run all the data pipelines in one go.",
)

def main(
    no_cache: bool = False,
    run_etl: bool = False,
    etl_config_filename: str = "digital_data_person_1.yaml",
    export_settings: bool = False,
    run_feature_engineering: bool = False,
    run_generate_instruct_datasets: bool = False,
    run_generate_preference_datasets: bool = False,
    run_end_to_end_data: bool = False,
) -> None:
    assert (
        run_etl
        or export_settings
        or run_feature_engineering
        or run_generate_instruct_datasets
        or run_generate_preference_datasets
        or run_end_to_end_data
    ), "Please specify an action to run."
    root_dir = Path(__file__).resolve().parent.parent

    if export_settings:
        logger.info("Exporting settings to ZenML secrets.")
        settings.export()

    pipeline_args = {
        "enable_cache": not no_cache,
    }

    if run_end_to_end_data:
        run_args_end_to_end = {}
        pipeline_args["config_path"] = root_dir / "configs" / "end_to_end_data.yaml"
        assert pipeline_args["config_path"].exists(), f"Config file not found: {pipeline_args['config_path']}"
        pipeline_args["run_name"] = f"end_to_end_data_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        end_to_end_data.with_options(**pipeline_args)(**run_args_end_to_end)

    if run_generate_instruct_datasets:
        run_args_cd = {}
        pipeline_args["config_path"] = root_dir / "configs" / "generate_instruct_datasets.yaml"
        pipeline_args["run_name"] = f"generate_instruct_datasets_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        generate_datasets.with_options(**pipeline_args)(**run_args_cd)

    if run_generate_preference_datasets:
        run_args_cd = {}
        pipeline_args["config_path"] = root_dir / "configs" / "generate_preference_datasets.yaml"
        pipeline_args["run_name"] = f"generate_preference_datasets_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        generate_datasets.with_options(**pipeline_args)(**run_args_cd)


    if run_etl:
        run_args_etl = {}
        pipeline_args["config_path"] = root_dir / "configs" / etl_config_filename
        assert pipeline_args["config_path"].exists(), f"Config file not found: {pipeline_args['config_path']}"
        pipeline_args["run_name"] = f"digital_data_etl_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        digital_data_etl.with_options(**pipeline_args)(**run_args_etl)

    if run_feature_engineering:
        run_args_fe = {}
        pipeline_args["config_path"] = root_dir / "configs" / "feature_engineering.yaml"
        pipeline_args["run_name"] = f"feature_engineering_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        feature_engineering.with_options(**pipeline_args)(**run_args_fe)


if __name__ == "__main__":
    main()
    