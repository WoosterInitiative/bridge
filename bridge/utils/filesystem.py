import stat
import sys
from pathlib import Path

from bridge.console import log_error


def set_executable(file_path: Path) -> None:
    file_path.chmod(
        file_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    )


def resolve_project_dir() -> Path:
    current_dir = Path.cwd()
    manage_py_path = current_dir / "manage.py"
    if not manage_py_path.exists():
        log_error(
            f"No manage.py file found in {current_dir}. "
            "Run the command from the same directory as manage.py"
        )
        sys.exit(1)

    return Path(current_dir)


def resolve_dot_bridge() -> Path:
    project_dir = resolve_project_dir()

    def _create(
        path: str | Path, is_file: bool = False, file_content: str = ""
    ) -> None:
        path = Path(path)
        if not path.exists():
            if is_file:
                with path.open("w") as f:
                    f.write(file_content.strip())
            else:
                path.mkdir(parents=True)

    # Create .bridge
    bridge_path = project_dir / ".bridge"
    _create(bridge_path)
    # Create pgdata
    pgdata_path = bridge_path / "pgdata"
    _create(pgdata_path)
    # Create .gitignore
    gitignore_content = """
# This folder is for bridge configuration. Do not edit.

# gitignore all content, including this .gitignore
*
    """
    gitignore_path = bridge_path / ".gitignore"
    _create(gitignore_path, is_file=True, file_content=gitignore_content)
    return bridge_path


def do_the_check(path_str: str) -> bool:
    return Path(path_str).exists()


def check_if_path_exists(path_str: str) -> bool:
    return do_the_check(path_str)
