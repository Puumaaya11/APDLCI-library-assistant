from graphics.GraphicsHandler import GraphicsHandler
import sys

sys.path.append(".")
sys.dont_write_bytecode = True

handler = GraphicsHandler()
config = {
    "callback" : handler.changeScreen,
    "first_name" : "Alice"
}
handler.changeScreen("STUDENT_DETAILS", config)