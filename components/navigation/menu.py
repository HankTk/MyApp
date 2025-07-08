from nicegui import ui

def create_menu(switch_page_callback):
    """Create the left sidebar menu
    
    Args:
        switch_page_callback: Function to call when switching pages
    """
    with ui.left_drawer().classes('bg-blue-50'):
        ui.label('Menu').classes('text-h6 q-pa-md')
        ui.separator()
        
        # Home button
        home_btn = ui.button('🏠 Home', on_click=lambda: switch_page_callback('home')).classes('full-width q-ma-sm')
        
        # Settings button
        settings_btn = ui.button('⚙️ Settings', on_click=lambda: switch_page_callback('settings')).classes('full-width q-ma-sm') 