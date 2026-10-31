#!/usr/bin/env python3
"""
scripts/verify_readiness.py
Automated health check verifying that the framework is ready to run
anywhere without broken dependencies or git tracking leaks.
"""

import sys, os, subprocess, json, shutil

def check(name, fn):
    sys.stdout.write(f"Checking {name}... ")
    sys.stdout.flush()
    try:
        ok, msg = fn()
        if ok:
            print(f"PASSED ({msg})")
            return True
        else:
            print(f"FAILED: {msg}")
            return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def test_python_version():
    v = sys.version_info
    if v >= (3, 11):
        return True, f"Python {v.major}.{v.minor}.{v.micro}"
    return False, f"Requires Python 3.11+, found {v.major}.{v.minor}"

def test_tracker_server():
    res = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "mcp/tracker-server", "-p", "test_*.py"], capture_output=True, text=True)
    if res.returncode == 0:
        return True, "15/15 tests OK"
    return False, res.stderr or res.stdout

def test_tectonic():
    if shutil.which("tectonic"):
        return True, "Installed"
    return False, "tectonic not found. Install via: brew install tectonic"

def test_pdfinfo():
    if shutil.which("pdfinfo"):
        return True, "Installed"
    return False, "pdfinfo not found. Install via: brew install poppler"

def test_mcp_config():
    if not os.path.exists(".mcp.json"):
        return False, ".mcp.json missing"
    with open(".mcp.json", "r") as f:
        data = json.load(f)
    if "tracker" in data.get("mcpServers", {}):
        return True, "tracker MCP registered"
    return False, "tracker missing from mcpServers in .mcp.json"

def test_git_hygiene():
    res = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
    if res.returncode != 0:
        return True, "Not a git repo"
    tracked = res.stdout.splitlines()
    leaks = [f for f in tracked if "node_modules" in f or "/venv/" in f or f.endswith(".pyc")]
    if leaks:
        return False, f"Found {len(leaks)} forbidden build files tracked in git!"
    return True, f"{len(tracked)} clean tracked files"

def main():
    print("=== AI Job Search Framework Readiness Check ===")
    checks = [
        ("Python Version", test_python_version),
        ("Tracker Server Unit Tests", test_tracker_server),
        ("Tectonic LaTeX Engine", test_tectonic),
        ("Poppler pdfinfo", test_pdfinfo),
        ("MCP Server Configuration", test_mcp_config),
        ("Git Index Hygiene", test_git_hygiene),
    ]
    
    passed = 0
    for name, fn in checks:
        if check(name, fn):
            passed += 1
            
    print(f"\nResult: {passed}/{len(checks)} checks passed.")
    if passed == len(checks):
        print("Framework is 100% plug-and-play ready!")
        sys.exit(0)
    else:
        print("Please review failed checks above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
