# USB phishing
For educational purposes only. Is meant to target Windows 10/11 machines.

# Workflow
1. RubberDucky opens windows menu and executes powershell code that downloads a script
2. Script gets executed in memory and downloads an executable
3. Executable gets run

# Building
pyinstaller --onefile --noconsole logger.pyw

