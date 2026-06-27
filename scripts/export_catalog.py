"""Rebuild the shipped catalog using the deterministic selector.

This compatibility entry point intentionally delegates to select_resources.py;
the selection and export are one atomic operation so profiles and manifests
cannot drift apart.
"""

from select_resources import main

if __name__ == "__main__":
    main()
