import Pacman

# Example1:
b = Pacman.Board(10, 10)
b.putPacman([3, 4])
b.putGhost([[3, 5], [1, 7], [6, 6]])
b.putWalls([[4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9]])
print(b.board)
b.findGhosts()
b.findGhostsHeuristic()

# Example2:
b = Pacman.Board(10, 10)
b.putPacman([3, 4])
b.randomize()
print("\n")
print(b.board)
b.findGhosts()
b.findGhostsHeuristic()
