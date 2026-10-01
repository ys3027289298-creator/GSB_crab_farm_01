import json


def new_game():
    return {'src': 10, 'dst': 0, 'events': {1: True}, 'paused': False, 'balance': 10, 'clock': 0, 'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_13(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def bug_20(state):
    state["events"].pop(1, None)
    return True

def bug_27(state):
    return False

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
    if 2 in state["events"]:
        return False
    state["events"][2] = True
    return True

def bug_25(state):
    if state["paused"]:
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def bug_2(state):
    return None

def bug_9(state):
    return state["next_id"]

def bug_16(state):
    return [row for row in state["audit"] if row[0] == "a"]

def bug_30(state):
    if any(len(entry) > 1 and entry[1] == "failed" for entry in state["log"]):
        state["value"] = state["snapshot"]
        return False
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
