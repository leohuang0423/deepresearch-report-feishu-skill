# Release Engineering

## Summary

This repository is the public GitHub release surface for the stable skill slug `research-feishu-report-cocreate`.

The internal source bundle is not pushed directly. Public release generation must:

- export only the approved public surface
- remove local absolute paths
- remove clicklink duplicates, `.DS_Store`, and lockfiles
- keep self-contained platform skill folders
- preserve the stable skill slug while using a human-readable repo/release name

## Public Projection Rules

### Keep

- `skills/<platform>/research-feishu-report-cocreate`
- root docs and manifests
- public validation fixtures
- GitHub marketplace/plugin metadata

### Strip

- `experiments/`
- internal runner logs
- local filesystem traces
- clicklink-hash duplicates
- legacy internal bundle names
- repo-external installation assumptions

## Required Checks

### Structure

- `python3 scripts/validate_public_repo.py --repo-root .`

### Install smoke

- `python3 scripts/run_install_smoke.py --repo-root .`

### Packaging

- `python3 scripts/package_release.py --repo-root .`

## Agent Acceptance Standard

One release gate is explicitly agent-first:

- give the GitHub URL to Claude Code or OpenClaw
- the agent can infer installation steps from repository structure and docs
- the agent can run minimum validation
- the agent can report results back to the user

This standard is tracked in [tests/public_validation_cases.yaml](../tests/public_validation_cases.yaml).

