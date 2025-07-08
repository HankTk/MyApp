from nicegui import ui
import sys
import os

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.template_loader import load_template
from utils.script_loader import load_script, load_json
from utils.page_data_loader import load_page_data

def create_script_loader_section():
    """Create a simple script loading section"""
    with ui.card().classes('q-ma-md'):
        ui.label('📜 Script Loader').classes('text-h6 q-mb-md')
        
        # Script loading
        script_path = ui.input('Script Path', placeholder='Enter script path (e.g., scripts/custom.js)').classes('q-mb-sm')
        
        def load_script_file():
            if script_path.value:
                result = load_script(script_path.value)
                ui.notify(result)
        
        ui.button('Load Script', on_click=load_script_file).classes('q-mb-sm')
        
        # Quick load buttons
        ui.label('Quick Load:').classes('text-subtitle2 q-mb-sm')
        
        quick_scripts = [
            ('Event Handler', 'pages/home/home_handler.js'),
            ('Settings Handler', 'pages/settings/settings_handler.js'),
            ('Custom Functions', 'pages/home/custom.js'),
            ('Data Handler', 'pages/home/data_handler.js')
        ]
        
        for name, path in quick_scripts:
            def load_quick_script(p=path):
                script_path.value = p
                load_script_file()
            
            ui.button(f'Load {name}', on_click=load_quick_script).classes('q-mr-sm q-mb-sm')

def create_json_loader_section():
    """Create a JSON data loading section"""
    with ui.card().classes('q-ma-md'):
        ui.label('📄 JSON Data Loader').classes('text-h6 q-mb-md')
        
        # JSON file loading
        json_path = ui.input('JSON Path', placeholder='Enter JSON path (e.g., data/user_config.json)').classes('q-mb-sm')
        
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
            ('User Config', 'data/user_config.json'),
            ('App Settings', 'data/app_settings.json'),
            ('Sample Data', 'data/sample.json'),
            ('Home Page Data', 'pages/home/home_data.json'),
            ('Settings Page Data', 'pages/settings/settings_data.json')
        ]
        
        for name, path in quick_json_files:
            def load_quick_json(p=path):
                json_path.value = p
                load_json_file()
            
            ui.button(f'Load {name}', on_click=load_quick_json).classes('q-mr-sm q-mb-sm')

def create_home_page():
    """Create home page using HTML template as foundation (Angular-like approach)"""
    
    # Load page data from JSON file
    page_data = load_page_data('home')
    
    # Fallback data if JSON file not found

    
    # Load and render the page using HTML template from file
    template_path = os.path.join(os.path.dirname(__file__), 'home_template.html')
    html_container = load_template(template_path, page_data)
    
    if html_container:
        # Add script loader section
        # create_script_loader_section()
        
        # Add JSON loader section
        # create_json_loader_section()
        
        # Load event handler script
        load_script('pages/home/home_handler.js')
        
        return html_container
    else:
        # Show message if template loading failed
        ui.label('Home page could not be loaded.').classes('text-h6 q-mb-md text-center text-red')

 