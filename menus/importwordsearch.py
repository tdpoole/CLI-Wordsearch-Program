import csv
from wordsearchclass import Wordsearch
import pickle

# Function to import, solve, then initialise and serialise the corresponding wordsearch object.
def import_wordsearch_from_file(file="wordsearch.csv"):
    try:
        with open(file, "r", newline="") as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
        serialise_wordsearch(Wordsearch(data))
    except FileNotFoundError:
        print("File not found. Returning.")

# Class to serialise the loaded wordsearch object
def serialise_wordsearch(serialidableclass, name=False):
    if not name:
        with open(
            f"loaded_wordsearch_files/{input('Please name your wordsearch   : ')}.ws",
            "wb",
        ) as f:
            pickle.dump(serialidableclass, f)
    else:
        with open(f"loaded_wordsearch_files/{name}.ws", "wb") as f:
            pickle.dump(serialidableclass, f)
    print("Wordsearch saved!")

if __name__=="__main__":
    import main