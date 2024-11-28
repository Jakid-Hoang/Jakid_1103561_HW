/*Name: Jakid
 * Student ID: 1103561
 * Date of Submission: 11/28/2024
*/

import heapq

def schedule_tasks(tasks, n):
    # Sort tasks by profit in descending order
    tasks.sort(key=lambda x: -x[0])  # Sort by profit (largest first)
    
    # To track available time slots (1 to N), we use a list to represent available slots
    available_slots = [False] * (n + 1)  # Slot availability (1-based index)
    
    # This list will store the scheduled tasks
    scheduled_tasks = []
    total_profit = 0
    
    # Iterate through tasks, try to schedule each one
    for profit, deadline in tasks:
        # Try to find an available slot for the task, starting from its deadline
        for t in range(deadline, 0, -1):
            if not available_slots[t]:
                # Schedule this task in slot t
                available_slots[t] = True
                scheduled_tasks.append(profit)
                total_profit += profit
                break
    
    return total_profit, scheduled_tasks

# Input
n = int(input())  # Number of tasks
tasks = []

for _ in range(n):
    profit, deadline = map(int, input().split())
    tasks.append((profit, deadline))

# Get the result
profit, scheduled = schedule_tasks(tasks, n)

# Output the result
print(f"Maximum Profit: {profit}")
print(f"Scheduled Tasks: {scheduled}")
