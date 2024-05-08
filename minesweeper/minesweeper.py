import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # All cells in the Sentence are mines if the num_cells = num_mines
        if len(self.cells) == self.count and self.count != 0:
            return self.cells
        # If the number of cells != count, we don't know for sure which are mines
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # Cells are safe if there is a count of zero for all cells in the sentence
        if self.count == 0:
            return self.cells
        # If the count != zero, we don't know which are safe.
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # If the cell is in the sentence, remove it and update the count
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # If cell is sentence, remove it. No need to update count
        if cell in self.cells:
            self.cells.remove(cell)

class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Mark the cell as a move that has been made
        self.moves_made.add(cell)
        # Mark the cell as safe
        self.mark_safe(cell)
        # Add a new sentence to the AI's knowledge base based on the value of cell and count
        unknown = set()
        num_mines = 0
        # Iterate through rows
        for i in range(cell[0]-1, cell[0]+2):
            # Iterate over columns
            for j in range(cell[1]-1, cell[1]+2):
                # Ignore current cell, ensure cell is within bounds
                if (i,j) != cell and (0 <= i < self.height) and (0 <= j < self.width):
                    # Keep track of which cells are known mines
                    if (i,j) in self.mines:
                        num_mines += 1
                    # Append unknown cells to list 
                    elif (i,j) not in self.safes:
                        unknown.add((i,j))
        # Add new sentence to kb, based on cell and count
        new_sentence = Sentence(unknown, (count - num_mines))
        self.knowledge.append(new_sentence)
        # Mark cells as safe or as mines, if it can be concluded from KB
        # Iterate over sentences in KB
        for sentence in self.knowledge:
            # If there are mines in the sentence, mark and remove
            if sentence.known_mines():
                # Iterate over copy of mines set, since modifications will be made
                for mine in sentence.known_mines().copy():
                    self.mark_mine(mine)
                    sentence.mark_mine(mine)
            # If there are known safes, mark and remove
            if sentence.known_safes():
                # Iterate over copy of safes set, since modifications will be made
                for safe in sentence.known_safes().copy():
                    self.mark_safe(safe)
                    sentence.mark_safe(safe)
        
        # Add any new sentences if they can be inferred from KB
        for sentence in self.knowledge:
            if new_sentence.cells.issubset(sentence.cells) and sentence.count > 0 and new_sentence != sentence:
                new_cells = sentence.cells.difference(new_sentence.cells)
                new_info = Sentence(new_cells, (sentence.count - new_sentence.count))
                # Add new sentence if it is not already in KB
                if new_info not in self.knowledge:
                    self.knowledge.append(new_info)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Initiate list of options
        options = []
        # Iterate over cells known to be safe
        for cell in self.safes:
            # If move has not been made, append it to the list of options
            if cell not in self.moves_made:
                options.append(cell)
        # Return a random cell from the list of options. If no options, return None
        if len(options) > 0:
            return random.choice(options)
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # If no safe move is possible
        if self.make_safe_move() == None:
            options = []
            # Iterate over rows and columns
            for i in range(self.height):
                for j in range(self.width):
                    cell = i,j
                    # Add cell to options if not a mine and not in moves_made
                    if cell not in self.mines and cell not in self.moves_made:
                        options.append(cell)
            # If options exist, return a random option. Otherwise, return None
            if len(options) > 0:
                return random.choice(options)
            return None
        # If a safe move is possible, return that instead
        return self.make_safe_move()