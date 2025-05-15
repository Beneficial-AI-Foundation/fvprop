from pathlib import Path
import subprocess as sp
import shutil
import tempfile


def lakeproj_copy_temp(lake_dir: Path) -> Path:
    """Creates a temporary directory and copies the lake project to it."""
    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    shutil.copytree(
        lake_dir,
        tmpdir,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".lake/"),
    )
    return Path(tmpdir)


def lake_build(cwd: Path) -> sp.CompletedProcess:
    """Run `lake build` in the given directory."""
    result = sp.run(["lake", "build"], text=True, capture_output=True, cwd=cwd)
    return result
