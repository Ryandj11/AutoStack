import click
import os
import subprocess
from rich.console import Console
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

console = Console()

@click.group()
def cli():
    """AutoStack is a Python-based CLI tool that automates the creation and configuration of full-stack application environments."""
    pass

@cli.command()
@click.argument('project_name')
@click.option('--backend', default='fastapi', help='Backend framework (fastapi, flask, express)')
@click.option('--frontend', default='none', help='Frontend framework (react, vue, none)')
@click.option('--with-docker', is_flag=True, help='Add Docker configuration')
@click.option('--with-tests', is_flag=True, help='Add testing setup')
@click.option('--with-ci', is_flag=True, help='Add GitHub Actions CI/CD')
def init(project_name, backend, frontend, with_docker, with_tests, with_ci):
    """Initialize a new project"""
    console.print(f"🚀 Initializing project: {project_name}")

    project_path = Path(project_name)
    # Create project directory
    try:
        project_path.mkdir(exist_ok=True)
        console.print(f"✅ Created project directory: {project_path}")
    except Exception as e:
        console.print(f"🔥 [bold red]Error creating project directory: {e}[/bold red]")
        return

    create_project_files(project_path, project_name)
    create_backend(project_path, backend)

    if frontend != 'none':
        create_frontend(project_path, frontend)

    if with_docker:
        create_docker_files(project_path, frontend)

    if with_ci:
        create_ci_cd(project_path, frontend)

    if with_tests:
        create_tests(project_path, backend, frontend)

    # At this point, you can call other functions to generate the project structure
    # For example:
    # create_backend(project_name, backend)
    # if frontend != 'none':
    #     create_frontend(project_name, frontend)
    # if with_docker:
    #     create_docker_files(project_name)
    # etc.

def create_project_files(project_path: Path, project_name: str):
    """Create common project files."""
    console.print("Creating project files...")
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / 'templates'))

    # Create .gitignore
    template = env.get_template('.gitignore.j2')
    output = template.render()
    with open(project_path / ".gitignore", "w") as f:
        f.write(output)

    # Create README.md
    template = env.get_template('README.md.j2')
    output = template.render(project_name=project_name)
    with open(project_path / "README.md", "w") as f:
        f.write(output)

    console.print("✅ Created project files")

def create_backend(project_path: Path, backend: str):
    """Creates the backend structure"""
    console.print(f"🔧 Creating backend: {backend}")
    backend_path = project_path / "backend"
    try:
        backend_path.mkdir(exist_ok=True)
    except Exception as e:
        console.print(f"🔥 [bold red]Error creating backend directory: {e}[/bold red]")
        return

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / 'templates'))

    # Render and create main.py
    if backend == 'fastapi':
        template = env.get_template('fastapi_main.py.j2')
        output = template.render()
        with open(backend_path / "main.py", "w") as f:
            f.write(output)

        # Render and create requirements.txt
        template = env.get_template('fastapi_requirements.txt.j2')
        output = template.render()
        with open(backend_path / "requirements.txt", "w") as f:
            f.write(output)
    
    console.print(f"✅ Created backend files for: {backend}")

def create_frontend(project_path: Path, frontend: str):
    """Creates the frontend structure"""
    console.print(f"🔧 Creating frontend: {frontend}")
    client_path = project_path / "client"

    if frontend == 'react':
        try:
            subprocess.run(
                ["npx", "create-vite@latest", str(client_path), "--template", "react"],
                check=True,
                capture_output=True,
                text=True,
            )
            console.print(f"✅ Created frontend files for: {frontend}")
        except subprocess.CalledProcessError as e:
            console.print(f"🔥 [bold red]Error creating React frontend: {e.stderr}[/bold red]")
            return

def create_docker_files(project_path: Path, frontend: str):
    """Creates the Docker files"""
    console.print("🐳 Creating Docker files...")
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / 'templates'))

    # Create backend Dockerfile
    template = env.get_template('Dockerfile.j2')
    output = template.render()
    with open(project_path / "Dockerfile", "w") as f:
        f.write(output)

    # Create docker-compose.yml
    template = env.get_template('docker-compose.yml.j2')
    output = template.render(frontend=frontend)
    with open(project_path / "docker-compose.yml", "w") as f:
        f.write(output)

    if frontend != 'none':
        # Create frontend Dockerfile
        template = env.get_template('Dockerfile.frontend.j2')
        output = template.render()
        with open(project_path / "client" / "Dockerfile.frontend", "w") as f:
            f.write(output)

    console.print("✅ Created Docker files")

def create_ci_cd(project_path: Path, frontend: str):
    """Creates the CI/CD files"""
    console.print("🚀 Creating CI/CD files...")
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / 'templates'))
    
    # Create .github/workflows directory
    github_workflows_path = project_path / ".github" / "workflows"
    try:
        github_workflows_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        console.print(f"🔥 [bold red]Error creating .github/workflows directory: {e}[/bold red]")
        return

    # Create ci.yml
    template = env.get_template('ci.yml.j2')
    output = template.render(frontend=frontend)
    with open(github_workflows_path / "ci.yml", "w") as f:
        f.write(output)

    console.print("✅ Created CI/CD files")

def create_tests(project_path: Path, backend: str, frontend: str):
    """Creates the test files"""
    console.print("🧪 Creating tests...")
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / 'templates'))

    if backend == 'fastapi':
        # Create backend tests directory
        backend_tests_path = project_path / "backend" / "tests"
        try:
            backend_tests_path.mkdir(exist_ok=True)
        except Exception as e:
            console.print(f"🔥 [bold red]Error creating backend tests directory: {e}[/bold red]")
            return

        # Create test_main.py
        template = env.get_template('test_main.py.j2')
        output = template.render()
        with open(backend_tests_path / "test_main.py", "w") as f:
            f.write(output)

        # Add pytest to requirements.txt
        with open(project_path / "backend" / "requirements.txt", "a") as f:
            f.write("\npytest")

    if frontend == 'react':
        # Jest is already included with Vite's react-ts template.
        # For react, we can add a sample test.
        # For now, we will just print a message.
        console.print("✅ Jest is included by default with vite react template.")

    console.print("✅ Created tests")

if __name__ == '__main__':
    cli() 