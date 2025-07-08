import os
import re
from string import Template
from typing import Dict, Any

class PageTemplateEngine:
    """シンプルなHTMLテンプレートエンジン"""
    
    def __init__(self, templates_dir: str = "templates"):
        self.templates_dir = templates_dir
    
    def load_template(self, template_name: str) -> str:
        """テンプレートファイルを読み込み"""
        template_path = os.path.join(self.templates_dir, template_name)
        
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Template file not found: {template_path}")
    
    def render_template(self, template_name: str, variables: Dict[str, Any]) -> str:
        """テンプレートを変数でレンダリング"""
        template_content = self.load_template(template_name)
        return self.render_string(template_content, variables)
    
    def render_string(self, template_string: str, variables: Dict[str, Any]) -> str:
        """テンプレート文字列を変数でレンダリング"""
        # Jinja2風の構文をサポート
        rendered = template_string
        
        # {% for item in items %} ... {% endfor %} 形式のループを先に処理
        rendered = self._process_loops(rendered, variables)
        
        # {% if condition %} ... {% endif %} 形式の条件分岐
        rendered = self._process_conditionals(rendered, variables)
        
        # {{variable}} 形式の置換（ループ処理後に実行）
        rendered = self._process_variables(rendered, variables)
        
        return rendered
    
    def _process_variables(self, content: str, variables: Dict[str, Any]) -> str:
        """変数を処理（ネストしたオブジェクトプロパティも対応）"""
        # {{variable}} または {{object.property}} 形式の置換
        pattern = r'\{\{([^}]+)\}\}'
        
        def replace_variable(match):
            var_path = match.group(1).strip()
            return self._get_nested_value(variables, var_path)
        
        return re.sub(pattern, replace_variable, content)
    
    def _get_nested_value(self, variables: Dict[str, Any], var_path: str) -> str:
        """ネストしたオブジェクトから値を取得"""
        parts = var_path.split('.')
        current = variables
        
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            elif isinstance(current, (list, tuple)) and part.isdigit():
                index = int(part)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    return f"{{{{{var_path}}}}}"
            else:
                return f"{{{{{var_path}}}}}"
        
        return str(current) if current is not None else ""
    
    def _process_conditionals(self, content: str, variables: Dict[str, Any]) -> str:
        """条件分岐を処理"""
        # シンプルな実装: {% if variable %} ... {% endif %}
        pattern = r'{%\s*if\s+(\w+)\s*%}(.*?){%\s*endif\s*%}'
        
        def replace_conditional(match):
            condition_var = match.group(1)
            conditional_content = match.group(2)
            
            if condition_var in variables and variables[condition_var]:
                return conditional_content
            return ''
        
        return re.sub(pattern, replace_conditional, content, flags=re.DOTALL)
    
    def _process_loops(self, content: str, variables: Dict[str, Any]) -> str:
        """ループを処理"""
        # シンプルな実装: {% for item in items %} ... {% endfor %}
        pattern = r'{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%}(.*?){%\s*endfor\s*%}'
        
        def replace_loop(match):
            item_var = match.group(1)
            items_var = match.group(2)
            loop_content = match.group(3)
            
            if items_var in variables:
                items = variables[items_var]
                if isinstance(items, (list, tuple)):
                    result = []
                    for item in items:
                        # ループ内の変数を置換
                        item_variables = variables.copy()
                        item_variables[item_var] = item
                        
                        # ループ内のコンテンツを再帰的に処理
                        item_content = self.render_string(loop_content, item_variables)
                        result.append(item_content)
                    return ''.join(result)
            
            return ''
        
        return re.sub(pattern, replace_loop, content, flags=re.DOTALL)

# 便利な関数
def render_template(template_name: str, variables: Dict[str, Any], templates_dir: str = "templates") -> str:
    """テンプレートを簡単にレンダリングする関数"""
    engine = PageTemplateEngine(templates_dir)
    return engine.render_template(template_name, variables)

def render_string(template_string: str, variables: Dict[str, Any]) -> str:
    """テンプレート文字列を簡単にレンダリングする関数"""
    engine = PageTemplateEngine()
    return engine.render_string(template_string, variables) 