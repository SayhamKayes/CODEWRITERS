1. Select/Activate the Python Virtual Environment
VS Code is typically set up to automatically activate the environment once the correct Python interpreter is selected for the workspace.
    1. Open the Command Palette: Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (macOS).

    2. Select the Python Interpreter: Type "Python: Select Interpreter" and choose the command.

    3. Choose your virtual environment: Select the virtual environment associated with your Django project (it will often be named .venv, env, or similar, and be located in your project folder).

    4. Once selected, the name of the interpreter should appear in the status bar at the bottom right of the VS Code window.

    Open a New Terminal: Go to Terminal > New Terminal (Ctrl+Shift+``). The virtual environment should be **automatically activated**. You'll see the environment name (e.g., (.venv)`) at the start of your terminal prompt.

    Note: If the environment doesn't activate automatically, you may need to manually run the activation script in the new terminal, replacing .venv with your environment's folder name:
        1. Windows (PowerShell): .\.venv\Scripts\Activate.ps1
        2. Windows (Command Prompt): .\.venv\Scripts\activate.bat
        3. macOS/Linux (Bash/Zsh): source ./.venv/bin/activate

2. Run the Django Development Server
Once the virtual environment is active in the VS Code terminal, navigate to the directory containing your project's manage.py file (usually the root of your project) and run the standard Django command:

    1. Ensure you are in the correct directory: Use the cd command if necessary to navigate to the folder where manage.py is located.

    2. Run the server command:
        python manage.py runserver
    
    3. Access your project: The terminal will display a message indicating the server is running, usually at a link like http://127.0.0.1:8000/. You can often Ctrl+Click (Windows/Linux) or Cmd+Click (macOS) the link in the terminal to open your Django project in your web browser.
    4. Video Tutorial

    https://www.youtube.com/watch?v=wc2fKm1ZmbI
