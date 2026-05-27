# Repository Dependency Map (Wave 2)

Primary dependency flow:

1. Governance definitions influence canon/candidate interpretation.
2. Core systems artifacts inform project and archive structures.
3. Archive and evidence lanes feed public documentation and project narratives.
4. Scripts/tests/schemas provide verification and consistency checks.
5. Root navigation and domain indexes expose these links for public access.

Validation dependencies referenced in root README:
- `python -m pytest -q` (reference_impl scope)
- `bash run_checks.sh`
- `ruff check` and `ruff format --check` for reference implementation paths
