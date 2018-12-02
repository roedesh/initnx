# -*- coding: utf-8 -*-

"""Includes tests for the 'libt' command"""

from click.testing import CliRunner

from nxstart.cli import cli
from nxstart.tests.helpers import (APP_AUTHOR, APP_NAME, DATE_CREATED,
                                   DIRECTORY_NAME, directory_exists,
                                   file_contains_strings, file_exists,
                                   makefile_has_project_and_author_name,
                                   readme_has_project_and_author_name)


def test_libt_with_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli, ["-n", APP_NAME, "-a", APP_AUTHOR, "libt", "--clion"]
        )
        assert not result.exception
        assert result.output.endswith(
            "Successfully created the libtransistor project!\n"
        )
        assert directory_exists(DIRECTORY_NAME)
        assert file_exists("CMakeLists.txt")
        assert readme_has_project_and_author_name()
        assert makefile_has_project_and_author_name()
        assert main_c_has_valid_data()


def test_libt_without_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli, ["-n", APP_NAME, "-a", APP_AUTHOR, "libt", "--no-clion"]
        )
        assert not result.exception
        assert result.output.endswith(
            "Successfully created the libtransistor project!\n"
        )
        assert directory_exists(DIRECTORY_NAME)
        assert not file_exists("CMakeLists.txt")
        assert readme_has_project_and_author_name()
        assert makefile_has_project_and_author_name()
        assert main_c_has_valid_data()


def main_c_has_valid_data():
    return file_contains_strings("main.c", [APP_NAME, APP_AUTHOR, DATE_CREATED])
