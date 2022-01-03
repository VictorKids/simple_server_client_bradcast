# Importing the relevant libraries
import websockets
import asyncio

#The main function that will handle connection and communication with the server
async def listen():

    url = "ws://127.0.0.1:7890"

    #connect to the server
    async with websockets.connect(url) as ws:

        #send a greeting msg
        await ws.send("Hello Server!")

        #stay alive forever, listening to incoming msgs
        while True:
            msg = await ws.recv()
            print(msg)

#start the connection
asyncio.get_event_loop().run_until_complete(listen())