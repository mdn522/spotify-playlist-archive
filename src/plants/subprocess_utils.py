#!/usr/bin/env python3

import logging
import subprocess
from typing import Sequence

from .external import external

logger: logging.Logger = logging.getLogger(__name__)


class SubprocessUtils:
    @classmethod
    @external
    def run(
        cls,
        args: Sequence[str],
        check: bool = False,
    ) -> "subprocess.CompletedProcess[str]":
        return subprocess.run(
            args=args,
            capture_output=True,
            check=check,
            text=True,
        )
