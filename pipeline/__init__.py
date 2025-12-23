# pipeline/__init__.py
"""
Pipeline package for secure_data_pipeline project.

This package contains the main orchestrator for running the data pipeline.
"""

from .run_pipeline import run_pipeline

__all__ = ["run_pipeline"]
