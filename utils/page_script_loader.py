import os
import json
from nicegui import ui

class PageScriptLoader:
    """Utility class for loading and executing JavaScript scripts from files"""
    
    def __init__(self):
        self.loaded_scripts = set()
    
    def load_script_from_file(self, script_path):
        """Load and execute JavaScript from a file"""
        try:
            # Check if script was already loaded
            if script_path in self.loaded_scripts:
                return f"Script already loaded: {script_path}"
            
            # Read script content
            with open(script_path, 'r', encoding='utf-8') as f:
                script_content = f.read()
            
            # Inject the script into the page
            ui.add_head_html(f"<script>{script_content}</script>")
            
            # Mark as loaded
            self.loaded_scripts.add(script_path)
            
            return f"Script loaded successfully: {script_path}"
            
        except FileNotFoundError:
            return f"Script file not found: {script_path}"
        except Exception as e:
            return f"Error loading script: {str(e)}"
    
    def load_json_from_file(self, json_path):
        """Load JSON data from a file"""
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            return {"error": f"JSON file not found: {json_path}"}
        except json.JSONDecodeError as e:
            return {"error": f"Invalid JSON format: {str(e)}"}
        except Exception as e:
            return {"error": f"Error loading JSON: {str(e)}"}
    
    def execute_script(self, script_code):
        """Execute JavaScript code directly"""
        try:
            ui.add_head_html(f"<script>{script_code}</script>")
            return "Script executed successfully"
        except Exception as e:
            return f"Script execution error: {str(e)}"
    
    def get_script_content(self, script_path):
        """Get script content without executing it"""
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"Script file not found: {script_path}"
        except Exception as e:
            return f"Error reading script: {str(e)}"

# Global instance
script_loader = PageScriptLoader()

# Convenience functions
def load_script(script_path):
    """Load and execute a JavaScript script from file"""
    return script_loader.load_script_from_file(script_path)

def load_json(json_path):
    """Load JSON data from file"""
    return script_loader.load_json_from_file(json_path)

def execute_script(script_code):
    """Execute JavaScript code"""
    return script_loader.execute_script(script_code)

def get_script_content(script_path):
    """Get script content without executing"""
    return script_loader.get_script_content(script_path) 