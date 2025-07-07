from nicegui import ui
import sys
import os

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.template_engine import render_template, render_string

def create_settings_page():
    """Create settings page using HTML template as foundation (Angular-like approach)"""
    
    # Page data (like Angular component data)
    page_data = {
        'title': 'MyApp - Settings',
        'header_title': '⚙️ Settings',
        'header_subtitle': 'Configure your application preferences',
        'app_name': 'MyApp',
        'settings': {
            'general': {
                'theme': 'Light',
                'language': 'English',
                'notifications': True
            },
            'account': {
                'username': 'user123',
                'email': 'user@example.com'
            },
            'application': {
                'autosave': True,
                'retention_period': '30 days'
            }
        },
        'themes': ['Light', 'Dark', 'Auto'],
        'languages': ['English', 'Japanese', 'Spanish'],
        'retention_options': ['30 days', '60 days', '90 days', '1 year']
    }
    
    try:
        # Render the page using HTML template (without script tags)
        # Use the current directory (pages/settings) as the templates directory
        current_dir = os.path.dirname(__file__)
        
        # Read the template and remove script tags
        template_path = os.path.join(current_dir, 'settings_template.html')
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        # Remove script tags from the template
        import re
        template_content = re.sub(r'<script[^>]*>.*?</script>', '', template_content, flags=re.DOTALL)
        
        # Render the cleaned template
        rendered_html = render_string(template_content, page_data)
        
        # Inject the HTML into NiceGUI
        html_container = ui.html(rendered_html).style('width: 100%;')
        
        # Add JavaScript event handlers using add_body_html
        ui.add_body_html("""
        <script>
        function handleThemeChange(value) {
            window.parent.postMessage({type: 'theme_change', value: value}, '*');
        }
        
        function handleLanguageChange(value) {
            window.parent.postMessage({type: 'language_change', value: value}, '*');
        }
        
        function handleNotificationChange(value) {
            window.parent.postMessage({type: 'notification_change', value: value}, '*');
        }
        
        function handlePasswordChange() {
            window.parent.postMessage({type: 'password_change'}, '*');
        }
        
        function handleAutosaveChange(value) {
            window.parent.postMessage({type: 'autosave_change', value: value}, '*');
        }
        
        function handleRetentionChange(value) {
            window.parent.postMessage({type: 'retention_change', value: value}, '*');
        }
        
        function handleSaveSettings() {
            const settings = {
                theme: document.getElementById('theme-select').value,
                language: document.getElementById('language-select').value,
                notifications: document.getElementById('notification-toggle').checked,
                username: document.getElementById('username-input').value,
                email: document.getElementById('email-input').value,
                autosave: document.getElementById('autosave-toggle').checked,
                retention: document.getElementById('retention-select').value
            };
            window.parent.postMessage({type: 'save_settings', settings: settings}, '*');
        }
        
        function handleResetSettings() {
            window.parent.postMessage({type: 'reset_settings'}, '*');
        }
        
        window.addEventListener('message', function(event) {
            const data = event.data;
            
            switch(data.type) {
                case 'theme_change':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: `Theme changed to: ${data.value}`
                    }, '*');
                    break;
                    
                case 'language_change':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: `Language changed to: ${data.value}`
                    }, '*');
                    break;
                    
                case 'notification_change':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: `Notifications: ${data.value ? 'On' : 'Off'}`
                    }, '*');
                    break;
                    
                case 'password_change':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: 'Password change dialog opened!'
                    }, '*');
                    break;
                    
                case 'autosave_change':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: `Auto Save: ${data.value ? 'On' : 'Off'}`
                    }, '*');
                    break;
                    
                case 'retention_change':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: `Data retention changed to: ${data.value}`
                    }, '*');
                    break;
                    
                case 'save_settings':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: 'Settings saved successfully!'
                    }, '*');
                    break;
                    
                case 'reset_settings':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: 'Settings reset to default!'
                    }, '*');
                    break;
            }
        });
        </script>
        """)
        
        return html_container
        
    except FileNotFoundError as e:
        # Fallback to NiceGUI components if template not found
        ui.label('❌ Template file not found').classes('text-h6 text-red')
        ui.label(str(e)).classes('text-caption')
        
        # Create fallback page with NiceGUI components
        create_fallback_settings_page()
        
    except Exception as e:
        ui.label(f'❌ Error rendering template: {str(e)}').classes('text-h6 text-red')
        create_fallback_settings_page()

def create_fallback_settings_page():
    """Fallback settings page using pure NiceGUI components"""
    ui.label('⚙️ Settings').classes('text-h4 q-mb-md text-center')
    ui.label('Configure your application preferences.').classes('text-body1 q-mb-lg text-center')
    
    with ui.row().classes('full-width justify-center'):
        with ui.card().classes('q-ma-md'):
            ui.label('🔧 General Settings').classes('text-h6')
            ui.select(['Light', 'Dark', 'Auto'], label='Theme', value='Light')
            ui.select(['English', 'Japanese', 'Spanish'], label='Language', value='English')
            ui.switch('Notifications', value=True)
    
    with ui.row().classes('full-width justify-center'):
        with ui.card().classes('q-ma-md'):
            ui.label('👤 Account Settings').classes('text-h6')
            ui.input('Username', value='user123')
            ui.input('Email', value='user@example.com')
            ui.button('Change Password', on_click=lambda: ui.notify('Password change dialog opened!'))
    
    with ui.row().classes('full-width justify-center'):
        with ui.card().classes('q-ma-md'):
            ui.label('📱 Application Settings').classes('text-h6')
            ui.switch('Auto Save', value=True)
            ui.select(['30 days', '60 days', '90 days', '1 year'], label='Data Retention', value='30 days')
    
    with ui.row().classes('full-width justify-center q-mt-lg'):
        ui.button('💾 Save Settings', on_click=lambda: ui.notify('Settings saved successfully!')).classes('q-mr-sm')
        ui.button('🔄 Reset to Default', on_click=lambda: ui.notify('Settings reset to default!')) 