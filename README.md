# 🚀 AutoStack

A CLI tool to automate the setup and deployment of full-stack applications with one command.

## 🧠 Description

AutoStack is a Python-based command-line tool that streamlines the setup of new projects by automating the creation of backend, frontend, Docker, CI/CD, and testing scaffolds. Developers can spin up production-ready environments with a single command, saving time, avoiding repetitive boilerplate, and standardizing best practices.

## 🔧 Installation

To install AutoStack, clone the repository and install it using pip:

```bash
# Clone the repository
git clone https://github.com/your-username/autostack-cli
cd autostack-cli

# Install the package in editable mode for development
pip install -e .
```

## 🚀 Quick Start

Once installed, you can use the `autostack` command to generate a new project:

```bash
# Create a full-stack app with FastAPI backend and React frontend
autostack init myapp --backend fastapi --frontend react --with-docker --with-tests --with-ci

# Navigate to your new project
cd myapp

# Start with Docker
docker-compose up --build
```

## 📦 Available Commands

| Command                         | Description                           |
| ------------------------------- | ------------------------------------- |
| `autostack init <project_name>` | Initialize a new project              |
| `--backend <framework>`         | Add backend (fastapi, express, flask) |
| `--frontend <framework>`        | Add frontend (react, vue, none)       |
| `--with-docker`                 | Add Docker configuration              |
| `--with-tests`                  | Add testing setup                     |
| `--with-ci`                     | Add GitHub Actions CI/CD              |

## 🗂️ Generated Project Structure

```
myapp/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── tests/
│       └── test_main.py
├── client/ (optional, if React selected)
│   └── Vite + React setup
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
└── README.md
```

## 🛠️ Supported Technologies

- **Backend**: FastAPI
- **Frontend**: React + Vite
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions
- **Testing**: pytest, Jest

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License
