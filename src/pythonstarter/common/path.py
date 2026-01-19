from pathlib import Path
from re import DOTALL, S

# 当前文件路径
_CURRENT_FILE_DIR = Path(__file__).resolve()

# 项目根目录（包含 src 目录的根）
PROJECT_ROOT = _CURRENT_FILE_DIR.parent.parent.parent.parent.absolute()

# Python 包根目录（src 下的 pythonstarter）
PACKAGE_ROOT = _CURRENT_FILE_DIR.parent.parent.absolute()

CONFIG_ROOT = PACKAGE_ROOT / "config"

SECRETS_ROOT = PACKAGE_ROOT / "secrets"
