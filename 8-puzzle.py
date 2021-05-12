

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
    
    def move(direction):
        index = -1
        if(direction == 0 and self.locY != 0):
            index = (locY - 1) * numrows + locX
        elif(direction == 1 and locY != numrows - 1):
            index = (locY + 1) * numrows + locX
        elif(direction == 2 and locX != 0):
            index = locY * numrows + locX - 1
        elif(direction == 3 and locX != numrows - 1)
            index = locY*numrows + locX + 1
        else
            return -1
        
        state_update = self.state.copy()
        temp = state_update[index]
        state_update[index] = state_update[locY * numrows + locX]
        state_update[locY * numrows + locX] = temp
        return state_update

class Problem():
    def __init__(self, init_state, goal_state, algo):
        self.init_state = int_state
        self.goal_state = [1,2,3,4,5,6,7,8,0]
        self.algo = algo
        head = [(self, 0)]      

    def solve():
        repeated = set([])
        limit = 0


        while head:
            for i in range(4):
                head.state = move(i)




if __name__ == "__main__":
    print("Welcome to the 8-Puzzle")

    print("Enter Algorithm of choice")
    choice = input("1: Uniform, 2: A* w/ misplaced, 3: A* w/ manhattan distance")