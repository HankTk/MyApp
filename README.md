# MyApp - NiceGUI Application with HTML Templates

A modern web application built with NiceGUI that uses HTML templates as the foundation for each page, similar to Angular's component-based architecture. This project demonstrates how to define page layouts in HTML files and load them dynamically in NiceGUI applications.

## 🏗️ Architecture

This application follows an **Angular-like component architecture** where:

- **HTML templates** serve as the foundation for each page
- **Python components** handle data and logic (like Angular TypeScript components)
- **Template engine** processes dynamic content with variables and loops
- **Single responsibility** - each page has one clear implementation

## 📁 Project Structure

```
MyApp/
├── main.py                          # Main application entry point
├── pages/                           # Page components (Angular-like)
│   ├── home/                        # Home page component
│   │   ├── home.py                  # Home page logic & data
│   │   └── home_template.html       # Home page template
│   └── settings/                    # Settings page component
│       ├── settings.py              # Settings page logic & data
│       └── settings_template.html   # Settings page template
├── templates/                       # Shared templates
│   └── base_layout.html            # Base layout template
├── utils/                          # Utilities
│   └── template_engine.py          # Template processing engine
└── requirements.txt                # Python dependencies
```

## 🚀 How It Works

### 1. **Component-Based Pages** (Like Angular)
Each page is a **component** with:
- **Template**: HTML file with dynamic variables
- **Logic**: Python file with data and event handlers
- **Data Binding**: Template variables connect Python data to HTML

### 2. **Template Engine**
- **Variable substitution**: `{{variable}}`
- **Conditional rendering**: `{% if condition %} ... {% endif %}`
- **Loop rendering**: `{% for item in items %} ... {% endfor %}`

### 3. **Event Handling**
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

## 🛠️ Usage

### Running the Application
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Creating a New Page
1. **Create page component**:
   ```python
   # pages/new_page/new_page.py
   def create_new_page():
       page_data = {
           'title': 'New Page',
           'content': 'Dynamic content here'
       }
       rendered_html = render_template('new_page_template.html', page_data)
       return ui.html(rendered_html)
   ```

2. **Create page template**:
   ```html
   <!-- pages/new_page/new_page_template.html -->
   <div>
       <h1>{{title}}</h1>
       <p>{{content}}</p>
   </div>
   ```

3. **Add to main app**:
   ```python
   # main.py
   from pages.new_page.new_page import create_new_page
   
   def switch_page(page_name):
       if page_name == 'new_page':
           create_new_page()
   ```

## 📚 HTML Template Techniques

NiceGUI provides the `ui.html()` function that allows you to inject HTML content directly into your application. This opens up several possibilities for using HTML templates:

### 1. **Direct HTML File Loading**

```python
from nicegui import ui

def create_page_from_html():
    # Load HTML from file
    with open('templates/page.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Inject the HTML
    ui.html(html_content)
```

### 2. **Template Variables**

```python
def create_page_with_variables():
    # Template with variables
    template = """
    <div>
        <h1>Welcome to {app_name}</h1>
        <p>Hello, {user_name}!</p>
    </div>
    """
    
    # Replace variables
    rendered = template.format(
        app_name="MyApp",
        user_name="John Doe"
    )
    
    ui.html(rendered)
```

### 3. **Template Engine**

```python
from utils.template_engine import render_template

def create_page_with_engine():
    # Template variables
    variables = {
        'title': 'My Page',
        'content': '<p>Dynamic content</p>',
        'show_header': True
    }
    
    # Render template
    html = render_template('base_layout.html', variables)
    ui.html(html)
```

## 🔧 Template Engine Features

The custom template engine supports:

### Variable Substitution
```html
<h1>{{title}}</h1>
<p>Welcome to {{app_name}}</p>
```

### Conditional Rendering
```html
{% if show_header %}
<div class="header">
    <h1>{{header_title}}</h1>
</div>
{% endif %}
```

### Loop Rendering
```html
{% for feature in features %}
<div class="feature">
    <h3>{{feature.title}}</h3>
    <p>{{feature.description}}</p>
</div>
{% endfor %}
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

## 🛡️ Best Practices

### 1. Error Handling
Always include fallbacks when loading templates:

```python
try:
    html = render_template('template.html', variables)
    ui.html(html)
except FileNotFoundError:
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
# Cache rendered templates
template_cache = {}

def get_cached_template(template_name, variables):
    cache_key = f"{template_name}_{hash(str(variables))}"
    if cache_key not in template_cache:
        template_cache[cache_key] = render_template(template_name, variables)
    return template_cache[cache_key]
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

## 🔄 Migration from Old Structure

The old structure had multiple redundant approaches:
- ❌ `home.py` (pure NiceGUI)
- ❌ `home_html.py` (HTML file loading)
- ❌ `home_template_engine.py` (template engine)
- ❌ `main_html_templates.py` (demo app)

**New structure** has one clean approach:
- ✅ `home.py` (component logic)
- ✅ `home_template.html` (component template)
- ✅ `main.py` (unified application)

This eliminates redundancy and provides a clear, maintainable architecture similar to Angular!

## 🎯 Conclusion

HTML templates in NiceGUI provide a powerful way to create rich, dynamic web applications while maintaining the benefits of Python backend logic. The approach is particularly useful for:

- Applications with complex layouts
- Projects requiring designer collaboration
- Legacy HTML/CSS integration
- Performance-critical applications
- Angular-like component-based architecture

Choose the approach that best fits your project's needs and complexity requirements. This application demonstrates a clean, production-ready implementation that combines the best of both worlds. 