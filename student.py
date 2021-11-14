import asyncio
import getpass
import json
import os
import random
import time
import websockets

from shape import Shape
import common
import treeSearch
import Agent

inputs = ["w", "a", "d"]
oppt_act = {"a": "d", "d": "a"}
class Node:
    def __init__(self):
        pass
#class Piece:

#def next_position(self, position,action):
#    x,y = position
#    if action == "a":
#        return [x - 1, y]
#    elif action == "d":
#        return [x + 1, y]

async def agent_loop(server_address="localhost:8000", agent_name="student"):
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))

        while True:
            try:
                state = json.loads(
                    await websocket.recv()
                )  # receive game update, this must be called timely or your game will get out of sync with the server
                #Stuff


                key = ""
                
                
                await websocket.send(
                    json.dumps({"cmd": "key", "key": key}))  # send key command to server - you must implement this send in the AI agent

            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return


# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='arrumador' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = os.environ.get("NAME", getpass.getuser())

#net_task = loop.create_task()
#solver_task = loop.create_task(())
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))
#loop.close()
