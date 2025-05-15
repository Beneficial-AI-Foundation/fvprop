from benchmark.mcp.server import mk_mcp


def main() -> None:
    """
    Entrypoint for the FVProp benchmark generator MCP server.
    """
    mcp = mk_mcp()
    mcp.run()
