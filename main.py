import menus
import importwordsearch
import observeedit
import generatewordsearches

result = menus.start_menu("main/main")
while True:
    # Uses my ***VERSITILE MENU SYSTEM*** to select an option!
    # Then calls function in relation to that option.

    if result == "exit":
        break
    
    if result == "importwordsearch":
        path = input("Please enter the path to the .csv wordsearch file.\n: ")
        importwordsearch.import_wordsearch_from_file(path)
        result=menus.start_menu("main/solvemenu")
        
    if result == "observeandeditwordsearch":
        observeedit.observe_edit_ws()
        result=menus.start_menu("main/solvemenu")

    if result == "genws":
        generatewordsearches.generate_wordsearch()
        result=menus.start_menu("main/main")