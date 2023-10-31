import app
import imgui
import waveprops as wp

def guiFunc():
    imgui.text("Hello World!")

def combotest(selected):
    items = ["AAAA", "BBBB", "CCCC", "DDDD"]
    if imgui.begin_combo("combo", items[selected]):
        for i, item in enumerate(items):
            is_selected = (i == selected)
            if imgui.selectable(item, is_selected)[0]:
                selected = i

            # Set the initial focus when opening the combo (scrolling + keyboard navigation focus)
            if is_selected:
                imgui.set_item_default_focus()

        imgui.end_combo()
    imgui.text(str(items[selected]))
    return selected


def main():
    myApp = app.App("Propagación")
    myApp.run(combotest)


if __name__ == "__main__":
    main()
