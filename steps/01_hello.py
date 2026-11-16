import platform, socket
print("Hello from", socket.gethostname())
print("Python", platform.python_version(), "on", platform.machine())