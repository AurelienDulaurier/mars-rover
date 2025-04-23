import os
import xml.etree.ElementTree as ET

def get_dependencies(project_path):
    dependencies = []
    try:
        tree = ET.parse(os.path.join(project_path, f"{os.path.basename(project_path)}.csproj"))
        root = tree.getroot()
        for reference in root.findall('.//Reference'):
            dependencies.append(reference.attrib['Include'])
    except Exception as e:
        print(f"Erreur lors de la lecture de {project_path}: {e}")
    return dependencies

def detect_circular_dependencies(project, visited, stack, dependencies):
    if project in stack:
        print(f"Dépendance circulaire détectée : {' -> '.join(stack + [project])}")
        return True
    if project in visited:
        return False

    visited.add(project)
    stack.append(project)

    for dep in dependencies.get(project, []):
        if detect_circular_dependencies(dep, visited, stack, dependencies):
            return True

    stack.pop()
    return False

def main(solution_path):
    dependencies = {}
    projects = [d for d in os.listdir(solution_path) if os.path.isdir(os.path.join(solution_path, d))]

    for project in projects:
        project_path = os.path.join(solution_path, project)
        dependencies[project] = get_dependencies(project_path)

    visited = set()
    has_cycle = False

    for project in dependencies.keys():
        if detect_circular_dependencies(project, visited, [], dependencies):
            has_cycle = True

    if not has_cycle:
        print("Aucune dépendance circulaire détectée.")
        return 0
    return 1

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python check_circular_dependencies.py <path_to_solution>")
        sys.exit(1)

    solution_path = sys.argv[1]
    exit_code = main(solution_path)
    sys.exit(exit_code)