class Node:
  def __init__(self, id, dist) -> None:
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist
  # def __str__(self):
  #   return f'Vertex: ({self.id}) - dist: {self.dist}'
  def __repr__(self):
    # return f'Vertex: ({self.id}) - dist: {self.dist}'
    return f'({self.id}, {self.dist})'
