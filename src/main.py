"""
Main application entry point
"""

from calculator import Calculator
from data_processor import DataProcessor

def main():
    """Main function to demonstrate functionality"""
    print("Python Review Test Application")
    print("=" * 30)
    
    # Test calculator
    calc = Calculator()
    print("\n🧮 Calculator Demo:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    print("\n📊 Calculator History:")
    for operation in calc.get_history():
        print(f"  {operation}")
    
    # Test data processor
    processor = DataProcessor()
    print("\n📁 Data Processor Demo:")
    sample_data = [
        {"name": "Alice", "age": 30, "department": "Engineering"},
        {"name": "Bob", "age": 25, "department": "Marketing"},
        {"name": "Charlie", "age": 35, "department": "Engineering"}
    ]
    
    processor.processed_data = sample_data
    engineering = processor.filter_data("department", "Engineering")
    print(f"Engineering employees: {len(engineering)}")
    
    counts = processor.count_by_category("department")
    print(f"Department counts: {counts}")

if __name__ == "__main__":
    main()