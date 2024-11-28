from experta import *

# Define a Fact to represent a path step
class PathStep(Fact):
    """Represents a single step in the path"""
    pass

# Define the Expert System
class PathfindingExpertSystem(KnowledgeEngine):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph  # Graph as a dictionary
        self.shortest_path = []  # To store the shortest path
        self.visited = set()  # To track visited nodes

    @DefFacts()
    def _initial_fact(self):
        """Initialize the graph traversal with a start and goal."""
        yield PathStep(current='A', goal='H', cost=0)


    #came for destination
    @Rule(PathStep(current=MATCH.current, goal=MATCH.goal, cost=MATCH.cost),
          TEST(lambda current, goal: current == goal))
    def reached_goal(self, current, goal, cost):
        """When the goal is reached, record the result."""
        print(f"Goal {goal} reached with total cost: {cost}")
        self.shortest_path.append(goal)

    @Rule(PathStep(current=MATCH.current, goal=MATCH.goal, cost=MATCH.cost),
          TEST(lambda current, goal: current != goal),
          AS.fact << PathStep())
    def traverse_graph(self, fact, current, goal, cost):
        """Traverse to the next node."""
        self.visited.add(current)

        # Get neighbors of the current node
        neighbors = self.graph.get(current, [])
        next_steps = sorted([(neighbor, neighbor_cost) for neighbor, neighbor_cost in neighbors if neighbor not in self.visited])

        if not next_steps:
            print(f"No further steps from {current}. Dead-end.")
            return

        # Choose the next step with the least cost
        next_node, edge_cost = min(next_steps, key=lambda x: x[1])
        total_cost = cost + edge_cost

        # Record the step and declare it as a fact
        print(f"Moving from {current} to {next_node} with cost {edge_cost}. Total cost so far: {total_cost}")
        self.shortest_path.append(current)
        self.modify(fact, current=next_node, goal=goal, cost=total_cost)

# Define the graph
graph = {
    'A': [('B', 4), ('C', 5), ('D', 5), ('F', 3)],
    'B': [('A', 4), ('C', 7)],
    'C': [('A', 5), ('B', 7)],
    'D': [('A', 5), ('E', 9), ('G', 9)],
    'E': [('D', 9), ('G', 7)],
    'F': [('A', 3), ('I', 3), ('G', 5)],
    'G': [('E', 7), ('D', 9), ('F', 5), ('I', 2), ('H', 1)],
    'H': [('G', 1), ('I', 3)],
    'I': [('F', 3), ('G', 2), ('H', 3)]

}

# Run the Expert System
engine = PathfindingExpertSystem(graph)
engine.reset()  # Initialize the system
engine.run()  # Run the rules

# Output the shortest path
print("Shortest Path:", " -> ".join(engine.shortest_path))
