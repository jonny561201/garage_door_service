import json


def write_status_to_file(door_number, time):
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            content = json.load(file)
            content[door_number] = f'{time:%Y-%m-%d %H:%M:%S%z}'

        with open('data.json', "w") as file:
            json.dump(content, file)
    except FileNotFoundError:
        content = {door_number: f'{time:%Y-%m-%d %H:%M:%S%z}'}
        with open('data.json', "w+") as file:
            json.dump(content, file)
