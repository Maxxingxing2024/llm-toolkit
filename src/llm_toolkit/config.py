import os
from dataclasses import dataclass

DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL = "gpt-4o-mini"


@dataclass
class AppConfig:
    api_key: str
    base_url: str = DEFAULT_BASE_URL
    model: str = DEFAULT_MODEL
    timeout: int = 30

    def __post_init__(self) -> None:
        if not self.api_key:
            raise ValueError("api_key 不能为空，请通过环境变量注入")


def load_config(env: dict | None = None) -> AppConfig:
    source = os.environ if env is None else env
    return AppConfig(
        api_key=source.get("API_KEY", ""),
        base_url=source.get("BASE_URL", DEFAULT_BASE_URL),
        model=source.get("MODEL", DEFAULT_MODEL),
        timeout=int(source.get("TIMEOUT", "30")),
    )