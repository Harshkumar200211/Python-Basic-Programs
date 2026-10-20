"""92. Inspect Python runtime information with sys."""

import sys
import platform

print("Python version:", sys.version.split()[0])
print("Python executable:", sys.executable)
print("Operating system:", platform.system())
print("Platform:", platform.platform())
print("Python module search path entries:", len(sys.path))
