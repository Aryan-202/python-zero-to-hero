# External Libraries Cheat Sheet

## PIP Commands

Run these in your terminal (not in Python).

```bash
# Install a package
pip install package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show package details
pip show package_name

# Save dependencies to file
pip freeze > requirements.txt

# Install from file
pip install -r requirements.txt
```

## Virtual Environments

Isolated environments for projects.

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

## Importing

```python
import pandas            # Import whole module
import pandas as pd      # Import with alias
from math import sqrt    # Import specific function
from datetime import *   # Import everything (use carefully)
```
