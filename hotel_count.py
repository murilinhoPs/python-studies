from typing import List

listaA = ["+0A", "+9Z", "+4F", "-9Z", "+3G"]  # -> 4
listaB = ["+4B", "-4B", "+4B", "-4B"]  # -> return 1 (1 room)
listaC = ["+4A", "+5B", "+5A"]  # -> 3


def different_booked_rooms(rooms):
    hash_map = {}
    for n in rooms:
        floor_room = n[1] + n[2]
        if hash_map.get(floor_room) is not None:
            continue
        else:
            hash_map[floor_room] = n[0]
    else:
        return len(hash_map)


print(different_booked_rooms(listaB))


def booked_rooms_at_end(rooms: List[str]):
    count = 0
    hash_map = {}
    for n in rooms:
        floor_room = n[1] + n[2]

        if hash_map.get(floor_room) is not None:
            if "+" in n:
                hash_map[floor_room] = "+"
                count += 1
            if "-" in n:
                del hash_map[floor_room]
                count -= 1
        else:
            hash_map[floor_room] = n[0]
            if "+" in n:
                count += 1
    else:
        if count <= 0:
            hash_map = {}
        return {"total-booked": count, "rooms": list(hash_map.keys())}


def booked_rooms_at_end_count(rooms: List[str]):
    count = 0
    for n in rooms:
        if "+" in n:
            count += 1
        else:
            count -= 1
    else:
        return count


def booked_rooms_at_end_names(rooms: List[str]):
    hash_map = {}
    for n in rooms:
        floor_room = n[1] + n[2]
        if hash_map.get(floor_room) is not None:
            if "-" in n:
                del hash_map[floor_room]
        else:
            hash_map[floor_room] = n[0]
    else:
        return {"rooms": list(hash_map.keys())}


print(booked_rooms_at_end(listaA))
print(booked_rooms_at_end_count(listaA))
print(booked_rooms_at_end_names(listaA))
