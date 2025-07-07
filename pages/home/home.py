from nicegui import ui
import sys
import os

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.template_engine import render_template

def create_home_page():
    """Create home page using HTML template as foundation (Angular-like approach)"""
    
    # Page data (like Angular component data)
    page_data = {
        'title': 'MyApp - Home',
        'header_title': '🏠 Welcome to MyApp',
        'header_subtitle': 'Your application dashboard',
        'app_name': 'MyApp',
        'stats': {
            'total_items': 123,
            'active_users': 45,
            'success_rate': '89%'
        },
        'features': [
            {
                'icon': '📊',
                'title': 'Dashboard',
                'description': 'View your application statistics and overview.',
                'action': 'dashboard'
            },
            {
                'icon': '📝',
                'title': 'Recent Activity',
                'description': 'Check your recent activities and updates.',
                'action': 'activity'
            },
            {
                'icon': '🚀',
                'title': 'Quick Actions',
                'description': 'Access frequently used features quickly.',
                'action': 'quickstart'
            }
        ]
    }
    
    try:
        # Render the page using HTML template
        # Use the current directory (pages/home) as the templates directory
        current_dir = os.path.dirname(__file__)
        rendered_html = render_template('home_template.html', page_data, templates_dir=current_dir)
        
        # Inject the HTML into NiceGUI
        html_container = ui.html(rendered_html).style('width: 100%;')
        
        # Add JavaScript event handlers (like Angular event binding)
        ui.add_head_html("""
        <script>
        window.addEventListener('message', function(event) {
            const data = event.data;
            
            switch(data.type) {
                case 'dashboard':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: 'Dashboard opened!'
                    }, '*');
                    break;
                    
                case 'activity':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: 'Activity log opened!'
                    }, '*');
                    break;
                    
                case 'quickstart':
                    window.parent.postMessage({
                        type: 'nicegui_notify',
                        message: 'Quick start initiated!'
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
        create_fallback_home_page()
        
    except Exception as e:
        ui.label(f'❌ Error rendering template: {str(e)}').classes('text-h6 text-red')
        create_fallback_home_page()

def create_fallback_home_page():
    """Fallback home page using pure NiceGUI components"""
    ui.label('🏠 Welcome to MyApp').classes('text-h4 q-mb-md text-center')
    ui.label('This is the home page of your application.').classes('text-body1 q-mb-lg text-center')
    
    with ui.row().classes('full-width justify-center'):
        with ui.card().classes('q-ma-md'):
            ui.label('📊 Dashboard').classes('text-h6')
            ui.label('View your application statistics and overview.').classes('text-caption')
            ui.button('Open Dashboard', on_click=lambda: ui.notify('Dashboard opened!')).classes('q-mt-sm')
    
    with ui.row().classes('full-width justify-center'):
        with ui.card().classes('q-ma-md'):
            ui.label('📝 Recent Activity').classes('text-h6')
            ui.label('Check your recent activities and updates.').classes('text-caption')
            ui.button('View Activity', on_click=lambda: ui.notify('Activity log opened!')).classes('q-mt-sm')
    
    with ui.row().classes('full-width justify-center'):
        with ui.card().classes('q-ma-md'):
            ui.label('🚀 Quick Actions').classes('text-h6')
            ui.label('Access frequently used features quickly.').classes('text-caption')
            ui.button('Quick Start', on_click=lambda: ui.notify('Quick start initiated!')).classes('q-mt-sm')
    
    with ui.row().classes('full-width justify-center q-mt-lg'):
        ui.label('📈 Statistics').classes('text-h5 q-mb-md')
    
    with ui.row().classes('full-width justify-center'):
        with ui.card().classes('q-ma-sm'):
            ui.label('123').classes('text-h4 text-primary')
            ui.label('Total Items').classes('text-caption')
        
        with ui.card().classes('q-ma-sm'):
            ui.label('45').classes('text-h4 text-secondary')
            ui.label('Active Users').classes('text-caption')
        
        with ui.card().classes('q-ma-sm'):
            ui.label('89%').classes('text-h4 text-positive')
            ui.label('Success Rate').classes('text-caption') 