from nicegui import ui, app
from pages.home.home import create_home_page
from pages.settings.settings import create_settings_page
from pages.chart.chart import create_chart_page
from components.navigation.menu import create_menu

# Global variable to manage current page
current_page_container = None

def switch_page(page_name):
    """Switch between pages"""
    global current_page_container
    
    # Clear current page container
    if current_page_container:
        current_page_container.clear()
    
    # Create new page (executed within container)
    with current_page_container:
        if page_name == 'home':
            create_home_page()
        elif page_name == 'settings':
            create_settings_page()
        elif page_name == 'chart':
            create_chart_page()

def main():
    """Main application"""
    global current_page_container
    
    # Set app title
    ui.page_title('My Application')
    
    # Create header
    with ui.header().classes('bg-blue-600 text-white'):
        ui.label('My Application').classes('text-h5')
    
    # Create left menu
    create_menu(switch_page)
    
    # Main content area
    with ui.column().classes('full-width q-pa-md') as content_container:
        current_page_container = content_container
        # Display home page by default
        with current_page_container:
            create_home_page()
    
    # Create footer
    with ui.footer().classes('bg-grey-100'):
        ui.label('© 2024 My Application').classes('text-caption')

if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run(
        title='My Application',
        port=8080,
        reload=True,
        show=True,
        native=True,
        window_size=(1400, 900)  # Default window size (width, height)
    ) 