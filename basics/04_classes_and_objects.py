"""
Python Classes and Objects
-------------------------
Object-oriented programming in Python. Similar concepts to JavaScript classes
but with some Python-specific features and conventions.
"""

from typing import Optional

# Basic class definition
class User:
    """A simple User class demonstrating Python OOP concepts."""
    
    # Class variable (shared by all instances)
    total_users = 0
    
    def __init__(self, name: str, email: str, role: str = "user"):
        """Constructor method (like constructor in JS classes)."""
        self.name = name
        self.email = email
        self.role = role
        self.is_active = True
        self._login_count = 0  # "private" attribute (convention with underscore)
        
        # Increment class variable
        User.total_users += 1
    
    def login(self) -> str:
        """Instance method for user login."""
        self._login_count += 1
        return f"{self.name} logged in (login #{self._login_count})"
    
    def get_info(self) -> dict:
        """Return user information as a dictionary."""
        return {
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "is_active": self.is_active,
            "login_count": self._login_count
        }
    
    def __str__(self) -> str:
        """String representation (like toString in JS)."""
        return f"User({self.name}, {self.role})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"User(name='{self.name}', email='{self.email}', role='{self.role}')"
    
    @classmethod
    def from_dict(cls, data: dict):
        """Class method to create User from dictionary (like a factory)."""
        return cls(data["name"], data["email"], data.get("role", "user"))
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Static method for email validation."""
        return "@" in email and "." in email.split("@")[1]

# Create user instances
print("Creating users:")
user1 = User("Ahmed", "ahmed@company.com", "developer")
user2 = User("Sarah", "sarah@company.com", "admin")

print(f"User 1: {user1}")
print(f"User 2: {user2}")
print(f"Total users created: {User.total_users}")

# Use instance methods
print(f"\nUser interactions:")
print(user1.login())
print(user1.login())
print(user2.login())

# Get user info
print(f"\nUser info:")
print(f"Ahmed's info: {user1.get_info()}")

# Use class method
user_data = {"name": "Mike", "email": "mike@company.com", "role": "manager"}
user3 = User.from_dict(user_data)
print(f"\nUser from dict: {user3}")

# Use static method
print(f"\nEmail validation:")
print(f"Valid email 'test@example.com': {User.is_valid_email('test@example.com')}")
print(f"Invalid email 'invalid-email': {User.is_valid_email('invalid-email')}")

# Inheritance (similar to extends in JavaScript)
class Developer(User):
    """Developer class inheriting from User."""
    
    def __init__(self, name: str, email: str, languages: Optional[list] = None):
        super().__init__(name, email, "developer")  # Call parent constructor
        self.languages = languages or []
        self.projects = []
    
    def add_language(self, language: str) -> None:
        """Add a programming language to developer's skills."""
        if language not in self.languages:
            self.languages.append(language)
    
    def assign_project(self, project_name: str) -> str:
        """Assign a project to the developer."""
        self.projects.append(project_name)
        return f"{self.name} assigned to project: {project_name}"
    
    def get_info(self) -> dict:
        """Override parent method to include developer-specific info."""
        info = super().get_info()  # Get parent info
        info.update({
            "languages": self.languages,
            "projects": self.projects
        })
        return info
    
    def __str__(self) -> str:
        """Override string representation."""
        return f"Developer({self.name}, {len(self.languages)} languages, {len(self.projects)} projects)"

# Create a developer
print(f"\nInheritance example:")
dev = Developer("Alex", "alex@company.com", ["Python", "JavaScript"])
print(f"Developer: {dev}")

dev.add_language("Go")
project_msg = dev.assign_project("API Refactor")
print(project_msg)

print(f"Developer info: {dev.get_info()}")

# Property decorators (like getters/setters)
class Product:
    """Product class demonstrating properties."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price  # "private" attribute
    
    @property
    def price(self) -> float:
        """Getter for price."""
        return self._price
    
    @price.setter
    def price(self, value: float) -> None:
        """Setter for price with validation."""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @property
    def formatted_price(self) -> str:
        """Computed property (like a getter in JS)."""
        return f"${self._price:.2f}"

# Using properties
print(f"\nProperty example:")
product = Product("Laptop", 999.99)
print(f"Product: {product.name} - {product.formatted_price}")

# Using setter
product.price = 899.99
print(f"After discount: {product.formatted_price}")

# Error handling with setter
try:
    product.price = -100
except ValueError as e:
    print(f"Price validation error: {e}")

# Context managers (Python's try-with-resources, like useEffect cleanup)
class DatabaseConnection:
    """Simulate a database connection with context manager."""
    
    def __init__(self, host: str):
        self.host = host
        self.connected = False
    
    def __enter__(self):
        """Called when entering 'with' block."""
        self.connected = True
        print(f"Connected to database at {self.host}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block (even if error occurs)."""
        self.connected = False
        print(f"Disconnected from database at {self.host}")
    
    def query(self, sql: str) -> str:
        """Simulate a database query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")
        return f"Query result for: {sql}"

# Using context manager
print(f"\nContext manager example:")
with DatabaseConnection("localhost:5432") as db:
    result = db.query("SELECT * FROM users")
    print(result)
# Connection automatically closed here

print(f"Total users at end: {User.total_users}")
