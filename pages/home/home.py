from nicegui import ui
import sys
import os

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.page_base import BasePage


class HomePage(BasePage):
    """Home page implementation"""
    
    # Page configuration constants
    PAGE_CONFIG = {
        'page_scripts': [
            ('Home Handler', 'pages/home/home_handler.js')
        ],
        'page_data': [
            ('Home Data', 'pages/home/home_data.json')
        ]
    }
    
    def __init__(self):
        super().__init__('home')


# Create instance and function for backward compatibility
home_page = HomePage()

def create_home_page():
    """Create home page using HTML template as foundation (Angular-like approach)"""
    return home_page.create_page(
        show_script_loader=False,  # Disabled by default
        show_json_loader=False     # Disabled by default
    )

 