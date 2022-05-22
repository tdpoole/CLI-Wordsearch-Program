import json
import os
import menus
import pickle
import importwordsearch

# Lets user interact with imported wordsearches
def observe_edit_ws():
    options = []
    valid_ansewrs = []
    ldir = os.listdir("loaded_wordsearch_files")
    
    if len(ldir)==0:
        print("No loaded wordsearches. Please import them first.\nReturning to main menu")
        return
    # Asks what wordsearch the user wants to inspect
    for i, x in enumerate(ldir):
        options.append(x.strip(".ws"))
        valid_ansewrs.append(str(i))

    while True:
        print("Which wordsearch do you want to select?")
        for i, x in enumerate(options):
            print(f"{i}: {x}")
        ans = input(": ")

        if ans in valid_ansewrs:
            break
        print("That answer was invalid. Please try again.")
    chosen_wordsearch = options[int(ans)]
    with open("loaded_wordsearch_files/" + chosen_wordsearch + ".ws", "rb") as f:
        editing_wordsearch = pickle.load(f)
    while True:
        # Uses my *VERSITILE MENU SYSTEM* to select an option!
        result = menus.start_menu("editobserve/main")
        if result=="exit":
            importwordsearch.serialise_wordsearch(editing_wordsearch, chosen_wordsearch)
            break
        
        # Reevaluates words based on new imput.
        elif result=="edit":
            editing_wordsearch.containswords = (
                input(
                    "Please enter the words this wordsearch should contain seperated by a space\n: "
                )
                .upper()
                .split()
            )
            print("Searching for words:")
            for x in editing_wordsearch.containswords:
                print(x)
            editing_wordsearch.find_words()
            print("Sucesfully updated wordsearch")

        # Displays the dictionary with all the solutions in it.
        elif result=="observe":
            print("\n==========\nLocations of the words:\n")
            print(json.dumps(editing_wordsearch.wordlocations, indent=4))


if __name__ == "__main__":
    observe_edit_ws()
