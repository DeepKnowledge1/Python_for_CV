## 📁 Section 1: Introduction Series (Videos 1–7)

Welcome to the beginning of your computer vision journey! This section lays the foundation for everything you'll build throughout the course. You'll understand what computer vision is, why it's a valuable skill, and how Python serves as a powerful tool for solving real-world CV problems. We'll also get you set up with the right tools, development environment, and mindset.

### 🎯 Learning Objectives:
- Understand the course goals and structure
- Learn why Python is widely used for computer vision
- Set up your environment with Poetry and pre-commit
- Run your first image-processing script
- Get a high-level roadmap of the course

| Video | Title                                                                   |
| ----- | ----------------------------------------------------------------------- |
| 1     | 🎬 [CTR Hook] "Struggling with Image Datasets? Here's How to Fix That" |
| 2     | 📦 What is Computer Vision & Why Python? + Real-World Use Cases         |
| 3     | 🛠️ Installing Python & Tools You Need – With Common Pitfalls & Fixes   |
| 4     | 🎵 Modern Dependency Management with Poetry                             |
| 5     | 🔍 Code Quality with Pre-commit Hooks                                   |
| 6     | 🧪 Running Your First Image Script – "Hello World" for CV               |
| 7     | 🧭 Course Roadmap – How to Get the Most Out of This Playlist            |

👉 By the end of this section, you'll have a clean Python development environment, a clear understanding of CV's relevance, and your first working image script!



# Installing Python & Tools You Need – With Common Pitfalls & Fixes

#### 📥 Install `pyenv-win`


```powershell
git clone https://github.com/pyenv-win/pyenv-win.git $HOME\.pyenv
setx PYENV $HOME\.pyenv
setx PATH "$env:PYENV\bin;$env:PYENV\shims;$env:PATH"
```


### 🔁 Most Important `pyenv` Commands

```bash
pyenv install <version>      # install a new version
pyenv uninstall <version>    # remove a version
pyenv versions               # list installed versions
pyenv global <version>       # set default
pyenv local <version>        # set per-project
pyenv shell <version>        # set for current shell only
pyenv rehash                 # rebuild shims after installing pip packages
```



# Modern Dependency Management with Poetry
---

### 📘 **Essential Poetry Commands Cheat Sheet**

| 🛠️ **Category**     | 🧾 **Command**                                                | 🧩 **Description**                         | 💡 **Example**                                                |
| -------------------- | ------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------- |
| 🔧 Project Setup     | `poetry new my_project`                                       | Create new project scaffold                | `poetry new image_toolkit`                                    |
|                      | `poetry init`                                                 | Interactive setup in existing folder       | `poetry init`                                                 |
| 📦 Dependency Mgmt   | `poetry add package`                                          | Add a regular dependency                   | `poetry add numpy`                                            |
|                      | `poetry add --group dev package`                              | Add a dev-only dependency                  | `poetry add --group dev black`                                |
|                      | `poetry remove package`                                       | Remove a package                           | `poetry remove pillow`                                        |
|                      | `poetry update`                                               | Update all dependencies                    | `poetry update`                                               |
| 📁 Environment       | `poetry install`                                              | Install dependencies from lockfile         | `poetry install`                                              |
|                      | `poetry shell`                                                | Activate Poetry's virtual environment      | `poetry shell`                                                |
|                      | `poetry run`                                                  | Run a command inside Poetry env            | `poetry run python main.py`                                   |
|                      | `poetry env list`                                             | List virtual environments                  | `poetry env list`                                             |
|                      | `poetry env remove`                                           | Delete virtual environment                 | `poetry env remove python3.11`                                |
| 🔍 Inspection        | `poetry show`                                                 | Show installed packages                    | `poetry show`                                                 |
|                      | `poetry show --tree`                                          | Show dependency tree                       | `poetry show --tree`                                          |
|                      | `poetry check`                                                | Validate project config                    | `poetry check`                                                |
| 🚚 Export (Plugin)   | `poetry export -f requirements.txt --output requirements.txt` | Export to pip format (**requires plugin**) | `poetry export -f requirements.txt --output requirements.txt` |
| ⚙️ Plugin Management | `poetry self add plugin`                                      | Add official plugin                        | `poetry self add poetry-plugin-export`                        |

---
