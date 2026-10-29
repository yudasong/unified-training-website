#!/usr/bin/env python3
"""Publish this blog under yudasong.github.io/unified-training/."""

from pathlib import Path
import shutil
import subprocess
import tempfile


SOURCE = Path(__file__).resolve().parent
REPOSITORY = "https://github.com/yudasong/yudasong.github.io.git"
PROJECT = "unified-training"
FILES = (
    "index.html",
    "style.css",
    "site.js",
    "typography.js",
    "teaser-animation.css",
    "teaser-animation.js",
    "assets",
)


def git(*args, cwd):
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, text=True, capture_output=True
    ).stdout.strip()


def main():
    for name in FILES:
        if not (SOURCE / name).exists():
            raise FileNotFoundError(SOURCE / name)
    revision = git("rev-parse", "--short", "HEAD", cwd=SOURCE)
    with tempfile.TemporaryDirectory(prefix="unified-training-publish-") as tmp:
        checkout = Path(tmp)
        git("clone", "--depth", "1", "--filter=blob:none", "--sparse",
            "--branch", "master", REPOSITORY, ".", cwd=checkout)
        git("sparse-checkout", "set", PROJECT, cwd=checkout)
        destination = checkout / PROJECT
        if destination.is_symlink():
            raise RuntimeError("Refusing to publish into a symlink")
        if destination.exists():
            shutil.rmtree(destination)
        destination.mkdir()
        for name in FILES:
            source = SOURCE / name
            target = destination / name
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copy2(source, target)
        git("add", "--", PROJECT, cwd=checkout)
        changed = git("diff", "--cached", "--name-only", cwd=checkout).splitlines()
        if not changed:
            print("The published source is already up to date.")
            return
        if any(not name.startswith(PROJECT + "/") for name in changed):
            raise RuntimeError("Unexpected changes outside the project folder")
        git("commit", "-m", f"Publish Unified Training blog ({revision})", cwd=checkout)
        git("push", "origin", "master", cwd=checkout)
        print("Published source to https://yudasong.github.io/unified-training/")
        print("GitHub Pages will serve the update after its build completes.")


if __name__ == "__main__":
    main()
