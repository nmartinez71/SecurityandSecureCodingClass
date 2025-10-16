import os
import re
import argparse
import logging
import tkinter as tk
from tkinter import filedialog

#define regex patterns
PATTERNS = {
    "AWS Access Key": r"(AKIA|ASIA)[0-9A-Z]{16}",
    "AWS Secret Key": r"(?i)aws(.{0,20})?(secret|access)?.{0,20}?['\"][0-9a-zA-Z/+]{40}['\"]",
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Slack Token": r"xox[baprs]-[0-9a-zA-Z]{10,48}",
    "Private Key": r"-----BEGIN (RSA|DSA|EC|PGP) PRIVATE KEY-----",
    "Generic Password": r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"][^'\"]{6,}['\"]"
}

#assuming Windows only functions with Tkinter, have not tried Linux.
def pick_path():
    root = tk.Tk()
    root.withdraw()  

    choice = filedialog.askopenfilename(title="Select a File")
    if not choice:
        choice = filedialog.askdirectory(title="Select a Directory")
    return choice

def scan_directory(path):
    results = []
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            results.extend(scan_file(full_path))
    return results


def scan_file(filepath):
    findings = []
    try:
        with open(filepath, "r", errors="ignore") as f:
            for lineno, line in enumerate(f, start=1):
                for name, pattern in PATTERNS.items():
                    if re.search(pattern, line):
                        findings.append((filepath, lineno, name, line.strip()))
    except Exception as e:
        logging.error(f"Could not read {filepath}: {e}")
    return findings

def main():
    print("Welcome to the Secret Scanner! \n Select a file to scan.")

    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("-o", "--output", default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    #if no path provided, use File Explorer
    path = args.path or pick_path()
    if not path:
        logging.error("No path selected.")
        return

    results = []
    if os.path.isfile(path):
        logging.info(f"Scanning file: {path}")
        results = scan_file(path)
    elif os.path.isdir(path):
        logging.info(f"Scanning directory: {path}")
        results = scan_directory(path)
    else:
        logging.error(f"Invalid path: {path}")
        return

    #outputs report
    if results:
        print("\nPotential Secrets Found!\n")
        for file, lineno, pattern, line in results:
            print(f"{pattern}: {file} || Ln #:{lineno} || {line}")
    else:
        print("No secrets found.")

if __name__ == "__main__":
    main()
