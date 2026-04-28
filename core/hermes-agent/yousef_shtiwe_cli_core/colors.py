"""Shared ANSI color utilities for YOUSEF SHTIWE CLI modules."""

import os
import sys

def should_use_color() -> bool:
    if os.environ.get("NO_COLOR") is not None:
        return False
    if os.environ.get("TERM") == "dumb":
        return False
    if not sys.stdout.isatty():
        return False
    return True

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    
    # YOUSEF SHTIWE Predatory Palette
    BLOOD_RED = "\033[38;5;160m"      # Main accent
    SHADOW_GRAY = "\033[38;5;236m"    # Borders
    VOID_BLACK = "\033[38;5;0m"       # Backgrounds
    MATRIX_GREEN = "\033[38;5;46m"    # Prompts
    ERROR_RED = "\033[38;5;196m"      # Critical
    
    # Compatibility mapping for original colors
    RED = BLOOD_RED
    GREEN = MATRIX_GREEN
    YELLOW = "\033[38;5;220m"
    BLUE = "\033[38;5;27m"
    MAGENTA = "\033[38;5;125m"
    CYAN = "\033[38;5;39m"
    WHITE = "\033[38;5;255m"

def color(text: str, *codes) -> str:
    if not should_use_color():
        return text
    return "".join(codes) + text + Colors.RESET
