import sys
import os

this_dir = os.path.dirname(os.path.abspath(__file__))
server_root = os.path.dirname(this_dir)

if server_root not in sys.path:
    sys.path.insert(0, server_root)
