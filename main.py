import shutil

# Create a directory for the final project structure
project_dir = '/mnt/data/JARVIS_AI_Project'

# Files and directories to include in the ZIP file
project_files = [
    ('features/speech_engine.py', 'speech_engine.py'),
    ('features/gpt_brain.py', 'gpt_brain.py'),
    ('features/internet_tools.py', 'internet_tools.py'),
    ('features/personal_assist.py', 'personal_assist.py'),
    ('features/system_tasks.py', 'system_tasks.py'),
    ('features/home_automation.py', 'home_automation.py'),
    ('features/memory_expansion.py', 'memory_expansion.py'),
    ('data/expanded_memory.json', 'expanded_memory.json'),  # This file may not exist yet, we'll create a dummy one
    ('gui_dashboard.py', 'gui_dashboard.py'),
    ('requirements.txt', 'requirements.txt'),
    ('README.md', 'README.md')
]

# Ensure all directories are created
import os

for file in project_files:
    file_path = os.path.join(project_dir, file[0])
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Create a dummy 'expanded_memory.json' file if it doesn't exist (empty memory file for now)
memory_file_path = os.path.join(project_dir, 'data/expanded_memory.json')
with open(memory_file_path, 'w') as f:
    f.write('{}')

# Dummy content for 'requirements.txt'
requirements_content = """
pyttsx3
psutil
requests
pywhatkit
wikipedia
gpiozero  # (Optional, used for Raspberry Pi)
tkinter    # Should be pre-installed with Python
"""

# Create 'requirements.txt'
with open(os.path.join(project_dir, 'requirements.txt'), 'w') as f:
    f.write(requirements_content)

# Dummy content for 'README.md'
readme_content = """
# JARVIS AI - Personal Assistant

## Overview
JARVIS AI is a personal assistant bot built with Python, capable of performing a wide range of tasks:
- Answering questions via GPT-3
- Managing your tasks and reminders
- Providing weather and news updates
- Controlling home automation devices
- Storing and recalling memories

## Features:
- **Speech Recognition and Synthesis**
- **Task Management** (Add, Show, Delete tasks)
- **Weather and News Updates**
- **System Control** (Shutdown, Restart, Get System Info)
- **Home Automation** (Simulated control for lights and thermostat)
- **Memory** (Store and recall preferences)

## Setup Instructions

### Prerequisites:
1. Python 3.x installed on your system.
2. Install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Project:
1. **Run the GUI**: 
    ```bash
    python gui_dashboard.py
    ```
2. The **GUI window** will pop up. Use the buttons to interact with JARVIS!

### Notes:
- The **Home Automation** feature is simulated. It can control lights, thermostat, and play music.
- The **Memory** feature stores user preferences and learned data in a file called `expanded_memory.json`.

## Contributing:
Feel free to fork this project, create issues, and submit pull requests for improvements.

## License:
This project is licensed under the MIT License.
"""

# Create 'README.md'
with open(os.path.join(project_dir, 'README.md'), 'w') as f:
    f.write(readme_content)

# Now, create the ZIP file
zip_file_path = '/mnt/data/JARVIS_AI_Project.zip'
shutil.make_archive(zip_file_path.replace('.zip', ''), 'zip', project_dir)

# Provide the path to the generated ZIP file
zip_file_path
