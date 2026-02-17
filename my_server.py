from fastmcp import FastMCP
from fastmcp.utilities.types import Image, Audio, File
from fastmcp.server.context import Context
from fastmcp.dependencies import CurrentContext



# run the server with watchmedog

#watchmedo auto-restart --patterns="*.py" --recursive -- python my_server.py

mcp = FastMCP("My MCP Server")

# @mcp.tool
# async def process_file(file_uri: str, ctx: Context = CurrentContext()) -> str:
#     """Processes a file, using context for logging and resource access."""
#     await ctx.report_progress(progress=50, total=100)
#     # await ctx.info(f"Processing {file_uri}")
#     return "Processed file"


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b 

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)