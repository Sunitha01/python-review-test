"""
Data processing utilities
"""

import json
import csv
from typing import List, Dict, Any

class DataProcessor:
    """Process and analyze data"""
    
    def __init__(self):
        self.processed_data = []
    
    def load_from_csv(self, filepath: str) -> List[Dict[str, Any]]:
        """Load data from CSV file"""
        data = []
        try:
            with open(filepath, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
            self.processed_data = data
            return data
        except FileNotFoundError:
            print(f"File {filepath} not found")
            return []
    
    def save_to_json(self, data: List[Dict[str, Any]], filepath: str) -> bool:
        """Save data to JSON file"""
        try:
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to JSON: {e}")
            return False
    
    def filter_data(self, key: str, value: Any) -> List[Dict[str, Any]]:
        """Filter data by key-value pair"""
        return [item for item in self.processed_data if item.get(key) == value]
    
    def count_by_category(self, category_key: str) -> Dict[str, int]:
        """Count items by category"""
        counts = {}
        for item in self.processed_data:
            category = item.get(category_key, 'Unknown')
            counts[category] = counts.get(category, 0) + 1
        return counts