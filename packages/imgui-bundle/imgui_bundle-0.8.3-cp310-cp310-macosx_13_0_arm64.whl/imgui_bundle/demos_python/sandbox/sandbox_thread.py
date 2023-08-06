import threading
import time
from imgui_bundle import imgui, hello_imgui


def gui():
    imgui.text("Bloat free code")


def thread_fun():
    hello_imgui.run(gui)


def main():
    use_thread = True
    if use_thread:
        thread = threading.Thread(target=thread_fun)
        thread.start()
        # Exit the thread after several seconds
        time.sleep(6)
        hello_imgui.get_runner_params().app_shall_exit = True
        thread.join()
    else:
        thread_fun()


if __name__ == "__main__":
    main()
