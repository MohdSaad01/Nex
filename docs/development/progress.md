# Nex Progress

This is a concise implementation record, and a full implementation log. Each entry provides information on what was implemented and why.

# M1 — `nex init`

- Set up the `nex` CLI entry point using `[project.scripts]` in `pyproject.toml`.
- Learned how `argparse` subparsers can handle commands such as `nex init`.
- Separated CLI command parsing from repository functionality.
- Investigated `pathlib` for filesystem operations and studied Git's repository initialization structure.
- Designed the initial `.nex/` repository structure and started implementing `nex init`.

# M2 — `nex add`

- Implemented recursive file existence checking.
- Defined the initial `.nexignore` system.
- Added file hashing using SHA-256.
- Added index-based object tracking.

# M3 — `nex commit`

- Initialized the commit functionality.
- Implemented `nex commit`.
- Added commit object storage and HEAD tracking.


# M4 - `nex status`
- Collected paths from HEAD and index.
- To be implemented