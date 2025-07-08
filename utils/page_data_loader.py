import os
import json
from typing import Dict, Any, Optional

class PageDataLoader:
    """Utility class for loading page data from JSON files"""
    
    def __init__(self, data_dir: str = "pages"):
        self.data_dir = data_dir
        self.cached_data = {}
    
    def load_page_data(self, page_name: str) -> Optional[Dict[str, Any]]:
        """Load page data from JSON file"""
        try:
            # Check cache first
            if page_name in self.cached_data:
                return self.cached_data[page_name]
            
            # Construct file path - now pages have their data in their own directories
            file_path = os.path.join("pages", page_name, f"{page_name}_data.json")
            
            # Load JSON data
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Cache the data
            self.cached_data[page_name] = data
            
            return data
            
        except FileNotFoundError:
            print(f"Page data file not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Invalid JSON in page data file: {e}")
            return None
        except Exception as e:
            print(f"Error loading page data: {e}")
            return None
    
    def load_custom_data(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Load custom JSON data from any file path"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Data file not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Invalid JSON in data file: {e}")
            return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def save_page_data(self, page_name: str, data: Dict[str, Any]) -> bool:
        """Save page data to JSON file"""
        try:
            file_path = os.path.join("pages", page_name, f"{page_name}_data.json")
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            # Save data
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Update cache
            self.cached_data[page_name] = data
            
            return True
            
        except Exception as e:
            print(f"Error saving page data: {e}")
            return False
    
    def get_available_pages(self) -> list:
        """Get list of available page data files"""
        try:
            pages_dir = "pages"
            if not os.path.exists(pages_dir):
                return []
            
            pages = []
            for page_dir in os.listdir(pages_dir):
                page_path = os.path.join(pages_dir, page_dir)
                if os.path.isdir(page_path):
                    data_file = os.path.join(page_path, f"{page_dir}_data.json")
                    if os.path.exists(data_file):
                        pages.append(page_dir)
            
            return pages
        except Exception as e:
            print(f"Error getting available pages: {e}")
            return []
    
    def clear_cache(self):
        """Clear the data cache"""
        self.cached_data.clear()

# Global instance
page_data_loader = PageDataLoader()

# Convenience functions
def load_page_data(page_name: str) -> Optional[Dict[str, Any]]:
    """Load page data from JSON file"""
    return page_data_loader.load_page_data(page_name)

def load_custom_data(file_path: str) -> Optional[Dict[str, Any]]:
    """Load custom JSON data from any file path"""
    return page_data_loader.load_custom_data(file_path)

def save_page_data(page_name: str, data: Dict[str, Any]) -> bool:
    """Save page data to JSON file"""
    return page_data_loader.save_page_data(page_name, data)

def get_available_pages() -> list:
    """Get list of available page data files"""
    return page_data_loader.get_available_pages() 