# Importing the relevant libraries
import websockets
import asyncio

PORT = 7890

print("Server listening on Port " + str(PORT))

#set of current users
connected = set()

#websocket = client
async def echo(websocket, path):

        #loging client connection
        print("A client just connected")
        #adding a new client to the set
        connected.add(websocket)

        try:

            #iterates through upcoming msgs
            #garatides that one msg is handled by time
            async for message in websocket:
                
                print("Received message from client: " + message)
                for conn in connected:
                    if conn != websocket:
                        await conn.send("Someone said: " + message)
                #await websocket.send("Echo says: " + message)

        except websockets.exceptions.ConnectionClosed as e:

            print("A client just disconnected")

        finally:
            
            #remove disconneted clients
            connected.remove(websocket)

#instance of the server
start_server = websockets.serve(echo, "localhost", PORT)

#start the server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()