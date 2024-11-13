import re
from pathlib import Path
from components.compmanager import ComponentManager


def compile() -> bool:
    """Compile Hydrazine project files"""
    print("Starting compilation process...")

    project_dir = Path.cwd()
    print(f"Project directory: {project_dir}")

    hydra_folder_path = project_dir / "hydra"
    print(f"Hydra folder path: {hydra_folder_path}")

    if not hydra_folder_path.exists():
        print("Error: 'hydra' folder not found.")
        return False

    comp_manager = ComponentManager()
    comp_manager.print_components()

    hdz_files = list(hydra_folder_path.glob("*.hdz"))
    if not hdz_files:
        print("No .hdz files found.")
        return True

    print(f"Found {len(hdz_files)} .hdz file(s):")
    for hdz_file in hdz_files:
        print(f"Processing: {hdz_file.name}")

        try:
            content = hdz_file.read_text(encoding='utf-8')

            # Find all hydrazine component tags (case-insensitive)
            components = re.finditer(r'<([hH][A-Za-z]+)([^>]*?)(/?>|>(.*?)</\1>)', content, re.DOTALL)

            # Process each component
            for match in components:
                full_tag = match.group(0)
                component_name = match.group(1).lower()  # Ensure component name is lowercase for matching
                print(f"Found component: {component_name}")

                replacement = comp_manager.get_component_content(component_name)
                if replacement:
                    print(f"Replacing {full_tag} with component content.")
                    content = content.replace(full_tag, replacement)

            # Write compiled HTML
            output_file = project_dir / hdz_file.name.replace('.hdz', '.html')
            output_file.write_text(content, encoding='utf-8')
            print(f"Created: {output_file.name}")

        except Exception as e:
            print(f"Error processing {hdz_file.name}: {str(e)}")
            return False

    print("Compilation process completed successfully.")
    return True