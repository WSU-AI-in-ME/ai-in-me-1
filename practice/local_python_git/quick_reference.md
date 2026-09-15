# Windows Command Reference

**ME 5995 · Optional, ungraded self-study**

Use PowerShell. Run commands one at a time and wait for the prompt to return.
These examples use the installed Python 3.13 with user-level packages.

## Find and open a project

| Command | Purpose |
|---|---|
| `pwd` | Show the current folder. |
| `dir` | List files and folders. |
| `cd $env:USERPROFILE` | Go to your Windows user folder. |
| `cd me5995-sensor-example` | Enter that project folder. |
| `code .` | Open the current folder in VS Code. |

A path containing spaces should be enclosed in quotes, for example
`cd "C:\My Projects\example"`. In a path, `.` means the current folder.

## Install and run

| Command | Purpose |
|---|---|
| `py -3.13 --version` | Check Python 3.13. |
| `py -3.13 -c "import sys; print(sys.executable)"` | Show its executable path; select this same Python in VS Code. |
| `py -3.13 -m pip install --user -r requirements.txt` | Install the listed requirements and their dependencies for your account. |
| `py -3.13 analyze_sensor.py` | Run the Practice B program. |

Run the installation command from the folder containing requirements.txt.
Cloning does not install packages. `Requirement already satisfied` means a
compatible installed package was found. Close the graph window when finished
so the terminal prompt returns. Practice B saves its graph automatically.

## Git commands used in Practice A

| Command | Purpose |
|---|---|
| `git status` | Show local changes and branch status. |
| `git diff -- vibration.py` | View unstaged text changes; press Q if a viewer opens. |
| `git add .` | Stage changes in the current folder and its subfolders, including additions, modifications, and deletions. Untracked files covered by .gitignore are excluded. |
| `git diff --cached --stat` | Summarize the staged changes before committing. |
| `git commit -m "Describe the change"` | Record staged content in local history. |
| `git push` | Send commits to your own configured GitHub repository. |

Run `git add .` from the project root to cover the whole project. To select
specific files or folders instead, use `git add README.md images/`.
Saving, staging, committing, and pushing are separate actions.

Practice B only downloads and runs the provided project. It does not require
editing, committing, or pushing to the course repository.

## Navigation

- [Windows setup](windows_setup.md)
- [Practice A](practice_a.md)
- [Practice B](practice_b.md)
- [Before leaving a shared computer](before_leaving.md)
- [Optional virtual environments](optional_venv.md)

## References

- [Git add documentation](https://git-scm.com/docs/git-add)
- [pip user installations](https://pip.pypa.io/en/stable/user_guide/#user-installs)
