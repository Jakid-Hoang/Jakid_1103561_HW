# Jakid_1103561_HW

Question 1: Binary Tree - Find the Diameter of a Binary Tree
Problem Statement:
Write a program to calculate the diameter of a binary tree. The diameter of a binary tree is the length of the longest path between any two nodes in the tree. The path may or may not pass through the root.

You are required to:

Build the binary tree using level-order input. Use -1 to represent null nodes.
Implement a function to calculate the diameter of the binary tree efficiently using recursion.
Input Format:

The first line contains a list of integers representing the level-order traversal of the binary tree. Use -1 for null nodes.
Output Format:

Print an integer representing the diameter of the binary tree.
Example Input:[3, 6, 9, -1, 7, -1, 10, 4, -1]
4

Question 2: Heap Sort - Build a Priority Queue for Tasks
Problem Statement:
Write a program to manage a task priority queue using a max heap. Each task has a name and a priority level. Your program should allow:

Add a Task: Add a task with a given priority.
Get the Highest Priority Task: Remove and return the task with the highest priority.
Display the Remaining Tasks: Print the remaining tasks in descending order of priority.
Input Format:

The first line contains an integer N, the number of operations.
The next N lines contain either:
"ADD task_name priority" to add a task.
"GET" to fetch the highest-priority task.
Output Format:

For every "GET" operation, print the name of the task with the highest priority.
At the end, print the list of remaining tasks in descending order of priority.
Example Input: 5
ADD TaskA 30
ADD TaskB 20
GET
ADD TaskC 25
GET
TaskA
TaskC
Remaining tasks: [('TaskB', 20)]


Question 3: Merge K Sorted Arrays Using Min Priority Queue
Problem Statement:
You are given K sorted arrays of integers. Write a Python program to merge these arrays into a single sorted array using a Min Priority Queue.

Your program should:

Insert the first element of each array into a Min Priority Queue along with the array index and element index.
Extract the smallest element from the queue, add it to the result array, and insert the next element from the same array into the queue.
Continue this process until all elements from all arrays are merged.
Input Format:

An integer K, the number of sorted arrays.
K sorted arrays, each entered on a new line, with elements separated by spaces.
Output Format:

A single line containing the merged sorted array.
Example Input: 4
2 3 9
1 5 6
7 8 10
4 11 12
Example Output:

Merged Array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]



Question 4: Schedule Tasks with Deadlines Using Max Priority Queue
Problem Statement:
You are given N tasks, each with a profit and a deadline. Write a Python program to schedule the tasks such that the maximum profit is achieved, using a Max Priority Queue.
Each task must be completed within its deadline (1-based index), and only one task can be scheduled at a time.

Input Format:

An integer N, the number of tasks.
N lines containing two integers each: profit and deadline of a task.
Output Format:

The maximum profit that can be achieved.
The list of scheduled tasks in the order they are executed.
Example Input: 5
80 3
50 2
60 3
70 2
90 1
Example Output:
Maximum Profit: 230
Scheduled Tasks: [90, 80, 60]

