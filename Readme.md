## Clipboard Data Management Script Documentation

This Python script provides functionality to manage clipboard data using a command-line interface. It allows users to save, load, and list clipboard data using user-defined keys. The data is stored in a JSON file for persistence.

### Libraries Used:

- `sys`: Provides access to variables and functions related to the Python interpreter and command-line arguments.
- `clipboard`: Offers functions to interact with the system clipboard.
- `json`: Enables reading and writing JSON files.

### Constants:

- `Saved_Data`: A string that defines the name of the JSON file where clipboard data will be stored.

### Function Definitions:

1. `save_items(filepath, data)`:
   - Arguments:
     - `filepath` (string): The path to the JSON file where data will be saved.
     - `data` (dictionary): The data to be saved.
   - Opens the specified file in write mode.
   - Uses `json.dump()` to write the data dictionary in JSON format to the file.

2. `load_items(filepath)`:
   - Argument:
     - `filepath` (string): The path to the JSON file to load data from.
   - Tries to open the specified file in read mode.
   - Uses `json.load()` to parse the JSON data from the file and returns it as a dictionary.
   - If the file doesn't exist or there's an error, returns an empty dictionary.

### Main Code Execution:

1. Checks if exactly one command-line argument is provided:
   - If yes:
     - Retrieves the command from the command-line arguments.
     - Loads existing clipboard data from the JSON file using `load_items()`.

2. Processes the provided command using conditional statements:
   - If the command is "save":
     - Prompts the user to enter a key.
     - Fetches clipboard data using `clipboard.paste()`.
     - Adds the data to the dictionary with the key.
     - Saves the updated data dictionary using `save_items()`.
     - Prints a success message.

   - If the command is "load":
     - Prompts the user to enter a key.
     - If the key exists in the data dictionary, copies the associated clipboard data to the system clipboard using `clipboard.copy()`.
     - Prints a success message.
     - If the key doesn't exist, prints an error message.

   - If the command is "list":
     - Prints the entire data dictionary.

   - If the command is none of the above:
     - Prints an "Unknown command" message.

3. If no or more than one command-line argument is provided:
   - Prints a message instructing the user to pass only one command.

### Usage:

1. Run the script from the command line with the desired command:
   - `python script_name.py save`
   - `python script_name.py load`
   - `python script_name.py list`

2. Follow the prompts and instructions provided by the script for each command.

3. Ensure that the `clipboard.json` file is in the same directory as the script for data persistence.

**Note:** Make sure to replace `script_name.py` with the actual name of your Python script file.
