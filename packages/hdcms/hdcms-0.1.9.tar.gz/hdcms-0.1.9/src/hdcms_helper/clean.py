from typing import List, Tuple
import sys
import os
import shutil

RED_BG = "\x1b[41m"
CLR = "\x1b[0m"
GRN = "\x1b[32m"
VLT = "\x1b[35m"

def compute_changes(lines: List[str]) -> Tuple[List[str], List[str]]:
    """figure out which lines to delete and return the acceptable lines, and the changes"""
    changes = []
    new_lines = []

    # we include a header of lines starting with '#' (essentially like comments above the data)
    content_start = 0
    for line in lines:
        if line[0] != '#':
            break
        new_lines.append(line)
        content_start += 1

    # deletes lines that aren't numbers, deletes leading + trailing whitespace
    for i, line in enumerate(lines[content_start:], start=content_start):
        line = line.rstrip()
        stripped = line.lstrip()

        if not stripped[0].isdigit():
            # delete line
            changes.append(f"{GRN}{i}{CLR}:{RED_BG}{line}{CLR}")
            continue
        elif len(line) != len(stripped):
            leading_whitespace = " "*(len(line) - len(stripped))
            changes.append(f"{GRN}{i}{CLR}:{RED_BG}{leading_whitespace}{CLR}{stripped}")
        new_lines.append(stripped)

    return new_lines, changes

def backup_file(src: str, dryrun=False, verbose=False):
    """this creates a backup file for file `src`"""
    # deal with ppl trying to escape tmp dir
    dest = os.path.join(get_tmpdir(), src.replace("..", "_"))

    # remove `dest`
    if verbose:
        print(f"removing (if exists): {dest}")
    if not dryrun:
        try:
            os.remove(dest)
        except FileNotFoundError:
            pass # it's okay if the file doesn't exist, we just want to remove it if it does

    if verbose:
        print(f"making (if doesn't exist): {os.path.dirname(dest)}")
    if not dryrun:
        os.makedirs(os.path.dirname(dest), exist_ok=True)

    if verbose:
        print(f"copying: {src} to {dest}")
    if not dryrun:
        shutil.copy(src, dest)

def parse_args(dryrun=False, verbose=False):
    """parse out the arguments from commandline"""
    if sys.argv[1][0] == '-':
        if sys.argv[1] == '--dry-run':
            sys.argv.pop(1)
            return parse_args(dryrun=True, verbose=verbose)
        elif sys.argv[1] == '--verbose':
            sys.argv.pop(1)
            return parse_args(dryrun=dryrun, verbose=True)
        elif sys.argv[1] == '--help':
            print("--dry-run, --verbose, --help")
            exit(2)
        else:
            print(f"unknown option: {sys.argv[1]}")
            exit(1)
    else:
        return dryrun, verbose

def clean(dryrun=False, verbose=False):
    """this function coordinates most of the work, makes backups, reads file and maches changes"""
    for path in sys.argv[1:]:
        backup_file(path, dryrun=dryrun, verbose=verbose)

        with open(path) as f:
            lines, changes = compute_changes(f.readlines())

            if len(changes) != 0:
                print(f"{VLT}{path}{CLR}")
                for change in changes:
                    print(change)

        if not dryrun:
            with open(path, "w") as f:
                f.writelines(lines)

    print(f"backups are in {get_tmpdir()}[/path/to/file]")

def get_tmpdir(dir="hdcms_backup"):
    """returns the name of a tmp directory"""
    return f"/tmp/{dir}" if sys.platform != "win32" else f"C:\\Users\\AppData\\Local\\Temp\\{dir}"

def main():
    """main"""
    dryrun, verbose = parse_args()
    clean(dryrun=dryrun, verbose=verbose)

# this ensures we only run it if we are running this file from the commandline, rather than importing it
if __name__ == "__main__":
    main()
