import json


def new_game():
    return {'src': 10, 'dst': 0, 'events': {1: True}, 'paused': False, 'balance': 10, 'clock': 0, 'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'snapshot': 5, 'value': 5, 'log': [], 'settled': False, 'owner': 'a'}

def bug_13(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def bug_20(state):
    state["events"].pop(1, None)
    return True

def bug_27(state):
    if state.get("from") == state.get("to"):
        return False
    return True

def bug_4(state):
    if state["paused"]:
        return False
    return True

def bug_11(state):
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True

def bug_18(state):
    event_id = 2
    if event_id in state["events"]:
        return False
    state["events"][event_id] = True
    return True

def bug_25(state):
    if state["paused"]:
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def bug_2(state):
    return None

def bug_9(state):
    allocated = state["next_id"]
    state["next_id"] += 1
    return allocated

def bug_16(state):
    owner = state.get("owner")
    return [row for row in state["audit"] if row[0] == owner]

def bug_30(state):
    if any(entry[1] == "failed" for entry in state["log"]):
        state["value"] = state["snapshot"]
        return False
    state["snapshot"] = state["value"]
    return True

def bug_31(state):
    if state["settled"]:
        return False
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
