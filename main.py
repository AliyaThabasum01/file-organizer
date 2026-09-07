# 📂 File Organizer

A lightweight Python CLI tool that automatically organizes files into folders based on their file extensions.

## Features

- Organize files automatically
- Create folders by extension
- Move files safely
- Handle files without extensions
- No external dependencies

## Run

```bash
python main.py
```

## Example

Before:

```text
Downloads/
├── photo.jpg
├── notes.txt
├── project.py
└── resume.pdf
```

After:

```text
Downloads/
├── JPG/
│   └── photo.jpg
├── TXT/
│   └── notes.txt
├── PY/
│   └── project.py
└── PDF/
    └── resume.pdf
```

## Built With

- Python
- os
- shutil
