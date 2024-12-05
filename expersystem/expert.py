from experta import *

# Define a Fact to represent a path step
class PathStep(Fact):
    """Represents a single step in the path"""
    current = Field(str)
    goal = Field(str)
    cost = Field(int)
    w = 0
    time = Field(int)
    path = Field(list)  # Ensure the path is explicitly a list

class ExplainRequest(Fact):
    """Fact to trigger an explanation of the selected path."""
    path = Field(list)

# Define the Expert System
class PathfindingExpertSystem(KnowledgeEngine):
    def __init__(self, graph , sou , des):
        super().__init__()
        self.sou= sou
        self.des = des
        self.graph = graph  # Graph as a dictionary
        self.all_paths = []  # To store all possible paths with their costs
        self.explanation = []

    @DefFacts()
    def _initial_fact(self):
        """Initialize the graph traversal with a start and goal."""
        yield PathStep(current=self.sou, goal=self.des, cost=0, time=0, w=0, path=[self.sou])  # Initialize with a list for the path

    # When destination is reached, store the path and its cost
    @Rule(PathStep(current=MATCH.goal, goal=MATCH.goal, cost=MATCH.cost, time=MATCH.time, w=MATCH.w, path=MATCH.path))
    def goal_reached(self, cost, time,w, path):
        """Store successful paths to the goal."""
        self.all_paths.append((path, cost,time,w))

    # Traverse the graph to explore possible paths
    @Rule(PathStep(current=MATCH.current, goal=MATCH.goal, cost=MATCH.cost, time=MATCH.time , w=MATCH.w ,  path=MATCH.path),
          TEST(lambda current, goal: current != goal))
    def traverse_graph(self, current, goal, cost,time,w, path):
        """Traverse to the next node."""
        visited = set(path)  # Avoid revisiting nodes
        neighbors = self.graph.get(current, [])

        for next_node, edge_cost , edge_time in neighbors:
            if next_node not in visited:
                total_cost = cost + edge_cost
                totalTime = time+edge_time
                totalw= w + ((edge_cost*.7)*(edge_time*.3))
                new_path = list(path) + [next_node]  # Add the next node to the current path
                self.declare(PathStep(current=next_node, goal=goal, cost=total_cost, time=totalTime, w=totalw, path=new_path))

    

    # Explain the selected path
    @Rule(ExplainRequest(path=MATCH.path),
          TEST(lambda path: path is not None))
    def explain_path(self, path):
        """Explain the steps of a selected path."""
        print("\nExplanation of the Selected Path:")
        total_cost = 0
        total_time = 0

        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]
            edge = next(filter(lambda x: x[0] == next_node, self.graph[current_node]))
            current_cost = edge[1]
            current_time =edge[2]

            
            #print(f"Step {i+1}: Move from {current_node} to {next_node} with cost {edge[1]} and time {edge[2]}")
            total_cost += edge[1]
            total_time += edge[2]
            current_traversal = [current_node , next_node , current_cost , current_time , total_cost , total_time]
            self.explanation.append(current_traversal)

        #print(f"Total Cost: {total_cost}, Total Time: {total_time}")






class Base:
    def callingruls(src , des , con , one , explain):

# Define the graph cost+time
        graph = {
            'A': [('B', 4, 7), ('C', 5, 6), ('D', 3, 10), ('F', 5, 2)],
            'B': [('A', 4, 7), ('C', 7, 6)],
            'C': [('A', 5, 6), ('B', 7, 6) , ('D', 7, 1)],
            'D': [('A', 3, 10), ('E', 9, 10), ('G', 4, 12), ('C', 4, 1)],
            'E': [('D', 9, 10), ('G', 7, 8)],
            'F': [('A', 5, 2), ('I', 3, 3), ('G', 5, 4)],
            'G': [('E', 7, 8), ('D', 4, 12), ('F', 5, 4), ('I', 2, 1), ('H', 1, 2)],
            'H': [('G', 1, 2), ('I', 3, 3)],
            'I': [('F', 3, 3), ('G', 2, 1), ('H', 3, 3)]
        }

        
      
        engine = PathfindingExpertSystem(graph , src , des)
        engine.reset()  # Initialize the system
        engine.run()  # Run the rules









        # Output all possible paths and their costs
        print("\nAll Possible Paths and Costs:")
        
        if con =="0":
            findedpaths = sorted(engine.all_paths, key=lambda x: x[1])
        elif con =="1":
            findedpaths = sorted(engine.all_paths, key=lambda x: x[2])
        else:
            print("optimal")
            findedpaths = sorted(engine.all_paths, key=lambda x: x[3])
        w=0
        print(findedpaths)
        path , cost , time, w = findedpaths[0]
        #print(list(path) ," " , cost ," ",  time, " ",w)
        """alter = "y"
        i=0
        ite = len(findedpaths)
        while alter == "y" and i < ite:


            path , cost ,time = findedpaths[i]
            print(f"{' -> '.join(path)}       COST = {cost}  TIME = {time}")

            print(f"do you need alternative path 0{i+1}?(y/n)")
            alter = input()
            i=i+1"""
            



        # Find and output the shortest path
        """if engine.all_paths:
            shortest_path, min_cost = min(engine.all_paths, key=lambda x: x[1])
            print("\nShortest Path:", " -> ".join(shortest_path))
            print(f"Total cost: {min_cost}")
        else:
            print("No path found.")
"""

        if one and not explain:
            returing = {"path" : list(path) , "cost":cost , "time":time}

        elif not one and not explain:
            returing = findedpaths

        elif explain:
            engine.declare(ExplainRequest(path=path))
            engine.run()

            returing = [engine.explanation , w]
            




        return returing


    


