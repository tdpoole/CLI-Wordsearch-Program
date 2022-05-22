import json

# The wordsearch class will contain the wordsearch itself as well as the solution to the wordsearch.
class Wordsearch:
#   Initialising variables
    def __init__(self, data):
        self.grid = data
        self.row_count = len(data)
        self.column_count = len(data[0])
        self.containswords = (
            input(
                "Please input the words this wordsearch should contain seperated by a space\n: "
            )
            .upper()
            .split()
        )
        print("Looking for words:")
        for x in self.containswords:
            print("    " + x)
#       Solves wordsearch with inputted words. Is then serialised by importwordsearch.py
        self.find_words()

#   A simple function that checks to see if a word is in a certain direction. Returns bool.
    def check_in_direction(
        self,
        direction,
        # Refer to the up and down directions to search in
        dirx,
        diry,
        looking_for_word_list,
        start_row_position,
        start_column_position,
        looking_for_word,
    ):
        for index, letter in enumerate(looking_for_word_list):
            try:
                if (
                    letter.upper()
                    != self.grid[start_row_position + index * diry][
                        start_column_position + index * dirx
                    ].upper()
                ):
                    return False
            except IndexError:
                return False
            if index == len(looking_for_word_list) - 1:
                self.wordlocations[looking_for_word] = {}
                self.wordlocations[looking_for_word]["Location"] = (
                    str(start_column_position) + " , " + str(start_row_position)
                )
                self.wordlocations[looking_for_word]["Direction"] = direction
                return True

#   The actual wordsearcher
    def find_words(self):
        self.wordlocations = {}
        
        # Iterate through every word searching for
        for looking_for_word in self.containswords:
            sucess = False
            looking_for_word_list = list(looking_for_word)

            # Iterate through every word in the grid
            for start_row_position, currentrow in enumerate(self.grid):
                for start_column_position, starting_letter in enumerate(currentrow):

                    if (starting_letter == looking_for_word_list[0]):  # If so, it is worth checking

                        # Checks in each direction. Results are stored by the check_in_direction function
                        sucess = self.check_in_direction(
                            "NORTH",
                            0,
                            -1,
                            looking_for_word_list,
                            start_row_position,
                            start_column_position,
                            looking_for_word,
                        )

                        if not sucess:
                            sucess = self.check_in_direction(
                                "SOUTH",
                                0,
                                1,
                                looking_for_word_list,
                                start_row_position,
                                start_column_position,
                                looking_for_word,
                            )

                        if not sucess:
                            sucess = self.check_in_direction(
                                "WEST",
                                -1,
                                0,
                                looking_for_word_list,
                                start_row_position,
                                start_column_position,
                                looking_for_word,
                            )

                        if not sucess:
                            sucess = self.check_in_direction(
                                "EAST",
                                1,
                                0,
                                looking_for_word_list,
                                start_row_position,
                                start_column_position,
                                looking_for_word,
                            )

                        if not sucess:
                            sucess = self.check_in_direction(
                                "NORTHWEST",
                                -1,
                                -1,
                                looking_for_word_list,
                                start_row_position,
                                start_column_position,
                                looking_for_word,
                            )

                        if not sucess:
                            sucess = self.check_in_direction(
                                "NORTHEAST",
                                1,
                                -1,
                                looking_for_word_list,
                                start_row_position,
                                start_column_position,
                                looking_for_word,
                            )

                        if not sucess:
                            sucess = self.check_in_direction(
                                "SOUTHWEST",
                                -1,
                                1,
                                looking_for_word_list,
                                start_row_position,
                                start_column_position,
                                looking_for_word,
                            )

                        if not sucess:
                            sucess = self.check_in_direction(
                                "SOUTHEAST",
                                1,
                                1,
                                looking_for_word_list,
                                start_row_position,
                                start_column_position,
                                looking_for_word,
                            )

        # Works out which words the program was unable to find and display them to the user.
        failedtofind = self.containswords
        for x in list(self.wordlocations.keys()):
            failedtofind.remove(x)

        if len(failedtofind) > 0:
            print("=====\nFailiure : Failed to find these words:")
            for x in failedtofind:
                print("    " + x)
        else:
            print("=====\nSucess : Found all words!")

if __name__=="__main__":
    import main