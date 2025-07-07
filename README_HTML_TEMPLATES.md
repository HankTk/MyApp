# HTML Templates in NiceGUI

This project demonstrates how to define page layouts in HTML files and load them dynamically in NiceGUI applications.

## Overview

NiceGUI provides the `ui.html()` function that allows you to inject HTML content directly into your application. This opens up several possibilities for using HTML templates:

1. **Direct HTML File Loading** - Load complete HTML files
2. **Template Variables** - Use string formatting with variables
3. **Template Engine** - Advanced templating with conditionals and loops
4. **Hybrid Approach** - Combine HTML templates with NiceGUI components

## Features Demonstrated

- ✅ Load HTML files from disk
- ✅ Template variable substitution
- ✅ Conditional rendering
- ✅ Loop rendering
- ✅ JavaScript integration
- ✅ CSS styling in templates
- ✅ Error handling and fallbacks

## File Structure

```
MyApp/
├── main_html_templates.py          # Demo application
├── templates/                      # HTML template files
│   ├── home_template.html         # Complete HTML page
│   └── base_layout.html           # Base layout template
├── utils/                         # Template engine utilities
│   ├── __init__.py
│   └── template_engine.py         # Template engine class
├── pages/                         # Page modules
│   ├── home_html.py               # HTML file loading
│   └── home_template_engine.py    # Template engine usage
└── README_HTML_TEMPLATES.md       # This file
```

## Usage Examples

### 1. Direct HTML File Loading

```python
from nicegui import ui

def create_page_from_html():
    # Load HTML from file
    with open('templates/page.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Inject the HTML
    ui.html(html_content)
```

### 2. Template Variables

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

### 3. Template Engine

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

## Template Engine Features

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
{% for item in items %}
<div class="item">
    <h3>{{item.title}}</h3>
    <p>{{item.description}}</p>
</div>
{% endfor %}
```

## JavaScript Integration

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

## Running the Demo

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the HTML templates demo:**
   ```bash
   python main_html_templates.py
   ```

3. **Open your browser** to `http://localhost:8080`

4. **Navigate through the menu** to see different template approaches:
   - Home (HTML File) - Loads complete HTML file
   - Home (Template Vars) - Uses string formatting
   - Home (Template Engine) - Uses advanced template engine
   - Dynamic Content - Shows dynamic data rendering

## Best Practices

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

## Advantages of HTML Templates

1. **Separation of Concerns** - HTML/CSS separate from Python logic
2. **Designer-Friendly** - Designers can work with HTML files directly
3. **Reusability** - Templates can be reused across different pages
4. **Flexibility** - Full control over HTML structure and styling
5. **Performance** - Pre-rendered HTML can be faster than dynamic components

## Limitations

1. **JavaScript Integration** - Requires careful handling of events
2. **State Management** - HTML templates don't automatically sync with NiceGUI state
3. **Component Integration** - Mixing HTML and NiceGUI components requires planning
4. **Debugging** - HTML errors can be harder to debug than Python code

## Conclusion

HTML templates in NiceGUI provide a powerful way to create rich, dynamic web applications while maintaining the benefits of Python backend logic. The approach is particularly useful for:

- Applications with complex layouts
- Projects requiring designer collaboration
- Legacy HTML/CSS integration
- Performance-critical applications

Choose the approach that best fits your project's needs and complexity requirements. 