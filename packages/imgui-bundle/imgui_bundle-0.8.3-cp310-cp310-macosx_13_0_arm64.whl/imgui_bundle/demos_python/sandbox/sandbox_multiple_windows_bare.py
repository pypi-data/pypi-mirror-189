from typing import List
from imgui_bundle import imgui, hello_imgui, immapp, ImVec2


class MySatelliteWindow:
    text_size = ImVec2
    text = "Hello"

    def __init__(self):
        self.text_size = ImVec2(300, 300)

    def gui(self):
        imgui.push_id(str(id(self)))
        imgui.text(f"Satellite {id(self)}")
        imgui.set_next_item_width(100);
        _, self.text_size.x = imgui.slider_float("size.x", self.text_size.x, 10, 600)
        imgui.set_next_item_width(100);
        _, self.text_size.y = imgui.slider_float("size.y", self.text_size.y, 10, 600)

        _, self.text = imgui.input_text_multiline("Text", self.text, self.text_size)
        imgui.pop_id()


def main():
    params = hello_imgui.RunnerParams()
    params.imgui_window_params.enable_viewports = True

    satellite_windows: List[MySatelliteWindow] = []

    def gui():
        nonlocal params
        if imgui.button("add satellite window"):
            satellite_window = MySatelliteWindow()
            satellite_windows.append(satellite_window)

        for i, satellite_window in enumerate(satellite_windows):
            window_flags = int(
                # imgui.WindowFlags_.no_move |
                # imgui.WindowFlags_.no_resize |
                imgui.WindowFlags_.no_collapse |
                # imgui.WindowFlags_.no_title_bar |
                # imgui.WindowFlags_.no_scrollbar |
                # imgui.WindowFlags_.no_scroll_with_mouse |
                imgui.WindowFlags_.always_auto_resize
            )
            imgui.begin(f"satellite {i}", None, window_flags)
            satellite_window.gui()
            imgui.end()

    params.callbacks.show_gui = gui
    hello_imgui.run(params)


if __name__ == "__main__":
    main()
