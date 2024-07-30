import os
from pathlib import Path

from environ import Env
from split_settings.tools import include

include(
    "components/*.py",
)
