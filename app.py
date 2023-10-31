from imgui.integrations.glfw import GlfwRenderer
import OpenGL.GL as gl
import glfw
import imgui
import sys

class App:
    def __init__(self, name):
        self.name = name
        self.window = impl_glfw_init()
        imgui.create_context()
        self.impl = GlfwRenderer(self.window)
    
    def appGui(self):
        changed, float_val = imgui.input_float('Type coefficient:', float_val)

    def main_loop(self, guiFunc):
        sel = 0
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            self.impl.process_inputs()
            imgui.new_frame()

            imgui.begin(self.name)

            sel = guiFunc(sel)

            imgui.end()

            gl.glClearColor(1.0, 1.0, 1.0, 1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

            imgui.render()
            self.impl.render(imgui.get_draw_data())
            glfw.swap_buffers(self.window)
    
    def run(self, guiFunc):
        self.main_loop(guiFunc)
        self.impl.shutdown()
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
