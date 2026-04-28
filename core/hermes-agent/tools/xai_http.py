"""Shared helpers for direct xAI HTTP integrations."""

from __future__ import annotations


def hermes_xai_user_agent() -> str:
    """Return a stable Hermes-specific User-Agent for xAI HTTP calls."""
    try:
        from yousef_shtiwe_cli_core import __version__
    except Exception:
        __version__ = "unknown"
    return f"yousef-sovereign-core/{__version__}"
