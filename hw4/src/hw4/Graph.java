package hw4;

import java.util.*;

public class Graph {
	// Properties
	int vertices;
	LinkedList<String>[] adjList;
	ArrayList<String> vertice;

	/**
            Constructs the graph object with
            the given number of vertices
            @param vertices: number of vertices
	 */
	
	@SuppressWarnings({ "unchecked", "rawtypes" })
	Graph(int vertices)
	{
		this.vertices = vertices;
		adjList = new LinkedList[vertices];
		vertice = new ArrayList<>();
		for (int i = 0; i < vertices; i++)
		{
			adjList[i] = new LinkedList();
		}
	}

	/**
            Method addEdge: Adds an edge to the graph structure
            given the source and destination names
            @param source: source node name
            @param destination: destination node name
	 */
	void addEdge(String source, String destination)
	{
		if(vertice.size() == 0)
		{
			vertice.add(source);
		}
		boolean foundS = false;
		int i;
		for(i = 0; i < vertice.size(); i++)
		{
			if (vertice.get(i).equals(source))
			{
				foundS = true;
				break;
			}
		}

		if(!foundS)
		{
			vertice.add(source);
			//System.out.println("Source " + i + ": " + source);
		}

		adjList[i].add(destination);

		boolean foundD = false;
		for(i = 0; i < vertice.size(); i++)
		{
			if (vertice.get(i).equals(destination))
			{
				foundD = true;
				break;
			}
		}

		if(!foundD)
		{
			vertice.add(destination);
		}
	}

	/**
            Topological sort algorithm
	 */
	void topologicalSorting()
	{
		boolean[] visited = new boolean[vertices];
		for (int i = 0; i < vertices; i++)
			visited[i] = false;

		@SuppressWarnings("rawtypes")
		Stack stack = new Stack<>();

		//visit from each node if not already visited
		for (int i = 0; i < vertices; i++)
		{
			if (!visited[i])
			{
				topologicalSortUtil(i, visited, stack);
			}
		}

		System.out.println("---Topological Sort--- (from highest to lowest)\n");

		// Printing the output
		int size = stack.size();
		int popped;
		for (int i = 0; i < size ; i++)
		{
			popped = (int) stack.pop();
			System.out.println((i+1) + ") " + vertice.get(popped));
		}
		System.out.println("\n------------------------------------\n");

	}

	/**
            Helper method for implementing Topoogical sort algorithm
            @param start: start index for the sort
            @param visited: the array of visited nodes
            @param stack: stack for managing the class precedence
	 */
	@SuppressWarnings({ "rawtypes", "unchecked" })
	private void topologicalSortUtil(int start, boolean[] visited, Stack stack)
	{
		visited[start] = true;

		String i;
		int j;
		Iterator<String> it = adjList[start].iterator();
		while(it.hasNext())
		{
			i = it.next();
			for(j = 0; j < vertice.size(); j++)
				if(vertice.get(j).equals(i))
					if (!visited[j])
						topologicalSortUtil(j, visited, stack);
		}

		stack.push(start);
	}
}
