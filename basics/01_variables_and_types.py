"""
Python Basics: Variables and Types
----------------------------------
Unlike JavaScript, Python has some different type behaviors and conventions.
Let's explore the differences and similarities.
"""

# Python is dynamically typed like JavaScript, but with some key differences
name = "Ahmed"  # str (similar to JS string)
age = 28        # int (JS would make this a number)
height = 6.0    # float (JS would also make this a number)
is_developer = True  # bool (note: capitalized True/False)

print(f"Name: {name} (type: {type(name).__name__})")  # __name__ is the name of the type
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Is Developer: {is_developer} (type: {type(is_developer).__name__})")

# Python has some types that don't exist in JavaScript
languages = ["Python", "JavaScript", "TypeScript"]  # list (similar to JS array)
skills = {"frontend": "React", "backend": "Django"}  # dict (similar to JS object)
coordinates = (40.7128, -74.0060)  # tuple (immutable sequence)

print(f"\nLanguages: {languages} (type: {type(languages).__name__})")
print(f"Skills: {skills} (type: {type(skills).__name__})")
print(f"Coordinates: {coordinates} (type: {type(coordinates).__name__})")

# String methods - Python has great string handling
email = "ahmed@company.com"
print(f"\nEmail processing:")
print(f"Domain: {email.split('@')[1]}")
print(f"Username: {email.split('@')[0].title()}")
print(f"Is company email: {email.endswith('@company.com')}")

# None is Python's null equivalent
database_connection = None
print(f"\nDatabase connection: {database_connection} (type: {type(database_connection).__name__})")

# Python's truthiness is similar to JavaScript but stricter
print(f"\nTruthiness checks:")
print(f"Empty string is falsy: {bool('')}")
print(f"Empty list is falsy: {bool([])}")
print(f"Zero is falsy: {bool(0)}")
print(f"None is falsy: {bool(None)}")
