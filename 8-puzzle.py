

numrows = 3
class Node():
    def __init__(self, state, priority, depth, leaves, locX, locY):
        self.state = state
        self.priority = priority
        self.depth = depth
        self.leaves = leaves
        self.locX = locX
        self.locY = locY
        
        int i = 0
        for i in range(9):
            if state == 0:
                continue

        self.locX = i%3
        self.locY = i/3
    
 