        if state not in visited:
            visited.add(state)
            for successor, action, cost in problem.expand(state):
                frontier.append((successor, actions + [action]))
    return None
    

def breadthFirstSearch(problem):
    visited = set()
    frontier = [(problem.getStartState(), [])]
    while frontier:
        state, actions = frontier.pop(0)