 # Windows Command Cheat Sheet (Git-Friendly)

## File & Directory Navigation

### List files
- PowerShell:
  ls
- Command Prompt:
  dir

### Change directory
cd folder-name

### Go up one directory
cd ..

### Show current directory
- PowerShell:
  pwd
- Command Prompt:
  cd

### Create a directory
mkdir folder-name

### Remove a directory
- PowerShell:
  rm -r folder-name
- Command Prompt:
  rmdir /s folder-name


## File Operations

### Create an empty file
- PowerShell:
  New-Item file.md
- Command Prompt:
  type nul > file.md

### Create a file with content
echo Hello > file.txt

### View file contents
- PowerShell:
  cat file.txt
- Command Prompt:
  type file.txt

### Delete a file
- PowerShell:
  rm file.txt
- Command Prompt:
  del file.txt


## Git Commands (Same on All Platforms)

git init
git status
git add file.md
git add .
git commit -m "commit message"
git log --oneline
git branch
git switch branch-name


## Recommended Terminal for Git on Windows

- Use PowerShell or Git Bash
- Avoid Command Prompt unless required

In VS Code:
Ctrl + `
→ Select PowerShell or Git Bash

