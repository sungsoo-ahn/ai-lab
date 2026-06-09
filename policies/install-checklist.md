# Install Checklist

Use this checklist for workstation package changes.

## Read-Only Audit

- Confirm OS and architecture with `sw_vers` and `uname -m`.
- Check existing tools with `command -v brew uv git gh rg fd jq yq shellcheck shfmt pre-commit sqlite3`.
- If Homebrew exists, run `brew --version` and `brew bundle check --file agent-system/Brewfile`.

## Approved Installation

- Install Homebrew if missing.
- Add Homebrew shellenv to `~/.zprofile` if the installer does not do so.
- Install the lean baseline with `brew bundle --file agent-system/Brewfile`.

## Verification

- Run `brew --version`.
- Run `brew bundle check --file agent-system/Brewfile`.
- Run `brew doctor` and inspect warnings.
- Run `uv --version`.
- Run `git --version`, `gh --version`, `rg --version`, `fd --version`, `jq --version`, `yq --version`, `shellcheck --version`, `shfmt --version`, and `pre-commit --version`.
- Verify Homebrew SQLite with `$(brew --prefix sqlite)/bin/sqlite3 --version`; macOS may keep `/usr/bin/sqlite3` first because Homebrew `sqlite` is keg-only.
- Create any smoke-test files only under a temporary directory, not in durable memory.

## Known Remediation

If `brew doctor` says `/opt/homebrew` directories are not writable by `sungs`, run this manually in Terminal so macOS can prompt for your password:

```sh
sudo chown -R sungs:admin /opt/homebrew
chmod -R u+w /opt/homebrew
```

Then rerun `brew doctor`.
