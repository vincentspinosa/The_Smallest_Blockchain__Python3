blocks = []

class Block:
  def __init__(self):
    self.id = 0 if len(blocks) < 1 else len(blocks)
    self.name = 'Block ' + str(self.id)
    self.prev = self.id - 1 if self.id > 0 else None
    self.next = None
    return None

  def __repr__(self):
    return f"Id : {self.id}, Name : {self.name}, Previous : {self.prev}, Next : {self.next}"

class NewB:
  def __init__(self):
    self.newBlock = Block()
    blocks.append(self.newBlock)
    if self.newBlock.prev is not None:
      blocks[self.newBlock.prev].next = self.newBlock.id
    return None

  def __repr__(self):
    return f"Id : {self.newBlock.id}, Name : {self.newBlock.name}, Previous : {self.newBlock.prev}, Next : {self.newBlock.next}"


for i in range(20):
  i = NewB()

for i in range(len(blocks)):
  print(blocks[i].__repr__())
