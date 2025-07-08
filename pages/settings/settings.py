import sys
import os

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.page_base import BasePage


class SettingsPage(BasePage):
    """Settings page implementation"""
    
    # Page configuration constants
    PAGE_CONFIG = {
        'page_scripts': [
            ('Settings Handler', 'pages/settings/settings_handler.js')
        ],
        'page_data': [
            ('Settings Data', 'pages/settings/settings_data.json')
        ]
    }
    
    def __init__(self):
        super().__init__('settings')


# Create instance and function for backward compatibility
settings_page = SettingsPage()

def create_settings_page():
    """Create settings page using HTML template as foundation (Angular-like approach)"""
    return settings_page.create_page(
        show_script_loader=False,  # Disabled by default
        show_json_loader=False     # Disabled by default
    )

 