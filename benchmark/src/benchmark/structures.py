from dataclasses import dataclass, asdict
from subprocess import CompletedProcess


@dataclass
class LakeBuildResult:
    """
    Represents the result of a lake build command.
    """

    exit_code: int
    stdout: str
    stderr: str

    @classmethod
    def from_subprocess_result(cls, result: CompletedProcess[str]) -> "LakeBuildResult":
        return cls(result.returncode, result.stdout, result.stderr)

    @property
    def dictionary(self) -> dict:
        return asdict(self)
