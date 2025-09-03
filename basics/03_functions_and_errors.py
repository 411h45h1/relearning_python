"""
Python Functions and Error Handling
----------------------------------
Functions in Python are similar to JavaScript but with some key differences.
Error handling uses try/except instead of try/catch.
"""

# Basic function (similar to JS but with def keyword and type hints)
def calculate_tax(amount: float, rate: float = 0.08) -> float:
    """Calculate tax amount with optional rate parameter."""
    return amount * rate

print("Tax calculation:")
print(f"Tax on $100: ${calculate_tax(100):.2f}")
print(f"Tax on $100 at 10%: ${calculate_tax(100, 0.10):.2f}")

# Functions with multiple return values (tuples - not possible in JS without objects)
def get_user_stats(users: list) -> tuple:
    """Return user statistics as a tuple."""
    total = len(users)
    active = sum(1 for user in users if user.get("is_active", False))
    return total, active

users_data = [
    {"name": "Alice", "is_active": True},
    {"name": "Bob", "is_active": False},
    {"name": "Charlie", "is_active": True},
]

total_users, active_users = get_user_stats(users_data)  # tuple unpacking
print(f"\nUser stats: {total_users} total, {active_users} active")

# Lambda functions (similar to JS arrow functions)
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"\nLambda examples:")
print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Even numbers: {even_numbers}")

from typing import Union

# Error handling - try/except instead of try/catch
def safe_divide(a: Union[int, float, str], b: Union[int, float, str]) -> float:
    """Safely divide two numbers with error handling."""
    try:
        # Convert to float if they're strings
        num_a = float(a)
        num_b = float(b)
        result = num_a / num_b
        return result
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero!")
        return 0.0
    except (TypeError, ValueError) as e:
        print(f"Error: Invalid types for division: {e}")
        return 0.0
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0.0

print(f"\nSafe division examples:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"'10' / 2 = {safe_divide('10', 2)}")  # Now this works with string input

# Working with JSON-like data (common in APIs)
def process_api_request(data: dict) -> dict:
    """Process API request data with validation."""
    try:
        # Validate required fields
        required_fields = ["user_id", "action"]
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")
        
        # Process the request
        response = {
            "status": "success",
            "user_id": data["user_id"],
            "action": data["action"],
            "timestamp": "2025-09-02T10:30:00Z",
            "processed": True
        }
        
        # Add optional fields if present
        if "metadata" in data:
            response["metadata"] = data["metadata"]
            
        return response
        
    except ValueError as e:
        return {"status": "error", "message": str(e)}
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {str(e)}"}

# Test the API processor
print(f"\nAPI request processing:")

# Valid request
valid_request = {"user_id": 123, "action": "login", "metadata": {"ip": "192.168.1.1"}}
result1 = process_api_request(valid_request)
print(f"Valid request result: {result1}")

# Invalid request
invalid_request = {"user_id": 123}  # missing action
result2 = process_api_request(invalid_request)
print(f"Invalid request result: {result2}")

# Higher-order functions (functions that take/return functions)
def create_validator(min_length: int):
    """Create a validation function with specific rules."""
    def validator(value: str) -> bool:
        return len(value) >= min_length
    return validator

# Create different validators
password_validator = create_validator(8)
username_validator = create_validator(3)

print(f"\nValidation examples:")
print(f"'password123' is valid password: {password_validator('password123')}")
print(f"'pw' is valid password: {password_validator('pw')}")
print(f"'ahmed' is valid username: {username_validator('ahmed')}")
print(f"'ab' is valid username: {username_validator('ab')}")

# Decorators (Python's middleware concept - similar to HOCs in React)
def log_execution(func):
    """Decorator to log function execution."""
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_execution
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

print(f"\nDecorator example:")
result = add_numbers(5, 3)
