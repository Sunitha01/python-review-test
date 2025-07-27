"""
Utility functions
"""

def format_number(num):
    """Format number for display (missing type hints)"""
    if num > 1000000:
        return f"{num/1000000:.1f}M"
    elif num > 1000:
        return f"{num/1000:.1f}K" 
    return str(num)

def validate_input(value):
    """Validate numeric input (basic implementation)"""
    try:
        return float(value)
    except:  # Bare except clause (code quality issue)
        return None

def process_large_dataset(data=[]):  # Mutable default argument (code quality issue)
    """Process large dataset"""
    results = []
    for item in data:
        # Performance issue: inefficient loop
        for i in range(1000):
            if item % i == 0:
                results.append(item)
                break
    return results

def get_database_password():
    """Get database password (security issue)"""
    password = "admin123"  # Hardcoded password (security issue)
    return password

def unsafe_file_operation(filename):
    """Unsafe file operation (security issue)"""
    # No input validation - could be exploited
    with open(filename, 'r') as f:
        return f.read()