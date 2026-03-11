import subprocess
import sys

class SecureExecutor:
    def __init__(self):
        self.allowed_commands = ['ls', 'echo', 'pwd']  # Specify allowed commands

    def execute(self, command):
        if command not in self.allowed_commands:
            raise ValueError('Command not allowed!')
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {str(e)}\n{e.output}'

if __name__ == '__main__':
    executor = SecureExecutor()
    command = sys.argv[1] if len(sys.argv) > 1 else 'ls'  # Default command
    print(executor.execute(command))