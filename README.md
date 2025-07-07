# MyApp - Angular-like NiceGUI Application

A modern web application built with NiceGUI that uses HTML templates as the foundation for each page, similar to Angular's component-based architecture.

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

## 🔧 Template Engine Features

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

## 🎨 Benefits

1. **Separation of Concerns** - HTML/CSS separate from Python logic
2. **Designer-Friendly** - Designers can work with HTML files directly
3. **Maintainable** - One clear approach per page, no redundancy
4. **Scalable** - Easy to add new pages following the same pattern
5. **Flexible** - Full control over HTML structure and styling
6. **Angular-like** - Familiar component-based architecture

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