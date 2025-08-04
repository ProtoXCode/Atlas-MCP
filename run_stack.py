#!/usr/bin/python3
import subprocess
import sys
import time
import os
import webbrowser
import shutil


def run_cmd(command, cwd=None) -> None:
    if sys.platform == 'win32':
        # Windows
        subprocess.Popen(['start', 'cmd', '/k'] + command, shell=True, cwd=cwd)
    elif sys.platform == 'darwin':
        # MacOS
        script = f'tell application "Terminal" to do script "cd {cwd or os.getcwd()} && {" ".join(command)}"'
        subprocess.Popen(['osascript', '-e', script])
    else:
        # Linux
        subprocess.Popen(['gnome-terminal', '--', *command], cwd=cwd)


def check_ollama_installed() -> bool:
    return shutil.which('ollama') is not None


# Check for Ollama
if not check_ollama_installed():
    print("[-] Ollama is not installed or not found in PATH")
    print("    Please install it from https://ollama.com/ or make sure it's "
          "    added to the PATH environment variable")
    sys.exit(1)

# Start Ollama llama3
print('[+] Starting Ollama with llama3...')
run_cmd(['ollama', 'run', 'llama3'])

# Start FastAPI backend
print('[+] Starting FastAPI backend...')
run_cmd(['uvicorn', 'server.main:app', '--reload'])

# Wait, then open browser
print('[~] Waiting before launching browser...')
time.sleep(5)
print('[+] Opening browser...')
webbrowser.open('http://localhost:8000/network_info')
