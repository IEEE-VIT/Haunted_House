rooms = {
    "hallway": {
        "description": "You are in a dark and spooky hallway.",
        "exits": {"west": "kitchen", "east": "living_room", "downstairs":"basement", "upstairs":"attic"},
    },
    "kitchen": {
        "description": "You are in a dusty old kitchen with cobwebs.",
        "exits": {"east": "hallway", "west": "pantry"},
        "items": {"knife", "bread"},
    },
    "pantry": {
        "description": "You are in a small pantry filled with shelves.",
        "exits": {"east": "kitchen"},
        "rats": True,
    },
    "living_room": {
        "description": "You are in a creepy living room with creaky furniture.",
        "exits": {"west": "hallway", "north": "library"},
        "items": {"black cat hair"},
    },
    "library": {
        "description": "You are in a dimly lit library filled with old books.",
        "exits": {"south": "living_room", "east":"bedroom"},
        "items": {"locket"},
    },
    "bedroom": {
        "description": "You are in a spooky bedroom with a large, unmade bed.",
        "exits": {"west": "living_room"},
        "items":{"treasure box"},
        "lock":True,
        "puzzle": "You see a locked chest with a numeric keypad. You need a code to open it. It can only be found in an old book.",
        "ending":"You have successfully secured the treasure! Thanks for playing with us"
    },
    "secretroom": {
        "description": "You are in a old,dusty room filled with lots of unopened boxes and antiques.",
        "exits": {"east": "kitchen", "west": "guestroom"},
        "items": {"big box","golden key"},
    },
    "guestroom": {
        "description": "You enter into a clean,tidy room untouched in years as it seems.",
        "exits": {"north": "bedroom"},
        "items": {"blood stained watch"},
    },
    "basement":{
        "description": "You are in a dimly lit basement with a musty smell."
        "exits": {"upstairs": "hallway"},
        "items":{"knight's sword"}
    },
    "attic":{
        "description": "You are in a dusty attic filled with old furniture and cobwebs.",
        "exits": {"downstairs": "hallway"},
        "items": {"old_book"}
    }
}
