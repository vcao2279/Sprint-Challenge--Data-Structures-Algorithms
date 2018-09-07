class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    #use Stack
    #Run cb function on current node value
    cb(self.value)
    #If there is left node, run cb function on the left node
    if self.left:
      self.left.depth_first_for_each(cb)
    #If there is left node, run cb function on the right node
    if self.right:
      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    #use Queue
    queue = []
    #first item in queue is root node
    queue.append(self)
    #repeat loop when there is item(s) in queue
    while queue:
      node = queue.pop(0)
      #call cb on the value of the node
      cb(node.value)
      #if there is a node on the left of current node, add it to queue
      if (node.left):
        queue.append(node.left)
      #if there is a node on the left of current node, add it to queue
      if (node.right):
        queue.append(node.right)
        

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
