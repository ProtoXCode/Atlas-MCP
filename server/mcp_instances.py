import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

base_path = Path(__file__).parent
config_path = base_path / 'config.json'

config = json.load(open(config_path))
os.environ['MCP_MODEL'] = config['mcp']['model']

mcp = FastMCP('Atlas MCP')
