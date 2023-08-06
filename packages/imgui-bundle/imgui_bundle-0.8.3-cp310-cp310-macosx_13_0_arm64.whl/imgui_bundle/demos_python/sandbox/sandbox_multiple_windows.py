from typing import List
from imgui_bundle import imgui, immapp, hello_imgui, immapp, ImVec2


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
    params.imgui_window_params.config_windows_move_from_title_bar_only = True
    params.imgui_window_params.enable_viewports = True

    satellite_windows: List[MySatelliteWindow] = []
    satellite_windows_visible: List[bool] = []

    mode = 2
    def gui():
        nonlocal params
        if imgui.button("add satellite window"):
            satellite_window = MySatelliteWindow()
            satellite_windows.append(satellite_window)
            satellite_windows_visible.append(True)

            if mode==1:
                dockable_window = hello_imgui.DockableWindow()
                dockable_window.imgui_window_flags = int(
                    imgui.WindowFlags_.no_title_bar |
                    imgui.WindowFlags_.no_collapse |
                    imgui.WindowFlags_.no_scrollbar |
                    imgui.WindowFlags_.no_scroll_with_mouse |
                    imgui.WindowFlags_.always_auto_resize
                )
                dockable_window.label = f"satellite {len(params.docking_params.dockable_windows)}"
                dockable_window.gui_function = satellite_window.gui

                # (!) append will silently fail, because it is a bound std::vector...
                # params.docking_params.dockable_windows.append(dockable_window)
                # => Use `=` operator instead
                params.docking_params.dockable_windows = params.docking_params.dockable_windows + [dockable_window]

        if mode==2:
            for i, satellite_window in enumerate(satellite_windows):
                if satellite_windows_visible[i]:
                    window_flags = int(
                        imgui.WindowFlags_.no_title_bar |
                        imgui.WindowFlags_.no_collapse |
                        imgui.WindowFlags_.no_scrollbar |
                        imgui.WindowFlags_.no_scroll_with_mouse |
                        imgui.WindowFlags_.always_auto_resize
                    )
                    opened, satellite_windows_visible[i] = imgui.begin(f"satellite {i}", satellite_windows_visible[i], window_flags)
                    if opened:
                        satellite_window.gui()
                    imgui.end()

    def post_init():
        imgui.get_io().config_viewports_no_decoration = False
        imgui.get_io().config_viewports_no_auto_merge = True

    params.callbacks.show_gui = gui
    params.callbacks.post_init = post_init
    immapp.run(params)

if __name__ == "__main__":
    main()