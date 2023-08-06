"""End-to-end tests."""

import random
import re
import shutil
import subprocess  # noqa: S404
from functools import partial
from pathlib import Path
from typing import Iterator

import pytest

from git_changelog import Changelog
from git_changelog.build import bump
from git_changelog.cli import build_and_render
from git_changelog.commit import AngularConvention
from git_changelog.templates import get_template

VERSIONS = ("0.1.0", "0.2.0", "0.2.1", "1.0.0", "1.1.0", "")
KEEP_A_CHANGELOG = get_template("keepachangelog")


def _git(*args) -> str:
    return subprocess.check_output([shutil.which("git") or "git", *args], text=True)  # noqa: S603


def _commit(repo, filename, section):
    with repo.joinpath(filename).open("a") as fh:
        fh.write(str(random.randint(0, 1)))  # noqa: S311
    _git("-C", repo, "add", "-A")
    _git("-C", repo, "commit", "-m", f"{section}: Commit with '{section}' type")


@pytest.fixture(scope="module", name="repo")
def git_repo(tmp_path_factory) -> Iterator[Path]:
    """Pytest fixture setting up a temporary Git repository.

    Parameters:
        tmp_path_factory: Utility to create temporary directories.

    Yields:
        The path to a temporary Git repository.
    """
    tmp_path = tmp_path_factory.mktemp("git_changelog")
    git = partial(_git, "-C", str(tmp_path))
    commit = partial(_commit, tmp_path, "dummy")
    git("init")
    git("config", "user.name", "dummy")
    git("config", "user.email", "dummy@example.com")
    git("remote", "add", "origin", "git@github.com:example/example")
    for version in VERSIONS:
        for section in AngularConvention.TYPES.keys():
            commit(section)
            commit(section)
        if version:
            git("tag", version)
    yield tmp_path
    shutil.rmtree(tmp_path)


def test_bumping_latest(repo):
    """Bump latest version.

    Parameters:
        repo: Path to a temporary repository.
    """
    changelog = Changelog(repo, convention=AngularConvention, bump_latest=True)
    # features, no breaking changes: minor bumped
    assert changelog.versions_list[0].planned_tag == bump(VERSIONS[-2], "minor")
    rendered = KEEP_A_CHANGELOG.render(changelog=changelog)
    assert "Unreleased" not in rendered


def test_not_bumping_latest(repo):
    """Don't bump latest version.

    Parameters:
        repo: Path to a temporary repository.
    """
    changelog = Changelog(repo, convention=AngularConvention, bump_latest=False)
    assert changelog.versions_list[0].planned_tag is None
    rendered = KEEP_A_CHANGELOG.render(changelog=changelog)
    assert "Unreleased" in rendered


def test_rendering_custom_sections(repo):
    """Render custom sections.

    Parameters:
        repo: Path to a temporary repository.
    """
    changelog = Changelog(repo, convention=AngularConvention, sections=["feat"])
    rendered = KEEP_A_CHANGELOG.render(changelog=changelog)
    for section_type, section_title in AngularConvention.TYPES.items():
        if section_type != "feat":
            assert section_title not in rendered


def test_rendering_in_place(repo, tmp_path):  # noqa: WPS218
    """Render changelog in-place.

    Parameters:
        repo: Path to a temporary repository.
        tmp_path: A temporary path to write the changelog into.
    """
    output = tmp_path.joinpath("changelog.md")
    _, rendered = build_and_render(
        str(repo),
        convention="angular",
        bump_latest=False,
        output=output.as_posix(),
        template="keepachangelog",
    )
    assert len(re.findall("<!-- insertion marker -->", rendered)) == 2
    assert "Unreleased" in rendered
    latest_tag = "91.6.14"
    assert latest_tag not in rendered
    _git("-C", repo, "tag", latest_tag)
    build_and_render(
        str(repo),
        convention="angular",
        bump_latest=True,
        output=output.as_posix(),
        template="keepachangelog",
        in_place=True,
    )
    rendered = output.read_text()
    assert len(re.findall("<!-- insertion marker -->", rendered)) == 1
    assert "Unreleased" not in rendered
    assert latest_tag in rendered
    _git("-C", repo, "tag", "-d", latest_tag)
