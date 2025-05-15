from pathlib import Path
from mcp.server.fastmcp import FastMCP
from benchmark.mcp.tools.lake import lakeproj_copy_temp, lake_build

LAKE_DIR = Path.cwd() / "artifacts" / "temp-lakeproj"


def mk_mcp() -> FastMCP:
    """
    Create a FastMCP instance for the FVProp benchmark generator.
    """
    mcp = FastMCP("FVProp-benchgen")

    @mcp.tool()
    def write_lean_and_lake_build(lean_code: str) -> None:
        """
        Check if the lake executable is available and can be run.
        """
        tmpdir = lakeproj_copy_temp(LAKE_DIR)
        with open(tmpdir / "TempArtifacts" / "Basic.lean", "w") as basic:
            basic.write(lean_code)
        result = lake_build(tmpdir)
        print(result.returncode)
        pass

    return mcp
