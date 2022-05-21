#!/usr/bin/env python3

import getpass
import os
import pathlib
from typing import Optional

from .external import external
from .subprocess_utils import SubprocessUtils


class Environment:
    @classmethod
    @external
    def get_user(cls) -> str:
        return getpass.getuser()

    @classmethod
    @external
    def get_env(cls, name: str) -> Optional[str]:
        return os.getenv(name)

    @classmethod
    def get_repo_root(cls) -> pathlib.Path:
        result = SubprocessUtils.run(["git", "rev-parse", "--show-toplevel"])
        return pathlib.Path(result.stdout.strip())
