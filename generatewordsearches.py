import json
import random
import support
import csv

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
directions=["NORTH","SOUTH","EAST","WEST","NORTHEAST","NORTHWEST","SOUTHEAST","SOUTHWEST"]
shift_values={
    "NORTH":{
        "x":0,
        "y":-1
    },
    "SOUTH":{
        "x":0,
        "y":1
    },
    "EAST":{
        "x":1,
        "y":0
    },
    "WEST":{
        "x":-1,
        "y":0
    },
    "NORTHEAST":{
        "x":1,
        "y":-1
    },
    "NORTHWEST":{
        "x":-1,
        "y":-1
    },
    "SOUTHEAST":{
        "x":1,
        "y":1
    },
    "SOUTHWEST":{
        "x":-1,
        "y":1
    }
}

def generate_wordsearch():
    words=input("Please enter the words you want to add to the wordsearch seperated by a space\n: ").upper().split()
    print(words)
    width=support.inputint("Please enter the width of the wordsearch\n: ")
    length=support.inputint("Please enter the length of the wordsearch\n: ")
    name=input("Please name your wordsearch\n: ")
    print("Loading empty grid...")
    grid=[["empty" for x in range(width)]for y in range(length)]
    
    for adding_word in words:
        print("Adding "+adding_word)
        gridbackup=grid
        sucess=False
        
        timeout=0
        while not sucess:
            timeout+=1
            
            if timeout>=100000:
                print("This wordsearch could not be generated.")
                return
            
            gridbackup=grid
            chosen_direction=random.choice(directions)
            chosen_x=random.randint(0,width-1)
            chosen_y=random.randint(0,length-1)            
            
            for addingletter in list(adding_word):            
                
                try:
                    if gridbackup[chosen_y][chosen_x] == "empty" or gridbackup[chosen_y][chosen_x] == addingletter:
                        gridbackup[chosen_y][chosen_x]=addingletter
                        chosen_x+=shift_values[chosen_direction]["x"]
                        chosen_y+=shift_values[chosen_direction]["y"]
                    else:
                        break
                except IndexError:
                    break
                
                if addingletter==adding_word[-1]:
                    sucess=True
                    grid=gridbackup
    print("Filling in letters...")
    #Added words, now fill in the spaces
    for y,row in enumerate(grid):
        for x,val in enumerate(row):
            if val=="empty":
                grid[y][x]=random.choice(alphabet)
    print("Writing to file...")
    with open(name+".csv","w",newline="")as f:
        writer=csv.writer(f)
        writer.writerows(grid)
    
    print("Sucess!")
    
    
if __name__ == "__main__":
    generate_wordsearch()