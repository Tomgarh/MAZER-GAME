class Game(object):

    def __init__(self):
        #Board width
        self.size = 10
        self.minMoves = 0
        self.level = 0
        self.marksLocations = []
        self.wallsLocations = []
        self.empties = self.size ** 2 - len(self.wallsLocations) - len(self.marksLocations)
        self.maxLevels = 0
        self.x1 = 0
        self.y1 = 0
        self.x2= 0
        self.y2 = 0
        self.turns = 0

    def set_level(self, level):
        """Assigns the location of all the walls and starting player position for the selected level"""
        self.minmoves = level.minMoves[self.level]
        self.wallsLocations = level.wallsLocations[self.level]
        self.marksLocations = []
        self.turns = 0
        self.maxLevels = len(level.minMoves) - 1
        self.x1 = level.playerPosition[self.level][0]
        self.x2 = level.playerPosition[self.level][0]
        self.y1 = level.playerPosition[self.level][1]
        self.y2 = level.playerPosition[self.level][1]
        self.empties = self.size ** 2 - len(self.wallsLocations) - len(self.marksLocations)
    
    def make_marks(self):
        """Creates markers at every position that the player crosses"""
        if self.y1 == self.y2 and self.x2 > self.x1:
            for displace in range(self.x2 - self.x1 + 1):
                if [self.x1 + displace, self.y1] not in self.marksLocations:
                    self.marksLocations.append([self.x1 + displace, self.y1])
        elif self.y1 == self.y2 and self.x1 > self.x2:
            for displace in range(self.x1 - self.x2 + 1):
                if [self.x2 + displace, self.y1] not in self.marksLocations:
                    self.marksLocations.append([self.x2 + displace, self.y1])
        elif self.y2 > self.y1:
            for displace in range(self.y2 - self.y1 + 1):
                if [self.x1, self.y1 + displace] not in self.marksLocations:
                    self.marksLocations.append([self.x1, self.y1 + displace])
        else:
            for displace in range(self.y1 - self.y2 + 1):
                if [self.x1, self.y2 + displace] not in self.marksLocations:
                    self.marksLocations.append([self.x1, self.y2 + displace])
        self.empties = self.size ** 2 - len(self.wallsLocations) - len(self.marksLocations)

    def move(self, direction):
        """Takes a direction and moves the player in that direction"""
        self.x1 = self.x2
        self.y1 = self.y2

        skip = self.distance_to_edge(direction)
        moves = {
            'a' : [-skip, 0],
            'd' : [skip, 0],
            'w' : [0, -skip],
            's' : [0, skip]
        }

        if \
            direction in moves \
            and self.x1 + moves[direction][0] in range(self.size) \
            and self.y1 + moves[direction][1] in range(self.size):
            #if statement checks the move is in still in the maze and is a legal direction
            self.x2 = self.x1 + moves[direction][0]
            self.y2 = self.y1 + moves[direction][1]
            if self.x2 != self.x1 or self.y2 != self.y1:
                self.turns += 1 

    def distance_to_edge(self, direction):
        """Calculates how far away the nearest wall or edge is and returns how far the self must travel to get there"""
        calc = []
        edge = 0
        
        for wall in self.wallsLocations:
            #I think I can simplify the logic here
            if direction == 'd':
                edge = (self.size - 1) - self.x1
                if wall[1] == self.y2 and (wall[0] - self.x1) > 0:
                    calc.append(wall[0] - self.x1)
                    
            elif direction == 'a':
                edge = self.x1
                if wall[1] == self.y2 and (self.x1 - wall[0]) > 0:
                    calc.append(self.x1 - wall[0])
                    
            elif direction == 's':
                edge = (self.size - 1) - self.y2
                if wall[0] == self.x1 and (wall[1] - self.y2) > 0:
                    calc.append(wall[1] - self.y2)
                    
            elif direction == 'w':
                edge = self.y2
                if wall[0] == self.x1 and (self.y2 - wall[1]) > 0:
                    calc.append(self.y2 - wall[1])

        if calc == []:
            calc = edge
        else:
            calc = min(calc)-1
        return calc