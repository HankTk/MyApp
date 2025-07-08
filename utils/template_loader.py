import os
from nicegui import ui
from utils.template_engine import render_template, render_string

class TemplateLoader:
    """Utility class for loading HTML templates from files"""
    
    def __init__(self):
        self.loaded_templates = {}
    
    def load_template_from_file(self, template_path, variables=None):
        """Load HTML template from file and render with variables"""
        try:
            # Check if template was already loaded
            if template_path in self.loaded_templates:
                template_content = self.loaded_templates[template_path]
            else:
                # Read template content
                with open(template_path, 'r', encoding='utf-8') as f:
                    template_content = f.read()
                self.loaded_templates[template_path] = template_content
            
            # Render template with variables
            if variables:
                rendered_html = render_string(template_content, variables)
            else:
                rendered_html = template_content
            
            # Inject the HTML into NiceGUI
            html_container = ui.html(rendered_html).style('width: 100%;')
            return html_container
            
        except FileNotFoundError:
            ui.label(f'❌ Template file not found: {template_path}').classes('text-h6 text-red')
            return None
        except Exception as e:
            ui.label(f'❌ Error loading template: {str(e)}').classes('text-h6 text-red')
            return None
    
    def get_template_content(self, template_path):
        """Get template content without rendering"""
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"Template file not found: {template_path}"
        except Exception as e:
            return f"Error reading template: {str(e)}"
    
    def render_template_string(self, template_string, variables=None):
        """Render template string with variables"""
        try:
            if variables:
                rendered_html = render_string(template_string, variables)
            else:
                rendered_html = template_string
            
            html_container = ui.html(rendered_html).style('width: 100%;')
            return html_container
            
        except Exception as e:
            ui.label(f'❌ Error rendering template: {str(e)}').classes('text-h6 text-red')
            return None

# Global instance
template_loader = TemplateLoader()

# Convenience functions
def load_template(template_path, variables=None):
    """Load and render HTML template from file"""
    return template_loader.load_template_from_file(template_path, variables)

def get_template_content(template_path):
    """Get template content without rendering"""
    return template_loader.get_template_content(template_path)

def render_template_string(template_string, variables=None):
    """Render template string with variables"""
    return template_loader.render_template_string(template_string, variables) 