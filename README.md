# MyApp - NiceGUI Application with HTML Templates

A modern web application built with NiceGUI that uses HTML templates as the foundation for each page, similar to Angular's component-based architecture. This project demonstrates how to define page layouts in HTML files and load them dynamically in NiceGUI applications.

## 🏗️ Architecture

This application follows an **Angular-like component architecture** where:

- **HTML templates** serve as the foundation for each page
- **Python components** handle data and logic (like Angular TypeScript components)
- **Template engine** processes dynamic content with variables and loops
- **Single responsibility** - each page has one clear implementation
- **Data-driven** - page content is loaded from JSON files

## 📁 Project Structure

```
MyApp/
├── main.py                          # Main application entry point
├── pages/                           # Page components (Angular-like)
│   ├── home/                        # Home page component
│   │   ├── home.py                  # Home page logic & data
│   │   ├── home_data.json           # Home page data
│   │   ├── home_template.html       # Home page template
│   │   └── home_handler.js          # Home page JavaScript
│   │
│   └── settings/                    # Settings page component
│       ├── settings.py              # Settings page logic & data
│       ├── settings_data.json       # Settings page data
│       ├── settings_template.html   # Settings page template
│       └── settings_handler.js      # Settings page JavaScript
│
├── utils/                          # Utilities
│   ├── page_template_engine.py     # Template processing engine
│   ├── page_template_loader.py     # Template loading utilities
│   ├── page_script_loader.py       # JavaScript loading utilities
│   └── page_data_loader.py         # Page data loading utilities
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🚀 How It Works

### 1. **Component-Based Pages** (Like Angular)
Each page is a **component** with:
- **Template**: HTML file with dynamic variables (`{{variable}}`)
- **Logic**: Python file with data loading and event handlers
- **Data**: JSON file with page-specific data
- **Scripts**: JavaScript files for client-side functionality

### 2. **Template Engine**
- **Variable substitution**: `{{variable}}` and `{{object.property}}`
- **Conditional rendering**: `{% if condition %} ... {% endif %}`
- **Loop rendering**: `{% for item in items %} ... {% endfor %}`

### 3. **Data Loading**
- **JSON-based**: Page data stored in separate JSON files
- **Caching**: Automatic caching for performance
- **Fallback**: Graceful handling of missing data files

### 4. **Event Handling**
- **JavaScript events** in HTML templates
- **Python event handlers** via `postMessage`
- **NiceGUI integration** for notifications and state

## 🎯 Key Features

- ✅ **Clean Architecture** - No redundant implementations
- ✅ **HTML Templates** - Designers can work with HTML directly
- ✅ **Dynamic Content** - Data-driven pages with loops and conditionals
- ✅ **Event Handling** - JavaScript ↔ Python communication
- ✅ **Responsive Design** - CSS Grid and Flexbox layouts
- ✅ **Error Handling** - Fallback to NiceGUI components if templates fail
- ✅ **Template Variable Substitution** - Use string formatting with variables
- ✅ **Advanced Templating** - Conditionals and loops
- ✅ **JavaScript Integration** - Full web capabilities
- ✅ **CSS Styling** - Complete design control
- ✅ **Data Separation** - JSON files for page data
- ✅ **Script Loading** - Dynamic JavaScript injection
- ✅ **Navigation** - Clean page switching with sidebar menu

## 🛠️ Usage

### Running the Application
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

The application will start on `http://localhost:8080` with a native window.

### Creating a New Page
1. **Create page directory**:
   ```
   pages/new_page/
   ├── new_page.py
   ├── new_page_data.json
   ├── new_page_template.html
   └── new_page_handler.js
   ```

2. **Create page logic**:
   ```python
   # pages/new_page/new_page.py
   from nicegui import ui
   import sys
   import os
   
   sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
   from utils.page_template_loader import load_template
   from utils.page_script_loader import load_script
   from utils.page_data_loader import load_page_data
   
   def create_new_page():
       # Load page data from JSON file
       page_data = load_page_data('new_page')
       
       # Load and render the page using HTML template
       template_path = os.path.join(os.path.dirname(__file__), 'new_page_template.html')
       html_container = load_template(template_path, page_data)
       
       if html_container:
           # Load event handler script
           load_script('pages/new_page/new_page_handler.js')
           return html_container
       else:
           ui.label('New page could not be loaded.').classes('text-h6 q-mb-md text-center text-red')
   ```

3. **Create page data**:
   ```json
   // pages/new_page/new_page_data.json
   {
     "title": "New Page",
     "header_title": "Welcome to New Page",
     "header_subtitle": "This is a new page component",
     "content": "Dynamic content here"
   }
   ```

4. **Create page template**:
   ```html
   <!-- pages/new_page/new_page_template.html -->
   <div>
       <h1>{{header_title}}</h1>
       <p>{{header_subtitle}}</p>
       <div>{{content}}</div>
   </div>
   ```

5. **Add to main app**:
   ```python
   # main.py
   from pages.new_page.new_page import create_new_page
   
   def switch_page(page_name):
       if page_name == 'new_page':
           create_new_page()
   ```

## 📚 HTML Template Techniques

### 1. **Variable Substitution**
```html
<h1>{{title}}</h1>
<p>Welcome to {{app_name}}</p>
<div>{{user.name}} - {{user.email}}</div>
```

### 2. **Conditional Rendering**
```html
{% if show_header %}
<div class="header">
    <h1>{{header_title}}</h1>
</div>
{% endif %}
```

### 3. **Loop Rendering**
```html
{% for feature in features %}
<div class="feature">
    <h3>{{feature.title}}</h3>
    <p>{{feature.description}}</p>
    <button onclick="window.parent.postMessage({type: '{{feature.action}}'}, '*')">
        {{feature.button_text}}
    </button>
</div>
{% endfor %}
```

### 4. **JavaScript Integration**
```html
<button onclick="window.parent.postMessage({type: 'action'}, '*')">
    Click Me
</button>
```

## 🔧 Utility Functions

### Template Loading
```python
from utils.page_template_loader import load_template

# Load and render HTML template
html_container = load_template('path/to/template.html', variables)
```

### Data Loading
```python
from utils.page_data_loader import load_page_data

# Load page data from JSON
page_data = load_page_data('page_name')
```

### Script Loading
```python
from utils.page_script_loader import load_script

# Load JavaScript file
load_script('path/to/script.js')
```

## 🌐 JavaScript Integration

HTML templates can include JavaScript that communicates with NiceGUI:

```html
<button onclick="window.parent.postMessage({type: 'action'}, '*')">
    Click Me
</button>
```

```python
# Handle JavaScript messages
ui.add_head_html("""
<script>
window.addEventListener('message', function(event) {
    if (event.data.type === 'action') {
        // Handle the action
        window.parent.postMessage({
            type: 'ui_notify',
            message: 'Action performed!'
        }, '*');
    }
});
</script>
""")
```

## 🎨 Benefits

1. **Separation of Concerns** - HTML/CSS separate from Python logic
2. **Designer-Friendly** - Designers can work with HTML files directly
3. **Maintainable** - One clear approach per page, no redundancy
4. **Scalable** - Easy to add new pages following the same pattern
5. **Flexible** - Full control over HTML structure and styling
6. **Angular-like** - Familiar component-based architecture
7. **Reusability** - Templates can be reused across different pages
8. **Performance** - Pre-rendered HTML can be faster than dynamic components
9. **Data-Driven** - Content managed through JSON files
10. **Modular** - Each component is self-contained

## 🛡️ Best Practices

### 1. Error Handling
Always include fallbacks when loading templates:

```python
try:
    html = load_template('template.html', variables)
    if html:
        return html
except Exception as e:
    # Fallback to NiceGUI components
    ui.label('Template not found')
    ui.button('Go back')
```

### 2. Security
When using user-provided data in templates:

```python
# Sanitize user input
import html
user_content = html.escape(user_input)
variables['content'] = user_content
```

### 3. Performance
For large templates, consider caching:

```python
# Template caching is built into page_template_loader
# Templates are automatically cached after first load
```

### 4. Responsive Design
Use CSS Grid and Flexbox in your templates:

```html
<style>
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
}
</style>
```

## ⚠️ Limitations

1. **JavaScript Integration** - Requires careful handling of events
2. **State Management** - HTML templates don't automatically sync with NiceGUI state
3. **Component Integration** - Mixing HTML and NiceGUI components requires planning
4. **Debugging** - HTML errors can be harder to debug than Python code

## 🔄 Current Architecture

The current structure follows a clean, Angular-like approach:

- ✅ **Single Implementation** - Each page has one clear approach
- ✅ **Component-Based** - Each page is a self-contained component
- ✅ **Data Separation** - JSON files for page data
- ✅ **Template Engine** - Advanced templating with variables, conditionals, and loops
- ✅ **Script Loading** - Dynamic JavaScript injection
- ✅ **Error Handling** - Graceful fallbacks for missing files

## 🎯 Conclusion

This application demonstrates a production-ready implementation of HTML templates in NiceGUI that combines the best of both worlds:

- **Python backend logic** for data processing and business logic
- **HTML templates** for rich, responsive user interfaces
- **Component-based architecture** for maintainable, scalable code
- **Data-driven approach** for flexible content management

The architecture is particularly useful for:
- Applications with complex layouts
- Projects requiring designer collaboration
- Legacy HTML/CSS integration
- Performance-critical applications
- Angular-like component-based architecture

Choose this approach when you need the flexibility of HTML templates combined with the power of Python backend logic. 