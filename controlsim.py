import pyxinput
import time
from aiohttp import web
import socketio
import pyvjoy

sio = socketio.AsyncServer()

app = web.Application()

sio.attach(app)
MyVirtual = pyxinput.vController()

MyRead = pyxinput.rController(1)  # For Controller 1


def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.on("down")
def print_message(sid, message):

    if(message == 69):
        MyVirtual.set_value('BtnA', 1)
        time.sleep(0.1)

    elif(message == 37):
        MyVirtual.set_value('AxisLx', -1)

    elif (message == 38):
        MyVirtual.set_value('AxisLy', 1)

    elif (message == 39):
        MyVirtual.set_value('AxisLx', 1)

    elif(message == 40):
        MyVirtual.set_value('AxisLy', -1)

    elif (message == 32):
        MyVirtual.set_value('BtnB', 1)

    elif(message == 87):
        MyVirtual.set_value('BtnY', 1)

    elif(message == 70):
        MyVirtual.set_value('BtnX', 1)

    elif(message == 81):

        MyVirtual.set_value('BtnShoulderL', 1)
    elif(message == 16):
        MyVirtual.set_value('TriggerR', 1)


@sio.on("up")
def print_message(sid, message):

    if(message == 69):
        MyVirtual.set_value('BtnA', 0)

    elif(message == 37):

        MyVirtual.set_value('AxisLx', 0)

    elif (message == 38):

        MyVirtual.set_value('AxisLy', 0)

    elif (message == 39):

        MyVirtual.set_value('AxisLx', 0)

    elif(message == 40):

        MyVirtual.set_value('AxisLy', 0)

    elif (message == 32):

        MyVirtual.set_value('BtnB', 0)

    elif(message == 87):

        MyVirtual.set_value('BtnY', 0)

    elif(message == 70):

        MyVirtual.set_value('BtnX', 0)

    elif(message == 81):

        MyVirtual.set_value('BtnShoulderL', 0)

    elif(message == 16):
        MyVirtual.set_value('TriggerR', 0)


@sio.on("videoobj")
async def send_video(sid, videoobjsrc):
    await sio.emit("videoobj", videoobjsrc)


app.router.add_get('/', index)


if __name__ == '__main__':
    web.run_app(app)
