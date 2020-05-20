from node import Node

class Graph: 
  def __init__(self, start, goal):
    self.start = start
    self.node_list = []
    self.goal = goal
    
  def a_star(self):
    opened = []
    opened.append(Node(self.start, self.goal, 0, None))
    self.node_list.append(Node(self.start, self.goal, 0, None))
    while (len(opened) > 0):
      selected =  min(opened, key=lambda n: n.fvalue)
      selected.checked = True
      if selected.is_goal():
        print('Finished')
        self.backtrack(selected)
        return
      children = selected.generate_children()      
      for child in children:
        if (child in [n.data for n in self.node_list]):
          index = [n.data for n in self.node_list].index(child)
          child_node = self.node_list[index]
          if(child_node.gvalue > selected.gvalue + 1):
            child_node.gvalue = selected.gvalue + 1
            child_node.parent = selected
          if(child_node.checked):
            continue            
        else:
          new_node = Node(child, self.goal, selected.gvalue + 1, selected)
          opened.append(new_node)
          self.node_list.append(new_node)
      opened.remove(selected)
  
  def bfs(self):
    opened = []
    opened.append(Node(self.start, self.goal, 0, None))
    self.node_list.append(Node(self.start, self.goal, 0, None))
    while (len(opened) > 0):
      selected = opened[0]
      selected.checked = True
      if selected.is_goal():
        print('Finished')
        self.backtrack(selected)
        return
      children = selected.generate_children()      
      for child in children:
        if (child in [n.data for n in self.node_list]):
          index = [n.data for n in self.node_list].index(child)
          child_node = self.node_list[index]
          if(child_node.gvalue > selected.gvalue + 1):
            child_node.gvalue = selected.gvalue + 1
            child_node.parent = selected
          if(child_node.checked):
            continue            
        else:
          new_node = Node(child, self.goal, selected.gvalue + 1, selected)
          opened.append(new_node)
          self.node_list.append(new_node)
      opened.remove(selected)
    
  def id_dfs(self):
    opened = []
    opened.append(Node(self.start, self.goal, 0, None))
    self.node_list.append(Node(self.start, self.goal, 0, None))
    while (len(opened) > 0):
      selected = opened[-1]
      selected.checked = True
      if selected.is_goal():
        print('Finished')
        self.backtrack(selected)
        return
      if (selected.gvalue < 31):
        children = selected.generate_children()      
        for child in children:
          if (child in [n.data for n in self.node_list]):
            index = [n.data for n in self.node_list].index(child)
            child_node = self.node_list[index]
            if(child_node.gvalue > selected.gvalue + 1):
              child_node.gvalue = selected.gvalue + 1
              child_node.parent = selected
            if(child_node.checked):
              continue            
          else:
            new_node = Node(child, self.goal, selected.gvalue + 1, selected)
            opened.append(new_node)
            self.node_list.append(new_node)
      opened.remove(selected)
    
  def backtrack(self, goal):
    route = []
    current = goal
    while(current.parent != None):
      route.append(current.parent)
      current = current.parent
    print(f'Need {len(route)} moves')
    for n in reversed(route):
      n.show_data()

  def is_solvable(self):
      flatten = lambda l: [item for sublist in l for item in sublist]
      flatten_start = flatten(self.start)
      flatten_goal = flatten(self.goal)
      flatten_start.remove('x')
      flatten_goal.remove('x')
      inversion = 0
      for i in range(len(flatten_start)):
        selected = flatten_start[i]
        current_inversion = len(list(set(flatten_start[i:]) & set(flatten_goal[:flatten_goal.index(selected)])))
        inversion += current_inversion
      if (len(self.start) % 2 != 0):
        return inversion % 2 == 0
      else:
        x_row = [x for x in self.start if 'x' in x][0]
        if (self.start.index(x_row) - len(self.start)) % 2 == 0 :
          return inversion % 2 != 0
        else:
          return inversion % 2 == 0
