# Cookiecutter template for anvil applications
# Copyright (C) 2020 Owen Campbell

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# This program is published at https://github.com/meatballs/anvil-cookiecutter
import io
import json
import shutil
import tarfile
from pathlib import Path
from typing import List, Union
from urllib.request import urlopen

github_url = "https://api.github.com/repos"

dependencies = [
    {
        "definition": {
            "repo_url": f"{github_url}/meatballs/anvil-navigation",
            "files": [Path("client_code", "navigation.py")],
        },
        "include": "yes",
    },
    {
        "definition": {
            "repo_url": f"{github_url}/s-cork/HashRouting",
            "files": [
                Path("client_code", "routing.py"),
                Path("client_code", "_logging.py"),
            ],
        },
        "include": "{{cookiecutter.with_hash_routing}}",
    },
    {
        "definition": {
            "repo_url": f"{github_url}/meatballs/anvil-authorisation",
            "files": [Path("server_code", "authorisation.py")],
        },
        "include": "{{cookiecutter.with_authorisation}}",
    },
]


def github_latest_tarball_url(repo_url: str) -> str:
    """Fetch the url for the latest version of the source code tar.gz file"""
    url = f"{repo_url}/releases/latest"
    with urlopen(url) as response:
        tarball_url = json.loads(response.read().decode("utf-8"))["tarball_url"]
    return tarball_url


def latest_tarball(url: str) -> tarfile.TarFile:
    """Fetch and unzip the tar.gz file from a url"""
    with urlopen(url) as response:
        tarball = tarfile.open(fileobj=io.BytesIO(response.read()), mode="r:gz")
    return tarball


def extract_file(tarball: tarfile.TarFile, path: Path) -> None:
    """Extract a source file from the tarball to a target location

    Parameters
    ----------
    tarball
        A .tar file object
    source
        path to the file for extraction
    target
        path to which the file should be extracted. Defaults to the same as the source
    """
    source_path = str(Path(tarball.getnames()[0], path))
    buffer = tarball.extractfile(source_path)
    with path.open("wb") as file:
        file.write(buffer.read())


def inject_dependency(repo_url: str, files: Union[List[Path], Path]) -> None:
    """Fetch the latest source code and extract files to the project folder"""
    if isinstance(files, Path):
        files = [files]
    tarball_url = github_latest_tarball_url(repo_url)
    tarball = latest_tarball(tarball_url)
    for file in files:
        extract_file(tarball, file)


if __name__ == "__main__":
    for dependency in [
        dependency["definition"]
        for dependency in dependencies
        if dependency["include"] == "yes"
    ]:
        inject_dependency(**dependency)

    Path("server_code", "temp.txt").unlink()
    if "{{cookiecutter.with_authorisation}}" == "no":
        shutil.rmtree(Path("client_code", "Login"))

