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
from Agent import *


# inputs = ["w", "a", "d"]
# oppt_act = {"a": "d", "d": "a"}
# class Node:
#     def __init__(self):
#         pass
# #class Piece:

# def next_position(self, position,action):
#     x,y = position
#     if action == "a":
#         return [x - 1, y]
#     elif action == "d":
#         return [x + 1, y]


async def agent_loop(server_address="localhost:8000", agent_name="student"):
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))
        exist_key = False
        primeira_it = True
        global x, y
        while True:
            try:
                state = json.loads(
                    await websocket.recv()
                )  # receive game update, this must be called timely or your game will get out of sync with the server
                # Stuff

                key = ""
                if primeira_it:
                    # print(state['grid'])
                    primeira_it = False

                    x = (state['dimensions'][0])
                    y = (state['dimensions'][1])
                else:
                    # print(state['game'])
                    if state['piece'] is None:
                        # print(state['piece'])
                        print("New Piece")
                        print(state['next_pieces'][0])  # proxima peça
                        print("Height")
                        print(calculate_total_height(state, x, y))
                        print("Holes")
                        print(calculate_holes(state, x, y))
                        print("Bumpiness")
                        print(calculate_bumpiness(state, x, y))
                    if exist_key == False:
                        keys = next_key(state)  # para agent2.py
                        # keys = next_key(state)  para agent.py
                        exist_key = True

                    if len(keys):
                        key = keys[0]
                        keys = keys[1:]
                    else:
                        exist_key = False

                await websocket.send(
                    json.dumps({"cmd": "key",
                                "key": key}))  # send key command to server - you must implement this send in the AI agent

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

# net_task = loop.create_task()
# solver_task = loop.create_task(())
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))
# loop.close()
