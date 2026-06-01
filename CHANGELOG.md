# Changelog

## Initial entries

### Chore — Bump Node.js 20 GitHub Actions before 2026-06-02 cutoff

- `pages.yml`: `actions/upload-pages-artifact` needs to be bumped from v4 (Node 20) to
  v5 (Node 24) ahead of GitHub's 2026-06-02 hard cutoff. The automated agent that
  opened this PR lacked the `workflow` OAuth scope required to write `.github/workflows/`
  files; the one-line change must be applied manually — see PR body for the exact diff.
