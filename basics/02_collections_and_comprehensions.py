"""
Python Collections: Lists, Dicts, and Comprehensions
---------------------------------------------------
Coming from JavaScript, you'll find Python's data structures familiar but more powerful.
"""

# Lists (Python's arrays) - more powerful than JS arrays
fruits = ["apple", "banana", "cherry", "date"]
print("Original fruits:", fruits)

# List methods (similar to JS array methods but different syntax)
fruits.append("elderberry")  # like JS push()
print("After append:", fruits)

fruits.insert(1, "blueberry")  # insert at index
print("After insert:", fruits)

# List slicing (powerful feature not in JS)
print("\nList slicing:")
print("First 3 fruits:", fruits[:3])
print("Last 2 fruits:", fruits[-2:])
print("Every other fruit:", fruits[::2])
print("Reverse order:", fruits[::-1])

# List comprehensions (very Pythonic - like JS map/filter combined)
print("\nList comprehensions:")
lengths = [len(fruit) for fruit in fruits]
print("Fruit lengths:", lengths)

long_fruits = [fruit.upper() for fruit in fruits if len(fruit) > 5]
print("Long fruits (uppercase):", long_fruits)

# Dictionaries (Python's objects) - similar to JS objects but keys can be any type
user = {
    "id": 123,
    "name": "Ahmed",
    "email": "ahmed@company.com",
    "roles": ["developer", "reviewer"],
    "is_active": True
}

print(f"\nUser dictionary:")
print(f"User: {user['name']} ({user['email']})")
print(f"Roles: {', '.join(user['roles'])}")

# Dictionary methods
print("\nDictionary operations:")
print("All keys:", list(user.keys()))
print("All values:", list(user.values()))

# Safe access (like JS optional chaining)
department = user.get("department", "Not specified")
print(f"Department: {department}")

# Dictionary comprehension
user_summary = {key: value for key, value in user.items() if key != "id"}
print("User summary (no ID):", user_summary)

# Sets (unique collections - no direct JS equivalent)
print("\nSets (unique collections):")
languages = {"Python", "JavaScript", "Python", "Go", "JavaScript"}
print("Unique languages:", languages)
print("Is Python in set:", "Python" in languages)

# Practical example: processing API-like data
api_response = [
    {"id": 1, "name": "Task 1", "status": "completed", "priority": "high"},
    {"id": 2, "name": "Task 2", "status": "pending", "priority": "low"},
    {"id": 3, "name": "Task 3", "status": "completed", "priority": "medium"},
    {"id": 4, "name": "Task 4", "status": "in_progress", "priority": "high"},
]

print(f"\nProcessing API response ({len(api_response)} tasks):")

# Filter completed tasks (like JS filter)
completed_tasks = [task for task in api_response if task["status"] == "completed"]
print(f"Completed tasks: {len(completed_tasks)}")

# Get high priority task names (like JS filter + map)
high_priority_names = [task["name"] for task in api_response if task["priority"] == "high"]
print(f"High priority tasks: {high_priority_names}")

# Group by status (useful for APIs)
status_groups = {}
for task in api_response:
    status = task["status"]
    if status not in status_groups:
        status_groups[status] = []
    status_groups[status].append(task["name"])

print("Tasks grouped by status:")
for status, tasks in status_groups.items():
    print(f"  {status}: {tasks}")
