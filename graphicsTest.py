from graphics.GraphicsHandler import GraphicsHandler
import sys

sys.path.append(".")
sys.dont_write_bytecode = True

handler = GraphicsHandler()
config = {
    "callback" : handler.changeScreen
}
handler.changeScreen("MAIN_MENU", config)