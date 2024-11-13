import os
import shutil
from pathlib import Path

class ComponentManager:
    def __init__(self, components_dir=None, target_dir=None):
        self.components_dir = Path(components_dir or os.path.dirname(os.path.abspath(__file__)))
        self.target_dir = Path(target_dir or os.getcwd())
        self.components = self._load_components()

    def _load_components(self):
        """Load all component files"""
        components = {}

        for item in self.components_dir.iterdir():
            if item.is_dir() and not item.name.startswith('__'):
                component_name = item.name.lower()
                components[component_name] = {
                    'html': None,
                    'js': None,
                    'css': None
                }

                # Process each file in the component directory
                for file_path in item.iterdir():
                    ext = file_path.suffix.lower()
                    if ext == '.html':
                        with open(file_path, 'r', encoding='utf-8') as f:
                            components[component_name]['html'] = f.read()
                    elif ext == '.js':
                        js_target = self.target_dir / 'scripts' / file_path.name
                        js_target.parent.mkdir(exist_ok=True)
                        shutil.copy2(file_path, js_target)
                        components[component_name]['js'] = f'<script src="scripts/{file_path.name}"></script>'
                    elif ext == '.css':
                        css_target = self.target_dir / 'styles' / file_path.name
                        css_target.parent.mkdir(exist_ok=True)
                        shutil.copy2(file_path, css_target)
                        components[component_name]['css'] = f'<link rel="stylesheet" href="styles/{file_path.name}">'

        return components

    def get_component_content(self, component_name: str) -> str:
        """Get the full content for a component"""
        component_name = component_name.lower()
        if component_name not in self.components:
            # Removed warning about missing component
            return None

        component = self.components[component_name]
        content = []

        # Add CSS and JS in the proper order (JS is typically at the bottom)
        if component['css']:
            content.append(component['css'])
        if component['html']:
            content.append(component['html'])
        if component['js']:
            content.append(component['js'])

        return '\n'.join(content) if content else None

    def print_components(self):
        """Print information about loaded components"""
        if not self.components:
            print("No components found.")
            return

        print("Found components:")
        for name, files in self.components.items():
            component_types = []
            if files['js']: component_types.append('JS')
            if files['css']: component_types.append('CSS')
            if files['html']: component_types.append('HTML')
            print(f"- {name} ({', '.join(component_types)})")