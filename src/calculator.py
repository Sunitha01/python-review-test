"""
Simple calculator module for testing PR review agent
"""

class Calculator:
    """Basic calculator with mathematical operations"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []