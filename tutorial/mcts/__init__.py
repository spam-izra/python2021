from .node import MCTSNode

            
def step(root):
    node = root.selection()
    node = node.expansion()
    score = node.simulation()
    node.backpropagation(score)