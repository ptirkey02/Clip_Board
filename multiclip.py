import sys
import clipboard
import json

Saved_Data = "clipboard.json"

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# save_items("test.json", {"key":"value"})

def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}
    

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(Saved_Data)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(Saved_Data, data)
        print("Your data has saved.")

    elif command=="load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("You have loaded your data!")
        else:
            print("There is no such key!")

    elif command == "list":
        print(data)

    else:
        print("Unknown command")
else:
    print("Please pass only one command.")
