import pytest

from bridge.config import BridgeConfig
from bridge.framework.django import DjangoHandler


@pytest.fixture
def django_handler(django_settings, tmp_path, mocker) -> DjangoHandler:
    mocker.patch("pathlib.Path.cwd", return_value=tmp_path)
    manage_py_path = tmp_path / "manage.py"
    manage_py_path.touch()
    bridge_config = BridgeConfig()
    return DjangoHandler(
        project_name="test",
        framework_locals=django_settings,
        bridge_config=bridge_config,
    )
