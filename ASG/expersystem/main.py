from experta import *

# Define a Fact to represent a path step
class PathStep(Fact):
    """Represents a single step in the path"""
    current = Field(str)
    goal = Field(str)
    cost = Field(int)
    cost = Field(int)
    time = Field(int)
    path = Field(list)  # Ensure the path is explicitly a list

# Define the Expert System
class PathfindingExpertSystem(KnowledgeEngine):
    def __init__(self, graph , sou , des):
        super().__init__()
        self.sou= sou
        self.des = des
        self.graph = graph  # Graph as a dictionary
        self.all_paths = []  # To store all possible paths with their costs

    @DefFacts()
    def _initial_fact(self):
        """Initialize the graph traversal with a start and goal."""
        yield PathStep(current=self.sou, goal=self.des, cost=0, time=0, path=[self.sou])  # Initialize with a list for the path

    # When destination is reached, store the path and its cost
    @Rule(PathStep(current=MATCH.goal, goal=MATCH.goal, cost=MATCH.cost, time=MATCH.time, path=MATCH.path))
    def goal_reached(self, cost, time, path):
        """Store successful paths to the goal."""
        self.all_paths.append((path, cost,time))

    # Traverse the graph to explore possible paths
    @Rule(PathStep(current=MATCH.current, goal=MATCH.goal, cost=MATCH.cost, time=MATCH.time ,  path=MATCH.path),
          TEST(lambda current, goal: current != goal))
    def traverse_graph(self, current, goal, cost,time, path):
        """Traverse to the next node."""
        visited = set(path)  # Avoid revisiting nodes
        neighbors = self.graph.get(current, [])

        for next_node, edge_cost , edge_time in neighbors:
            if next_node not in visited:
                total_cost = cost + edge_cost
                totalTime = time+edge_time
                new_path = list(path) + [next_node]  # Add the next node to the current path
                self.declare(PathStep(current=next_node, goal=goal, cost=total_cost, time=totalTime, path=new_path))







        
# Define the graph
graph = {
    'A': [('B', 4 , 7), ('C', 5, 6), ('D', 3, 10), ('F', 5, 2)],
    'B': [('A', 4,7), ('C', 7,6)],
    'C': [('A', 5,6), ('B', 7,6)],
    'D': [('A', 3,10), ('E', 9,10), ('G', 4,12)],
    'E': [('D', 9,10), ('G', 7,8)],
    'F': [('A', 5,2), ('I', 3,3), ('G', 5,4)],
    'G': [('E', 7,8), ('D', 4,12), ('F', 5,4), ('I', 2,1), ('H', 1,2)],
    'H': [('G', 1,2), ('I', 3,3)],
    'I': [('F', 3,3), ('G', 2,1), ('H', 3,3)]
}

# Run the Expert System
print("source")
source = input()
print("destination")
des= input()
engine = PathfindingExpertSystem(graph , source , des)
engine.reset()  # Initialize the system
engine.run()  # Run the rules









# Output all possible paths and their costs
print("\nAll Possible Paths and Costs:")
findedpaths = sorted(engine.all_paths, key=lambda x: x[2])

alter = "y"
i=0
ite = len(findedpaths)
while alter == "y" and i < ite:


    path , cost ,time = findedpaths[i]
    print(f"{' -> '.join(path)}       COST = {cost}  TIME = {time}")

    print(f"do you need alternative path 0{i+1}?(y/n)")
    alter = input()
    i=i+1
    



# Find and output the shortest path
if engine.all_paths:
    shortest_path, min_cost = min(engine.all_paths, key=lambda x: x[1])
    print("\nShortest Path:", " -> ".join(shortest_path))
    print(f"Total cost: {min_cost}")
else:
    print("No path found.")
