import os
from mcp_tool import mcp

if __name__ == "__main__":
    # Detect Codespace forwarded URL
    codespace_port = os.getenv("PORT", "3333")
    print(f"🚀 Starting MCP server on port {codespace_port}...")
    mcp.run()  # Do not add host/port arguments
