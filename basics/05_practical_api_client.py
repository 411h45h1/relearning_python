"""
Practical Exercise: Simple API Client
------------------------------------
A practical example combining all Python concepts we've learned.
This simulates working with APIs - common in backend development.
"""

import json
from typing import Dict, List, Optional, Union
from datetime import datetime

class APIClient:
    """A simple API client demonstrating Python best practices."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')  # Remove trailing slash
        self.api_key = api_key
        self.session_data = {}
        self._request_count = 0
    
    def _make_request(self, endpoint: str, method: str = "GET", data: Optional[Dict] = None) -> Dict:
        """Simulate making an HTTP request."""
        self._request_count += 1
        
        # Simulate request processing
        print(f"[{method}] {self.base_url}{endpoint}")
        
        # Simulate different responses based on endpoint
        if endpoint.startswith("/users"):
            return self._handle_users_endpoint(endpoint, method, data)
        elif endpoint.startswith("/auth"):
            return self._handle_auth_endpoint(endpoint, method, data)
        else:
            return {"error": "Endpoint not found", "status": 404}
    
    def _handle_users_endpoint(self, endpoint: str, method: str, data: Optional[Dict]) -> Dict:
        """Handle users API endpoints."""
        if method == "GET" and endpoint == "/users":
            return {
                "status": 200,
                "data": [
                    {"id": 1, "name": "Alice", "email": "alice@example.com", "active": True},
                    {"id": 2, "name": "Bob", "email": "bob@example.com", "active": False},
                    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "active": True},
                ]
            }
        elif method == "POST" and endpoint == "/users" and data:
            # Simulate creating a user
            new_user = {
                "id": 999,  # Simulated ID
                "name": data.get("name"),
                "email": data.get("email"),
                "active": True,
                "created_at": datetime.now().isoformat()
            }
            return {"status": 201, "data": new_user}
        else:
            return {"error": "Invalid users endpoint", "status": 400}
    
    def _handle_auth_endpoint(self, endpoint: str, method: str, data: Optional[Dict]) -> Dict:
        """Handle authentication endpoints."""
        if method == "POST" and endpoint == "/auth/login" and data:
            username = data.get("username")
            password = data.get("password")
            
            # Simulate authentication
            if username == "admin" and password == "secret":
                token = f"token_for_{username}_{self._request_count}"
                self.session_data["token"] = token
                return {
                    "status": 200,
                    "data": {"token": token, "expires_in": 3600}
                }
            else:
                return {"error": "Invalid credentials", "status": 401}
        else:
            return {"error": "Invalid auth endpoint", "status": 400}
    
    def get_users(self) -> List[Dict]:
        """Get all users from the API."""
        try:
            response = self._make_request("/users")
            if response.get("status") == 200:
                return response.get("data", [])
            else:
                raise APIError(f"Failed to get users: {response.get('error')}")
        except Exception as e:
            print(f"Error getting users: {e}")
            return []
    
    def create_user(self, name: str, email: str) -> Optional[Dict]:
        """Create a new user."""
        if not self._is_valid_email(email):
            raise ValueError(f"Invalid email format: {email}")
        
        user_data = {"name": name, "email": email}
        response = self._make_request("/users", "POST", user_data)
        
        if response.get("status") == 201:
            return response.get("data")
        else:
            raise APIError(f"Failed to create user: {response.get('error')}")
    
    def login(self, username: str, password: str) -> bool:
        """Authenticate with the API."""
        auth_data = {"username": username, "password": password}
        response = self._make_request("/auth/login", "POST", auth_data)
        
        if response.get("status") == 200:
            print(f"Login successful! Token: {self.session_data.get('token')}")
            return True
        else:
            print(f"Login failed: {response.get('error')}")
            return False

    @staticmethod  # Marks the method as a static method, meaning it does not access or modify class or instance state.
    def _is_valid_email(email: str) -> bool:
        """Validate email format."""
        return "@" in email and "." in email.split("@")[1]
    
    def get_stats(self) -> Dict:
        """Get client statistics."""
        return {
            "requests_made": self._request_count,
            "base_url": self.base_url,
            "authenticated": "token" in self.session_data,
            "session_data": self.session_data
        }

class APIError(Exception):
    """Custom exception for API errors."""
    pass

class UserManager:
    """Higher-level user management using the API client."""
    
    def __init__(self, api_client: APIClient):
        self.api = api_client
        self.users_cache = []
        self.last_fetch = None
    
    def refresh_users(self) -> None:
        """Refresh the users cache."""
        self.users_cache = self.api.get_users()
        self.last_fetch = datetime.now()
        print(f"Refreshed {len(self.users_cache)} users from API")
    
    def get_active_users(self) -> List[Dict]:
        """Get only active users."""
        if not self.users_cache:
            self.refresh_users()
        
        return [user for user in self.users_cache if user.get("active", False)]
    
    def find_user_by_email(self, email: str) -> Optional[Dict]:
        """Find a user by email address."""
        if not self.users_cache:
            self.refresh_users()
        
        for user in self.users_cache:
            if user.get("email") == email:
                return user
        return None
    
    def create_and_add_user(self, name: str, email: str) -> Optional[Dict]:
        """Create a user and add to cache."""
        try:
            new_user = self.api.create_user(name, email)
            if new_user:
                self.users_cache.append(new_user)
                print(f"Created and cached user: {new_user['name']}")
                return new_user
            return None
        except (APIError, ValueError) as e:
            print(f"Failed to create user: {e}")
            raise
    
    def get_user_summary(self) -> Dict:
        """Get summary statistics about users."""
        if not self.users_cache:
            self.refresh_users()
        
        total = len(self.users_cache)
        active = len(self.get_active_users())
        
        # Get email domains
        domains = {}
        for user in self.users_cache:
            email = user.get("email", "")
            if "@" in email:
                domain = email.split("@")[1]
                domains[domain] = domains.get(domain, 0) + 1
        
        return {
            "total_users": total,
            "active_users": active,
            "inactive_users": total - active,
            "email_domains": domains,
            "last_refresh": self.last_fetch.isoformat() if self.last_fetch else None
        }

# Main execution - demonstrate the API client
def main():
    """Main function demonstrating the API client usage."""
    print("=== Python API Client Demo ===\n")
    
    # Initialize API client
    client = APIClient("https://api.example.com", "secret-api-key")
    
    # Authenticate
    print("1. Authentication:")
    login_success = client.login("admin", "secret")
    print(f"Login result: {login_success}\n")
    
    # Initialize user manager
    user_manager = UserManager(client)
    
    # Get users
    print("2. Fetching users:")
    user_manager.refresh_users()
    
    active_users = user_manager.get_active_users()
    print(f"Active users: {[user['name'] for user in active_users]}\n")
    
    # Find specific user
    print("3. Finding user:")
    alice = user_manager.find_user_by_email("alice@example.com")
    if alice:
        print(f"Found user: {alice['name']} (ID: {alice['id']})\n")
    
    # Create new user
    print("4. Creating new user:")
    try:
        new_user = user_manager.create_and_add_user("David", "david@example.com")
        print(f"New user created: {new_user}\n")
    except Exception as e:
        print(f"Error creating user: {e}\n")
    
    # Get summary
    print("5. User summary:")
    summary = user_manager.get_user_summary()
    print(json.dumps(summary, indent=2))
    
    # Show client stats
    print(f"\n6. Client statistics:")
    stats = client.get_stats()
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()
