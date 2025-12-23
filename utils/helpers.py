# utils/helpers.py
import time

def log(message: str):
    """
    Simple timestamped logging function.

    Args:
        message (str): The message to log.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def ensure_output_dir(path: str):
    """
    Ensure that the output directory exists.

    Args:
        path (str): Directory path to create if missing.
    """
    import os
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        log(f"✅ Created directory: {path}")
    else:
        log(f"✅ Directory already exists: {path}")
