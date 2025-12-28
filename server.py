from mcp_tool import mcp

if __name__ == "__main__":
    # FastMCP default URL: http://localhost:3333
    mcp.run(host="0.0.0.0", port=3333)
