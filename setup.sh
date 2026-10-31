#!/usr/bin/env bash
set -e

echo "=== AI Job Search Framework Setup ==="

# 1. Check prerequisites
echo "Checking prerequisites..."
command -v python3 >/dev/null 2>&1 || { echo >&2 "Error: python3 is required. Aborting."; exit 1; }

HAS_BUN=false
HAS_NPM=false
if command -v bun >/dev/null 2>&1; then
    HAS_BUN=true
    echo "  [x] bun detected ($(bun --version))"
elif command -v npm >/dev/null 2>&1; then
    HAS_NPM=true
    echo "  [x] npm detected ($(npm --version))"
else
    echo "  [!] Neither bun nor npm detected. Portal search CLIs may require node/bun."
fi

if command -v tectonic >/dev/null 2>&1; then
    echo "  [x] tectonic detected"
else
    echo "  [!] Warning: tectonic not found. Install via: brew install tectonic"
fi

if command -v pdfinfo >/dev/null 2>&1; then
    echo "  [x] pdfinfo detected"
else
    echo "  [!] Warning: pdfinfo not found. Install via: brew install poppler"
fi

# 2. Initialize environment config
if [ ! -f .env ]; then
    echo "Initializing .env from config/.env.example..."
    cp config/.env.example .env
fi

# 3. Initialize candidate profile if missing
if [ ! -f config/profile.json ]; then
    echo "Initializing config/profile.json from config/profile.example.json..."
    cp config/profile.example.json config/profile.json
    echo "  -> Please update config/profile.json with your actual candidate details."
fi

# 4. Initialize tracker CSV if missing
if [ ! -f applications.csv ]; then
    echo "Initializing applications.csv from templates/applications_template.csv..."
    cp templates/applications_template.csv applications.csv
fi

# 5. Build search skills
echo "Installing search CLI dependencies..."
for skill_dir in .agents/skills/*-search/cli; do
    if [ -d "$skill_dir" ]; then
        echo "  Configuring $(basename $(dirname "$skill_dir"))..."
        (
            cd "$skill_dir"
            if [ "$HAS_BUN" = true ]; then
                bun install --silent 2>/dev/null || true
            elif [ "$HAS_NPM" = true ]; then
                npm install --silent 2>/dev/null || true
            fi
        )
    fi
done

echo ""
echo "=== Setup complete! ==="
echo "Run readiness check: python3 scripts/verify_readiness.py"
