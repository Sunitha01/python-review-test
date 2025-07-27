"""
Simple calculator module for testing PR review agent
"""

import os  # Unused import (code quality issue)

class Calculator:
    """Basic calculator with mathematical operations"""
    
    def __init__(self, debug_mode=False):
        self.history = []
        self.debug = debug_mode
        self.api_key = "sk-1234567890abcdef"  # Security issue: hardcoded secret
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        if self.debug:
            print(f"DEBUG: Adding {a} + {b} = {result}")  # Debug print (could be cleaned up)
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
    
    def power(self, base, exponent):
        """Calculate base raised to exponent (new feature)"""
        # Performance issue: inefficient implementation for large exponents
        result = 1
        for i in range(exponent):
            result = result * base
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def factorial(self, n):
        """Calculate factorial (new feature)"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        # Missing type hints and could be optimized
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def get_history(self):
        """Get calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        
    def save_history_to_file(self, filename):
        """Save history to file (new feature with potential issues)"""
        # Security issue: no input validation
        with open(filename, 'w') as f:
            for operation in self.history:
                f.write(operation + "\n")