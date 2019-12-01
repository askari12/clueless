package hw4;

/***
    Homework Assignment 4:
    Topological Sort for Class precedence list
    Group name: CLUELESS
    Group members:
    Aliyu Saifullah Vandana
    Haya Shamim Khan Khattak
	Askari Iqbal
	Bilal Siraj
	Muhammad Omer Sahto
*/
     
class Main
{
    
    // Main for executing
    public static void main(String args[])
    {
        /** Test 1
    	Graph  test1 = new Graph(13);    	
    	test1.addEdge("Dwarfs", "Everything");
    	test1.addEdge("Endomorphs", "Dwarfs");
    	test1.addEdge("Athletes", "Dwarfs");
    	test1.addEdge("Shotputters", "Endomorphs");
    	test1.addEdge("Weightlifters", "Athletes");
    	test1.addEdge("Jacque", "Shotputters");
    	test1.addEdge("Jacque", "Weightlifters");
    	test1.addEdge("Programmers", "Dwarfs");
    	test1.addEdge("Teachers", "Dwarfs");
    	test1.addEdge("Eccentrics", "Dwarfs");
    	test1.addEdge("Hackers", "Programmers");
    	test1.addEdge("Professors", "Teachers");
    	test1.addEdge("Professors", "Eccentrics"); 
    	test1.addEdge("Crazy", "Hackers");
    	test1.addEdge("Crazy", "Professors");

        // Test 2
        Graph test2 = new Graph(7);
        test2.addEdge("Dwarfs", "Everything");
        test2.addEdge("Competitors", "Dwarfs");
        test2.addEdge("Diarists", "Dwarfs");
        test2.addEdge("Gourmands", "Dwarfs");
        test2.addEdge("Managers", "Competitors");
        test2.addEdge("Blimpy", "Managers");
        test2.addEdge("Blimpy", "Diarists");
        test2.addEdge("Blimpy", "Gourmands");

        // Output
        System.out.println("\nOUTPUT");
        System.out.println("\nTest data 1");
        test1.topologicalSorting();
        System.out.println("Test data 2");
        test2.topologicalSorting();
        */
    	
    	//Example 1
    	Graph example11 = new Graph(6);
    	example11.addEdge("CAIObject", "Everything");
    	example11.addEdge("CAIActor", "CAIObject");
    	example11.addEdge("CAIPipeUser", "CAIActor");
    	example11.addEdge("CAIPuppet", "CAIPipeUser");
    	example11.addEdge("CAIVehicle", "CAIPuppet");
    	
    	Graph example12 = new Graph(4);
    	example12.addEdge("CAIObject", "Everything");
    	example12.addEdge("CAIActor", "CAIObject");
    	example12.addEdge("CAIPlayer", "CAIActor");
    	
    	//Example 2
    	Graph example21 = new Graph(4);
    	example21.addEdge("ios", "Everything");
    	example21.addEdge("istream", "ios");
    	example21.addEdge("ifstream", "istream");
    	
    	Graph example22 = new Graph(6);
    	example22.addEdge("ios", "Everything");
    	example22.addEdge("ostream", "ios");
    	example22.addEdge("iostream", "ostream");
    	example22.addEdge("fstream", "iostream");
    	example22.addEdge("istream", "ios");
    	example22.addEdge("iostream", "istream"); 
    	example22.addEdge("fstream", "iostream");
    	
    	Graph example23 = new Graph(4);
    	example23.addEdge("ios", "Everything");
    	example23.addEdge("ostream", "ios");
    	example23.addEdge("ofstream", "ostream");
    	
    	//Example 3
    	Graph example31 = new Graph(6);
    	example31.addEdge("Employee", "Everything");
    	example31.addEdge("Manager", "Employee");
    	example31.addEdge("Temporary Employee", "Employee");
    	example31.addEdge("Consultant Manager", "Manager");
    	example31.addEdge("Consultant", "Temporary Employee");
    	example31.addEdge("Consultant Manager", "Consultant");
    	
    	Graph example32 = new Graph(4);
    	example32.addEdge("Employee", "Everything");
    	example32.addEdge("Manager", "Employee");
    	example32.addEdge("Director", "Manager");
    	
    	Graph example33 = new Graph(5);
    	example33.addEdge("Employee", "Everything");
    	example33.addEdge("Permanent Employee", "Employee");
    	example33.addEdge("Manager", "Employee");
    	example33.addEdge("Permanent Manager", "Permanent Employee");
    	example33.addEdge("Permanent Manager", "Manager");
    	
    	System.out.println("\n\nOUTPUT");
        System.out.println("\nExample 1");
        example11.topologicalSorting();
        example12.topologicalSorting();
        
        System.out.println("\nExample 2");
        example21.topologicalSorting();
        example22.topologicalSorting();
        example23.topologicalSorting();
        
        System.out.println("\nExample 3");
        example31.topologicalSorting();
        example32.topologicalSorting();
        example33.topologicalSorting();
    	
    }
}