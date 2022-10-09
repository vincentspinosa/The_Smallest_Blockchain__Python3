from datetime import datetime

class Block:
  def __init__(self, chain):
    x = len(chain.blocks)
    self.id = 0 if x < 1 else x
    self.name = 'Block ' + str(self.id)
    self.creation_date = datetime.now()
    self.prev = self.id - 1 if self.id > 0 else None
    self.next = None
    return None

  def __repr__(self):
    return f"Id: {self.id}, Name: {self.name}, Creation: {self.creation_date}, Previous: {self.prev}, Next: {self.next}"


class New_Block:
  def __init__(self, chain):
    self.newBlock = Block(chain)
    chain.blocks.append(self.newBlock)
    if self.newBlock.prev is not None:
      chain.blocks[self.newBlock.prev].next = self.newBlock.id
    return None

  def __repr__(self, chain):
    return True if chain.blocks[self.newBlock.prev].next == self.newBlock.id else False


class Blockchain:
  def __init__(self):
    self.blocks = []
    for i in range(20):
      i = New_Block(self)
    return None

  def count_blocks(self):
    return len(self.blocks)

  def print_blockchain(self):
    for block in self.blocks:
      print(block.__repr__())
    return None


def main():
  Main = Blockchain()
  print(f"{Main.count_blocks()} Blocks\n")
  Main.print_blockchain()
  return None


__BLOCKCHAIN__ = main()
