# SPDX-FileCopyrightText: 2023 Alex Lemna <git@alexanderlemna.com>
#
# SPDX-License-Identifier: MIT

import enum
import inspect
import logging
import shutil
from enum import Enum
from logging import DEBUG, INFO, WARN, Logger, getLevelName
from pathlib import Path

#
# TODO TODO TODO TODO TODO
# Explain how this file is organized.
#


class NextVersion(Enum):
    UNKNOWN = 0
    MAJOR = enum.auto()
    MINOR = enum.auto()
    PATCH = enum.auto()


#
# ---------------------------------------------------------
# =========================================================
#                        UTILITIES
# =========================================================
# ---------------------------------------------------------
#


def get_logger(verbosity: int) -> Logger:
    """Returns a `logging.Logger` (Python's built-in logger) configured
    just how I like it.

    The logging level will be WARN by default, INFO if `verbosity == 1`
    (aka `-v`), and DEBUG if `verbosity >= 2` (aka`-vv` or `-vvvvvvvv`)."""

    loglevel = DEBUG if verbosity >= 2 else INFO if verbosity == 1 else WARN

    # We want to include the name of the top-level function inside the logger's
    # name, which means we want the 'function' attribute of the second frame
    # on the stack.
    top_function_frame = inspect.stack()[1]  # 1 is 2 because Python is zero-indexed
    top_function = top_function_frame.function

    # create logger
    # -------------
    # This recipe direct from
    #   https://docs.python.org/3/howto/logging.html#configuring-logging
    logger = logging.getLogger(f"{__name__}:{top_function}")
    logger.setLevel(loglevel)
    # create console handler and set level
    ch = logging.StreamHandler()
    ch.setLevel(DEBUG)
    # create formatter
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)

    logger.info(f"displaying logs with level {getLevelName(logger.level)} or higher")
    return logger


def get_version_current():
    """Returns the current local version using `auldcommons.__version__`."""
    try:
        import auldcommons

        return auldcommons.__version__

    # These errors can happen, and I'm explicitly calling them
    # out as possibilities below and then *not* handling them
    # because I want my higher-level functions to deal with that
    # instead.
    #
    # I dunno if it's the best design choice, but I'm documenting
    # it here so I don't forget I did it and I can reevaluate
    # later on.
    except (ImportError, AttributeError) as error:
        raise error


# Each of the get_version_next_* functions should include flags for
#   --version


def get_version_next_alpha():
    ...


def get_version_next_beta():
    ...


def get_version_next_rc():
    ...
    # check if


def get_version_next_final():
    ...


def get_version_next_post():
    ...


def remove_path(path: Path, logger: logging.Logger):
    """Removes a file or directory, if it exists. Logs the result
    either way."""
    if path.exists() is False:
        logger.debug(f"tried removing {path} but it does not exist")
    elif path.is_dir():
        logger.info(f"removing {path}")
        shutil.rmtree(path)
    elif path.is_file():
        logger.info(f"removing {path}")
        path.unlink()
    else:
        logger.error(f"could not determine how to remove {path}")


#
# ---------------------------------------------------------
# =========================================================
#                          TASKS
# =========================================================
# ---------------------------------------------------------
#


from invoke.tasks import task


@task(incrementable=["verbose"])
def cleanup_build_artifacts(context, verbose=0):
    """NOT YET IMPLEMENTED"""
    logger = get_logger(verbose)
    # TODO: remove *.egg-info

    base_dirs_to_remove = ["build", "dist"]
    this_dir = Path(__file__).parent
    for subdir in base_dirs_to_remove:
        dir = this_dir / subdir
        remove_path(dir, logger=logger)


@task(incrementable=["verbose"])
def cleanup_bytecode(context, verbose=0):
    """NOT YET IMPLEMENTED"""
    logger = get_logger(verbose)
    # remove __pycache__


@task(incrementable=["verbose"])
def cleanup_test_reports(context, verbose=0):
    """NOT YET IMPLEMENTED"""
    logger = get_logger(verbose)
    # remove pytest_cache
    # remove .coverage


@task(incrementable=["verbose"])
def show_current_version(context, verbose=0):
    """Shows the current local version using auldcommons.__version__."""
    logger = get_logger(verbose)

    try:
        current_version = get_version_current()
    except ImportError as e:
        logger.error(
            "Could not import auldcommons to determine version "
            + "due to ImportError: {e}."
        )
    except AttributeError as e:
        logger.error("No version string (auldcommons.__version__) exists.")
    else:
        print(current_version)


#
# ---------------------------------------------------------
# =========================================================
#             INVOKE's COMMAND LINE INTERFACE
# =========================================================
# ---------------------------------------------------------
#
# check.docstrings
# check.formatting
# check.reuse
#
# devtools.ensure
# devtools.list --updates-available
#
# project.clean
# project.install --editable
# project.setup
#
# release.alpha --real --dry-run --verbose --version VERSION
# release.beta --real --dry-run --verbose --version VERSION
# release.rc --real --dry-run --verbose --version VERSION
# release.final --real --dry-run --verbose --version VERSION
# release.post --real --dry-run --verbose --version VERSION
#
# show.coverage
# show.docstrings
# show.version.current
# show.version.next --alpha --beta --rc --final --post --version VERSION
#
# test.docstrings
# test.pytest --coverage=True (default)
# test.nox
#

from invoke.collection import Collection

# namespace = Collection()

# namespace.add_task(clean)

# version_cmds = Collection("version")
# version_cmds.add_task(version_current, "show")
# namespace.add_collection(version_cmds)
