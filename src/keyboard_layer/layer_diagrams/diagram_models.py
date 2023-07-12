from typing import List

from pkg_resources import resource_filename


class Diagram:
    def __init__(self, path: str, name: str, layer: int):
        self.path: str = path
        self.name: str = name
        self.layer: int = layer


class KeyboardDiagrams:
    def __init__(self, keyboard_name: str, diagrams: List[Diagram]):
        self.name: str = keyboard_name
        self.diagrams: List[Diagram] = diagrams


class Series1(KeyboardDiagrams):
    def __init__(self):
        super().__init__(
            keyboard_name="Atlantis 9e",
            diagrams=[
                Diagram(
                    path=resource_filename(
                        __name__,
                        "series_1/a9e_series_1_layer_0_pycharm.png",
                    ),
                    layer=0,
                    name="PyCharm",
                ),
                Diagram(
                    path=resource_filename(
                        __name__,
                        "series_1/a9e_series1_layer_1_f_keys.png",
                    ),
                    layer=1,
                    name="F-Keys",
                ),
                Diagram(
                    path=resource_filename(
                        __name__,
                        "series_1/a9e_keyboard_layout_layer_2_num_pad.png",
                    ),
                    layer=2,
                    name="Num Pad",
                ),
                Diagram(
                    path=resource_filename(
                        __name__,
                        "series_1/a9e_keyboard_layout_layer_9_rgb_keys.png",
                    ),
                    layer=9,
                    name="RGB Controls",
                ),
            ],
        )
