from node import Node
from graph import Graph
from time import time

def main():
  # 9 moves
  start = [
    [1, 8, 2],
    ['x', 4, 3],
    [7, 6, 5]
  ]
  # 31 moves
  start = [
    [8, 6, 7],
    [2, 5, 4],
    [3, 'x', 1]
  ]

  goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 'x']
  ]
  graph1 = Graph(start, goal)
  start_time = time()
  if graph1.is_solvable():
    # graph1.id_dfs()
    # graph1.bfs()
    # graph1.id_a_star()
    graph1.a_star()
    end_time = time()
    print(f'finished in {end_time-start_time} s')
  else:
    print('No Solution')
  

if __name__ == '__main__':
  main()