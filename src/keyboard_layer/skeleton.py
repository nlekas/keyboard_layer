"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = keyboard_layer.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""


import argparse
import sys
from argparse import Namespace
import time
from pathlib import Path

import appdirs
import cv2
from loguru import logger
from global_hotkeys import *

from keyboard_layer.layer_diagrams.diagram_models import Diagram, Series2

__author__ = "Noah Lekas"
__copyright__ = "Noah Lekas"
__license__ = "MIT"11100


is_alive: bool = True


def what_layer(n: Namespace):
    layout = Series2()
    for diagram in layout.diagrams:
        if diagram.layer == n.layer:
            logger.info(
                f"Started Displaying Layout - "
                f"Name: {diagram.name} - "
                f"Layer: {diagram.layer} - "
                f"Path: {diagram.path}"
            )
            image = cv2.imread(diagram.path)
            while True:
                cv2.imshow(f"{diagram.name}", image)
                cv2.waitKey(0)
                break
            cv2.destroyAllWindows()
            logger.info(
                f"Stop Displaying Layout - "
                f"Name: {diagram.name} - "
                f"Layer: {diagram.layer} - "
                f"Path: {diagram.path}"
            )


class StopException(Exception):
    pass


def bind(diagram: Diagram):
    def on_activate_layer_0():
        logger.info("f18 + 0 pressed")
        what_layer(Namespace(layer=0))

    def on_activate_layer_1():
        logger.info("f18 + 1 pressed")
        what_layer(Namespace(layer=1))

    def on_activate_layer_2():
        logger.info("f18 + 2 pressed")
        what_layer(Namespace(layer=2))

    def on_activate_layer_3():
        logger.info("f18 + 3 pressed")
        what_layer(Namespace(layer=3))

    def on_activate_layer_9():
        logger.info("f18 + 3 pressed")
        what_layer(Namespace(layer=9))

    def on_activate_escape():
        logger.info("f18 + q pressed")
        global is_alive
        is_alive = False

    bindings = [
        {
            "hotkey": "f18 + 0",
            "on_press_callback": None,
            "on_release_callback": on_activate_layer_0,
            "actuate_on_partial_release": False,
            # "callback_params": {"test": "testing"},
        },
        {
            "hotkey": "f18 + 1",
            "on_press_callback": None,
            "on_release_callback": on_activate_layer_1,
            "actuate_on_partial_release": False,
            # "callback_params": {"test": "testing"},
        },
        {
            "hotkey": "f18 + 2",
            "on_press_callback": None,
            "on_release_callback": on_activate_layer_2,
            "actuate_on_partial_release": False,
            # "callback_params": {"test": "testing"},
        },
        {
            "hotkey": "f18 + 3",
            "on_press_callback": None,
            "on_release_callback": on_activate_layer_3,
            "actuate_on_partial_release": False,
            # "callback_params": {"test": "testing"},
        },
        {
            "hotkey": "f18 + 9",
            "on_press_callback": None,
            "on_release_callback": on_activate_layer_9,
            "actuate_on_partial_release": False,
            # "callback_params": {"test": "testing"},
        },
        {
            "hotkey": "f18 + q",
            "on_press_callback": None,
            "on_release_callback": on_activate_escape,
            "actuate_on_partial_release": False,
            # "callback_params": {"test": "testing"},
        },
    ]

    register_hotkeys(bindings=bindings)

    start_checking_hotkeys()

    global is_alive
    is_alive = True

    while is_alive:
        time.sleep(0.01)


def keyboard_layer(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Shows layer diagrams for the A9E keyboard",
    )
    subparsers = parser.add_subparsers(required=True)

    what_layer_arg = subparsers.add_parser(
        "what_layer", help="shows the layout for a specific layer"
    )
    what_layer_arg.add_argument(
        "-l", "--layer", help="The layer number diagram you want to see.", type=int
    )
    what_layer_arg.set_defaults(func=what_layer)

    bind_hotkeys = subparsers.add_parser(
        "bind_hotkeys",
        help="binds the hotkeys to windows for use with the a9e keyboard",
    )
    bind_hotkeys.add_argument(
        "-tf", "--start_stop", help="starts hotkey binds, True starts, False stops"
    )
    bind_hotkeys.set_defaults(func=bind)

    return parser.parse_args(args)


def add_logging(src: str, log_path: Path) -> None:
    logger.add(
        log_path.joinpath(f"{src}.log"),
        rotation="1 day",
        retention="10 weeks",
        compression="zip",
    )


def main(args) -> None:
    source = args[1]
    log_path = appdirs.user_data_dir(
        appname="A9E Layout Viewer", appauthor="Noah Lekas", version="0.1", roaming=True
    )
    add_logging(src=source, log_path=Path(log_path))
    logger.info("start")
    args = keyboard_layer(args[1:])
    args.func(args)
    logger.info("end")


def run():
    main(sys.argv)


if __name__ == "__main__":
    run()
