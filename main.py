from array import array
from imgui.integrations.glfw import GlfwRenderer
import waveprops as wp
import OpenGL.GL as gl
import glfw
import imgui
import sys

def main():
    # Init
    window = impl_glfw_init()
    imgui.create_context()
    impl = GlfwRenderer(window)

    method_sel = 8
    opt_sel = 0
    f = 450
    hm = 1.5
    hb = 30
    pltf = 0.01
    plot_values = array("f", [wp.method_func[wp.methods[method_sel]](wp.method_opts[wp.methods[method_sel]][opt_sel], f, hm, hb, d*pltf) for d in range(1, 200)]) #opt, f, hm, hb, d
    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()

        imgui.new_frame()

        imgui.begin("Plot example")


        imgui.plot_lines(
                wp.methods[method_sel],
                plot_values,
                overlay_text="A(d)",
                graph_size=(0, 400),
        )

        if imgui.begin_combo("Método", wp.methods[method_sel]):
            for i, item in enumerate(wp.methods):
                m_is_selected = (i == method_sel)
                if imgui.selectable(item, m_is_selected)[0]:
                    method_sel = i
                    opt_sel = 0
                if m_is_selected:
                    imgui.set_item_default_focus()
            imgui.end_combo()

        if imgui.begin_combo("Región", wp.method_opts[wp.methods[method_sel]][opt_sel]):
            for i, item in enumerate(wp.method_opts[wp.methods[method_sel]]):
                o_is_selected = (i == opt_sel)
                if imgui.selectable(item, o_is_selected)[0]:
                    opt_sel = i
                if o_is_selected:
                    imgui.set_item_default_focus()
            imgui.end_combo()

        changed_f, f = imgui.input_int("Frequency", f)
        chagend_hm, hm = imgui.input_float("Altura Mobil", hm)
        chagend_hb, hb = imgui.input_float("Altura Antena", hb)

        plot_values = array("f", [wp.method_func[wp.methods[method_sel]](wp.method_opts[wp.methods[method_sel]][opt_sel], f, hm, hb, d*pltf) for d in range(1, 200)]) #opt, f, hm, hb, d

        imgui.end()

        gl.glClearColor(1.0, 1.0, 1.0, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    impl.shutdown()
    glfw.terminate()

def impl_glfw_init():
    width, height = 1280, 720
    window_name = "minimal ImGui/GLFW3 example"

    if not glfw.init():
        print("Could not initialize OpenGL context")
        sys.exit(1)

    # OS X supports only forward-compatible core profiles from 3.2
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(int(width), int(height), window_name, None, None)
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        sys.exit(1)

    return window

if __name__ == "__main__":
    main()
