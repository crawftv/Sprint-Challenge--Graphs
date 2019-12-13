from room import Room
from player import Player
from world import World
from adv_room import roomGraph
import random

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.

# roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}], 12: [(4, 6), {'w': 1, 'e': 13}], 13: [(5, 6), {'w': 12, 'n': 14}], 14: [(5, 7), {'s': 13}], 15: [(2, 6), {'e': 1, 'w': 16}], 16: [(1, 6), {'n': 17, 'e': 15}], 17: [(1, 7), {'s': 16}]}
roomGraph = roomGraph

world.loadGraph(roomGraph)
world.printRooms()

player = Player("Name", world.startingRoom)
player_graph = {world.startingRoom.id:{}}
opposite_map = {"n":"s","e":"w","w":"e","s":"n"}
traversalPath = []
visited_rooms_list = [0,]

# def move(direction)): 
#     previous_room = player.currentRoom.id
#     player.travel(direction)
#     traversalPath.append(direction)
#     player_graph[previous_room][direction]=player.currentRoom.id
#     new_exits = player.currentRoom.get_exits()
#     if player.currentRoom.id not in player_graph.keys():
#         player_graph[player.currentRoom.id] = {i:"?" for i in new_exits}
#     player_graph[player.currentRoom.id][opposite_map[direction]] = previous_room

exits = player.currentRoom.get_exits()
player_graph[player.currentRoom.id] = {i:"?" for i in exits}
player_graph[player.currentRoom.id]["breadcrumb"] = "w"
player_graph[player.currentRoom.id]["unexplored"] = [player.currentRoom.id]
bread_crumb = False
# import pdb;pdb.set_trace()
while len(player_graph)<440:
    
    direction = None
   

    previous_room = player.currentRoom.id
    
    if bread_crumb == True:
        if player_graph[player.currentRoom.id]["unexplored"] is not None:
            for key,value in player_graph[player.currentRoom.id].items():
                if (key in ["n","s","e","w"]) and (value =="?"):
                    direction = key
                    break
                elif key in ["n","s","e","w"]:
                    if value==player_graph[player.currentRoom.id]["unexplored"]:
                        direction = key
    
    bread_crumb = False

    
    if direction is None:
        for key,value in player_graph[player.currentRoom.id].items():
            if (key in ["n","s","e","w"]) and (value == "?"):
                direction = key

    
    
    if direction == None:
        direction=player_graph[player.currentRoom.id]["breadcrumb"]
        bread_crumb = True
    
    
    player.travel(direction)
    traversalPath.append(direction)
    visited_rooms_list.append(player.currentRoom.id)
    
    player_graph[previous_room][direction]=player.currentRoom.id
    new_exits = player.currentRoom.get_exits()

    if player.currentRoom.id not in player_graph.keys():
        player_graph[player.currentRoom.id] = {i:"?" for i in new_exits}
        player_graph[player.currentRoom.id]["breadcrumb"] = opposite_map[direction]
        if player_graph[previous_room]["unexplored"] is not None:
            player_graph[player.currentRoom.id]["unexplored"] = previous_room
    
    

    player_graph[player.currentRoom.id][opposite_map[direction]] = previous_room
    
    # elif player_graph[previous_room]["unexplored"] is None:
    #     if player
# FILL THIS IN


print(visited_rooms_list)
print(player_graph[218])

# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom.id)
not_visited_rooms = [i for i in list(roomGraph.keys()) if i not in visited_rooms]
if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")

    print(sorted(not_visited_rooms))
    print(len(traversalPath))
    o = open("path.txt","w")
    o.write(", ".join([str(i) for i in visited_rooms_list]))
    o.close()



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
