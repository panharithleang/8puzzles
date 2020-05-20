import math
class Node: 
  def __init__(self, data, goal, gvalue, parent=None):
    self.data = data
    self.goal = goal
    self.fvalue = self.caculate_hvalue() + gvalue
    self.gvalue = gvalue
    self.parent = parent
    self.checked = False
  def generate_children(self):
    children = []
    x, y = self.find_empty()
    if(self.parent != None):
      if(x != 0 and self.parent.data != self.move_up()):
        children.append(self.move_up())
      if(x != len(self.data)-1 and self.parent.data != self.move_down()):
        children.append(self.move_down())
      if(y != 0 and self.parent.data != self.move_left()):
        children.append(self.move_left())
      if(y != len(self.data)-1 and self.parent.data != self.move_right()):
        children.append(self.move_right())
    else:
      if(x != 0):
        children.append(self.move_up())
      if(x != len(self.data)-1):
        children.append(self.move_down())
      if(y != 0):
        children.append(self.move_left())
      if(y != len(self.data)-1):
        children.append(self.move_right())
    return children
  
  def move_up(self):
    x, y = self.find_empty()
    new_data = [d[:] for d in self.data] 
    new_data[x][y] = new_data[x-1][y]
    new_data[x-1][y] = "x"
    return new_data
  
  def move_down(self):
    x, y = self.find_empty()
    new_data = [d[:] for d in self.data] 
    new_data[x][y] = new_data[x+1][y]
    new_data[x+1][y] = "x"
    return new_data
  
  def move_right(self):
    x, y = self.find_empty()
    new_data = [d[:] for d in self.data] 
    new_data[x][y] = new_data[x][y+1]
    new_data[x][y+1] = "x"
    return new_data
  
  def move_left(self):
    x, y = self.find_empty()
    new_data = [d[:] for d in self.data] 
    new_data[x][y] = new_data[x][y-1]
    new_data[x][y-1] = "x"
    return new_data
  
  def caculate_hvalue(self):
    total_hvalue = 0
    for l in self.data:
      for d in l:
        x1, y1 = self.find_in_goal(d)
        x2, y2 = self.find_empty(d)
        total_hvalue += (math.pow((x1 - x2),2) + math.pow((y1 - y2),2))
    return total_hvalue
  
  def is_goal(self):
    return self.data == self.goal
  
  def find_in_goal(self, target='x'):
    for n in range(len(self.goal)):
      if(target in self.goal[n]):
        return [n, self.goal[n].index(target)]
    
  def find_empty(self, target="x"):
    for n in range(len(self.data)):
      if (target in self.data[n]):
        return [n,self.data[n].index(target)]
    return [-1, -1]

  def show_data(self):
    for i in self.data:
      print(i)
    print('\n')