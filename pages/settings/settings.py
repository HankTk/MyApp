from nicegui import ui
import sys
import os

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.page_template_loader import load_template
from utils.page_script_loader import load_script, load_json
from utils.page_data_loader import load_page_data

def create_json_loader_section():
    """Create a JSON data loading section for settings page"""
    with ui.card().classes('q-ma-md'):
        ui.label('📄 Settings Data Loader').classes('text-h6 q-mb-md')
        
        # JSON file loading
        json_path = ui.input('JSON Path', placeholder='Enter JSON path (e.g., data/pages/settings_data.json)').classes('q-mb-sm')
        
        def load_json_file():
            if json_path.value:
                data = load_json(json_path.value)
                if data and "error" not in data:
                    ui.notify('JSON data loaded successfully!')
                    with ui.card().classes('q-mt-sm'):
                        ui.label('JSON Data:').classes('text-subtitle2')
                        ui.json_editor(data, on_change=lambda e: ui.notify(f'JSON changed: {e}'))
                else:
                    ui.notify(str(data), type='error')
        
        ui.button('Load JSON', on_click=load_json_file).classes('q-mb-sm')
        
        # Quick load buttons
        ui.label('Quick Load:').classes('text-subtitle2 q-mb-sm')
        
        quick_json_files = [
            ('Settings Data', 'pages/settings/settings_data.json'),
            ('Home Page Data', 'pages/home/home_data.json')
        ]
        
        for name, path in quick_json_files:
            def load_quick_json(p=path):
                json_path.value = p
                load_json_file()
            
            ui.button(f'Load {name}', on_click=load_quick_json).classes('q-mr-sm q-mb-sm')

def create_settings_page():
    """Create settings page using HTML template as foundation (Angular-like approach)"""
    
    # Load page data from JSON file
    page_data = load_page_data('settings')
    
    # Load settings handler script first
    load_script('pages/settings/settings_handler.js')
    
    # Load and render the page using HTML template from file
    template_path = os.path.join(os.path.dirname(__file__), 'settings_template.html')
    html_container = load_template(template_path, page_data)
    
    if html_container:
        # Add JSON loader section
        # create_json_loader_section()
        return html_container
    else:
        # Show message if template loading failed
        ui.label('Settings page could not be loaded.').classes('text-h6 q-mb-md text-center text-red')

 