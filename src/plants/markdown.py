#!/usr/bin/env python3


class MarkdownEscapedString(str):
    def __new__(cls, text: str) -> str:
        text = text.replace("\n", "<br/>")
        for pattern in [
            "\\",  # Existing backslashes
            ". ",  # Numbered lists
            "#",  # Headers
            "(",  # Links
            ")",  # Links
            "[",  # Links
            "]",  # Links
            "-",  # Bulleted lists
            "*",  # Bulleted lists and emphasis
            "_",  # Emphasis
            "`",  # Code
            "|",  # Tables
            "~",  # Strikethrough
        ]:
            text = text.replace(pattern, f"\\{pattern}")
        return super().__new__(cls, text)
