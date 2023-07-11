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
from pathlib import Path

from loguru import logger
import sys
import cv2
import appdirs
from pkg_resources import resource_filename

from keyboard_layer import __version__

from PIL import Image

__author__ = "Noah Lekas"
__copyright__ = "Noah Lekas"
__license__ = "MIT"


def what_layer(n):
    layer_images = {
        0: resource_filename(__name__, "layer_diagrams/series_1/a9e_series_1_layer_0_pycharm.png"),
        1: resource_filename(__name__,
                                  "layer_diagrams/series_1/a9e_series1_layer_0_f_keys.png"),
        2: resource_filename(__name__,
                                  "layer_diagrams/series_1/a9e_keyboard_layout_layer_2_num_pad.png"),
        9: resource_filename(__name__,
                                  "layer_diagrams/series_1/a9e_keyboard_layout_layer_9_rgb_keys.png"),
    }
    image = cv2.imread(layer_images[n.layer])
    print(layer_images[n.layer])
    while True:
        cv2.imshow(f"Layer {n.layer}", image)
        cv2.waitKey(0)
        break
    cv2.destroyAllWindows()

def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Shows layer diagram for the A9E keyboard"
    )
    parser.add_argument(
        "-l",
        "--layer",
        help="The layer number diagram you want to see.",
        type=int
    )
    parser.set_defaults(func=what_layer)

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
    log_path = appdirs.user_data_dir(appname="A9E Layout Viewer", appauthor="Noah Lekas", version="0.1", roaming=True)
    add_logging(src=source, log_path=Path(log_path))
    logger.info("start")
    args = parse_args(args[1:])
    args.func(args)
    logger.info("end")


def run():
    main(sys.argv)


if __name__ == "__main__":
    run()