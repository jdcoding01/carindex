import asyncio
import json
import websockets

# create handler for each connection

async def handler(websocket, path):

    data = await websocket.recv()
    msg = json.loads(data)

    if msg["message"] == "/help":
        await websocket.send('{ "message": "Ok, got it." }')
    elif msg["message"].split(" ")[0] == "/scan":
        print(msg["message"].split(" ")[1])
    else:
        await websocket.send('{ "message": "Sorry, I didn\'t quite get that" }')

    await asyncio.Event().wait()

 

start_server = websockets.serve(handler, "localhost", 8000)

 

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()