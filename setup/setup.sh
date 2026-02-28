#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

log() {
  printf "[setup] %s\n" "$1"
}

fail() {
  printf "[setup][error] %s\n" "$1" >&2
  exit 1
}

have_cmd() {
  command -v "$1" >/dev/null 2>&1
}

detect_os() {
  case "$(uname -s)" in
    Darwin) echo "macos" ;;
    Linux) echo "linux" ;;
    *) echo "other" ;;
  esac
}

find_chrome() {
  local os="$1"
  if [[ "$os" == "macos" ]]; then
    [[ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]] && return 0
    [[ -x "$HOME/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]] && return 0
  elif [[ "$os" == "linux" ]]; then
    have_cmd google-chrome && return 0
    have_cmd google-chrome-stable && return 0
    have_cmd chromium && return 0
    have_cmd chromium-browser && return 0
  fi
  return 1
}

ensure_python() {
  if have_cmd python3; then
    PYTHON_BIN="python3"
  elif have_cmd python; then
    PYTHON_BIN="python"
  else
    fail "Python is not installed. Install Python 3.10+ and run this script again."
  fi
  log "Using Python: $($PYTHON_BIN -V)"
}

create_venv() {
  if [[ ! -d "$VENV_DIR" ]]; then
    log "Creating virtual environment at $VENV_DIR"
    "$PYTHON_BIN" -m venv "$VENV_DIR"
  else
    log "Virtual environment already exists at $VENV_DIR"
  fi
  # shellcheck source=/dev/null
  source "$VENV_DIR/bin/activate"
}

install_packages() {
  log "Upgrading pip"
  pip install --upgrade pip

  if [[ -f "$ROOT_DIR/requirements.txt" ]]; then
    log "Installing Python dependencies from requirements.txt"
    pip install -r "$ROOT_DIR/requirements.txt"
  else
    # Fallback for cases where requirements.txt is missing.
    local deps=(
      selenium
      undetected-chromedriver
      pyautogui
      python-dotenv
      flask
      flask-cors
      openai
      google-generativeai
    )
    log "Installing Python dependencies (fallback list)"
    pip install "${deps[@]}"
  fi
}

main() {
  local os
  os="$(detect_os)"
  [[ "$os" == "other" ]] && fail "Unsupported OS. Use macOS or Linux."

  ensure_python
  create_venv
  install_packages

  if find_chrome "$os"; then
    log "Google Chrome/Chromium detected."
  else
    log "Chrome not found. Install Google Chrome (or Chromium) before running runAiBot.py."
    if [[ "$os" == "macos" ]]; then
      log "Download: https://www.google.com/chrome/"
    else
      log "Install from your distro package manager or: https://www.google.com/chrome/"
    fi
  fi

  log "Setup complete."
  log "Activate venv: source \"$VENV_DIR/bin/activate\""
  log "Run bot: python \"$ROOT_DIR/runAiBot.py\""
}

main "$@"
