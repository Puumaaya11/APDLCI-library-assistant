from graphics.GraphicsHandler import GraphicsHandler
import sys

sys.path.append(".")
sys.dont_write_bytecode = True

handler = GraphicsHandler()
handler.screenList["LOGIN"].credentialManager.login("john.smith", "GU2498")
config = {
    "callback" : handler.changeScreen
}
handler.changeScreen("MANAGE", config)