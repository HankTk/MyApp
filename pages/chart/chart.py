import sys
import os
import matplotlib.pyplot as plt
import matplotlib
import io
import base64
from nicegui import ui

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.page_base import BasePage
from utils.page_template_loader import load_template
from utils.page_script_loader import load_script
from utils.page_data_loader import load_page_data


class ChartPage(BasePage):
    """Chart page implementation with matplotlib integration"""
    
    # Page configuration constants
    PAGE_CONFIG = {
        'page_scripts': [
            ('Chart Handler', 'pages/chart/chart_handler.js')
        ],
        'page_data': [
            ('Chart Data', 'pages/chart/chart_data.json')
        ]
    }
    
    def __init__(self):
        super().__init__('chart')
        # Set matplotlib to use non-interactive backend
        matplotlib.use('Agg')
    
    def create_matplotlib_chart(self, chart_type='line', data=None):
        """Create a matplotlib chart and return as base64 encoded image"""
        if data is None:
            data = {
                'x': [1, 2, 3, 4, 5],
                'y': [2, 4, 6, 8, 10],
                'title': 'Sample Chart',
                'xlabel': 'X Axis',
                'ylabel': 'Y Axis'
            }
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create chart based on type
        if chart_type == 'line':
            ax.plot(data['x'], data['y'], marker='o', linewidth=2, markersize=6)
        elif chart_type == 'bar':
            ax.bar(data['x'], data['y'])
        elif chart_type == 'scatter':
            ax.scatter(data['x'], data['y'], s=100, alpha=0.7)
        elif chart_type == 'pie':
            ax.pie(data['y'], labels=data.get('labels', [f'Item {i+1}' for i in range(len(data['y']))]))
        
        # Set labels and title
        ax.set_xlabel(data.get('xlabel', 'X Axis'))
        ax.set_ylabel(data.get('ylabel', 'Y Axis'))
        ax.set_title(data.get('title', 'Chart'))
        
        # Add grid for line and bar charts
        if chart_type in ['line', 'bar']:
            ax.grid(True, alpha=0.3)
        
        # Adjust layout
        plt.tight_layout()
        
        # Convert to base64
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
        plt.close()
        
        return img_base64
    
    def create_chart_section(self):
        """Create interactive chart section"""
        with ui.card().classes('q-ma-md'):
            ui.label('📊 Interactive Chart Generator').classes('text-h6 q-mb-md')
            
            # Chart type selector
            chart_type = ui.select(
                options=['line', 'bar', 'scatter', 'pie'],
                value='line',
                label='Chart Type'
            ).classes('q-mb-md')
            
            # Data input section
            with ui.row().classes('q-mb-md'):
                x_data = ui.input('X Values (comma separated)', value='1,2,3,4,5').classes('q-mr-sm')
                y_data = ui.input('Y Values (comma separated)', value='2,4,6,8,10').classes('q-mr-sm')
            
            chart_title = ui.input('Chart Title', value='Sample Chart').classes('q-mb-md')
            
            # Chart display area
            chart_container = ui.html('').classes('q-mt-md')
            
            def update_chart():
                try:
                    # Parse input data
                    x_values = []
                    y_values = []
                    
                    if x_data.value.strip():
                        x_values = [x.strip() for x in x_data.value.split(',')]
                        # Try to convert to numbers for numeric charts
                        if chart_type.value != 'bar':
                            x_values = [float(x) for x in x_values]
                    
                    if y_data.value.strip():
                        y_values = [float(y.strip()) for y in y_data.value.split(',')]
                    
                    data = {
                        'x': x_values,
                        'y': y_values,
                        'title': chart_title.value,
                        'xlabel': 'X Axis',
                        'ylabel': 'Y Axis'
                    }
                    
                    # Generate chart
                    img_base64 = self.create_matplotlib_chart(chart_type.value, data)
                    
                    # Update display
                    chart_container.content = f'''
                    <div style="text-align: center; padding: 20px;">
                        <img src="data:image/png;base64,{img_base64}" 
                             style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    </div>
                    '''
                    
                    ui.notify('Chart generated successfully!', type='positive')
                    
                except Exception as e:
                    ui.notify(f'Error creating chart: {str(e)}', type='negative')
            
            # Action buttons
            with ui.row().classes('q-mb-md'):
                ui.button('🎨 Generate Chart', on_click=update_chart).classes('q-mr-sm')
                ui.button('🔄 Reset', on_click=lambda: reset_form()).classes('q-mr-sm')
            
            def reset_form():
                chart_type.value = 'line'
                x_data.value = '1,2,3,4,5'
                y_data.value = '2,4,6,8,10'
                chart_title.value = 'Sample Chart'
                chart_container.content = ''
                ui.notify('Form reset to default values')
            
            # Quick chart buttons
            ui.label('🚀 Quick Charts:').classes('text-subtitle2 q-mb-sm')
            
            def create_quick_chart(chart_type_val, x_vals, y_vals, title):
                chart_type.value = chart_type_val
                x_data.value = x_vals
                y_data.value = y_vals
                chart_title.value = title
                update_chart()
            
            with ui.row().classes('q-mb-sm'):
                ui.button('Line', on_click=lambda: create_quick_chart('line', '1,2,3,4,5', '2,4,6,8,10', 'Line Chart')).classes('q-mr-sm q-mb-sm')
                ui.button('Bar', on_click=lambda: create_quick_chart('bar', 'A,B,C,D,E', '10,20,15,25,30', 'Bar Chart')).classes('q-mr-sm q-mb-sm')
                ui.button('Scatter', on_click=lambda: create_quick_chart('scatter', '1,2,3,4,5', '3,1,4,1,5', 'Scatter Plot')).classes('q-mr-sm q-mb-sm')
                ui.button('Pie', on_click=lambda: create_quick_chart('pie', '', '30,20,25,15,10', 'Pie Chart')).classes('q-mr-sm q-mb-sm')
                ui.button('Random', on_click=lambda: create_random_chart()).classes('q-mr-sm q-mb-sm')
            
            def create_random_chart():
                import random
                x_vals = ','.join([str(i) for i in range(1, 11)])
                y_vals = ','.join([str(random.randint(1, 50)) for _ in range(10)])
                create_quick_chart('line', x_vals, y_vals, 'Random Data Chart')


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
            # Add chart generation section after HTML template
            self.create_chart_section()
            
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


# Create instance and function for backward compatibility
chart_page = ChartPage()

def create_chart_page():
    """Create chart page using HTML template as foundation (Angular-like approach)"""
    return chart_page.create_page(
        show_script_loader=False,  # Disabled by default
        show_json_loader=False     # Disabled by default
    ) 