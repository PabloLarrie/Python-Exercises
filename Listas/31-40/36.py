dic = {
    "count": 380,
    "next": "http://127.0.0.1:8001/cards/cards/?page=2",
    "previous": None,
    "results": [
        {"id": 8, "name": "Mind Control", "card_type": "spell", "quality": "common"},
        {"id": 12, "name": "Mana Addict", "card_type": "minion", "quality": "rare"},
        {"id": 22, "name": "Inner Rage", "card_type": "spell", "quality": "common"},
    ],
}


# def go_inside(formula):
#     result = [y for y in formula.values() if type(y) == list]
#     second = [v for v in result]
#     return second


def go_inside(formula):
    result = [y for v in formula.values() if type(v) == list for y in v]
    return result


print(go_inside(dic))