import heapq

def manage_tasks():
    # Min-heap by default, so we use negative priority to simulate a max-heap
    heap = []
    result = []  # List to store the results of GET operations
    
    operations = int(input("Enter number of operations: "))  # Number of operations
    
    for _ in range(operations):
        command = input().split()
        
        if command[0] == "ADD":
            task_name = command[1]
            priority = int(command[2])
            # Push to heap with negative priority to simulate max-heap
            heapq.heappush(heap, (-priority, task_name))
        
        elif command[0] == "GET":
            # Pop from heap and get the task with the highest priority
            if heap:
                priority, task_name = heapq.heappop(heap)
                result.append(task_name)  # Store the task name in result list
            else:
                result.append("No tasks available")
    
    # Now that all operations are done, print the results of GET operations
    for task in result:
        print(task)

    # To show remaining tasks in correct order
    remaining_tasks = sorted(heap, reverse=True)  # Sort by priority (largest to smallest)
    print("Remaining tasks:", [(task[1], -task[0]) for task in remaining_tasks])

# Run the function
manage_tasks()
