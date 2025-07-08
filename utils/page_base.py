from abc import ABC, abstractmethod
from nicegui import ui
import sys
import os
import inspect

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.page_template_loader import load_template
from utils.page_script_loader import load_script, load_json
from utils.page_data_loader import load_page_data


class BasePage(ABC):
    """Abstract base class for page implementations"""
    
    # Default page configuration - can be overridden by subclasses
    PAGE_CONFIG = {
        'page_scripts': [],
        'page_data': []
    }
    
    def __init__(self, page_name: str):
        self.page_name = page_name
        self.page_dir = os.path.dirname(self._get_page_file_path())
    
    def _get_page_file_path(self) -> str:
        """Get the path to the current page file"""
        # Use the page name to construct the path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        page_path = os.path.join(project_root, 'pages', self.page_name, f'{self.page_name}.py')
        return page_path
    
    def create_json_loader_section(self, title: str = None, page_data: list = None):
        """Create a JSON data loading section"""
        if title is None:
            title = f'📄 {self.page_name.title()} Data Loader'
        
        if page_data is None:
            page_data = [
                (f'{self.page_name.title()} Data', f'pages/{self.page_name}/{self.page_name}_data.json'),
            ]
        
        with ui.card().classes('q-ma-md'):
            ui.label(title).classes('text-h6 q-mb-md')
            
            # JSON file loading
            json_path = ui.input('JSON Path', placeholder='Enter JSON path (e.g., pages/home/home_data.json)').classes('q-mb-sm')
            
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
            
            for name, path in page_data:
                def load_quick_json(p=path):
                    json_path.value = p
                    load_json_file()
                
                ui.button(f'Load {name}', on_click=load_quick_json).classes('q-mr-sm q-mb-sm')
    
    def create_script_loader_section(self, page_scripts: list = None):
        """Create a script loading section"""
        if page_scripts is None:
            page_scripts = [
                (f'{self.page_name.title()} Handler', f'pages/{self.page_name}/{self.page_name}_handler.js'),
            ]
        
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
            
            for name, path in page_scripts:
                def load_quick_script(p=path):
                    script_path.value = p
                    load_script_file()
                
                ui.button(f'Load {name}', on_click=load_quick_script).classes('q-mr-sm q-mb-sm')
    
    def create_page(self, template_filename: str = None, handler_script: str = None, 
                   show_script_loader: bool = False, show_json_loader: bool = False):
        """Create page using HTML template as foundation (Angular-like approach)"""
        
        # Load page data from JSON file
        page_data = load_page_data(self.page_name)
        
        # Set default template filename if not provided
        if template_filename is None:
            template_filename = f'{self.page_name}_template.html'
        
        # Set default handler script if not provided
        if handler_script is None:
            handler_script = f'pages/{self.page_name}/{self.page_name}_handler.js'
        
        # Load handler script first
        load_script(handler_script)
        
        # Load and render the page using HTML template from file
        template_path = os.path.join(self.page_dir, template_filename)
        html_container = load_template(template_path, page_data)
        
        if html_container:
            # Add optional sections
            if show_script_loader:
                self.create_script_loader_section()
            
            if show_json_loader:
                self.create_json_loader_section()
            
            return html_container
        else:
            # Show message if template loading failed
            ui.label(f'{self.page_name.title()} page could not be loaded.').classes('text-h6 q-mb-md text-center text-red')
            return None
    
    def get_page_specific_config(self):
        """Return page-specific configuration"""
        # Use the class's PAGE_CONFIG by default
        return self.PAGE_CONFIG 