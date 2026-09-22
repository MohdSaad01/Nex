# Nex Progress

This is a concise implementation record, and a full implementation log. Each entry provides information on what was implemented and why.

# M1 — `nex init`

- Set up the `nex` CLI entry point using `[project.scripts]` in `pyproject.toml`.
- Learned how `argparse` subparsers can handle commands such as `nex init`.
- Separated CLI command parsing from repository functionality.
- Investigated `pathlib` for filesystem operations and studied Git's repository initialization structure.
- Designed the initial `.nex/` repository structure and started implementing `nex init`.

# M2 - `nex add`

- Implement efficient recursive file existence check
- While implementing `nex add` i also defined the nex ignore system.
- More to be implemented