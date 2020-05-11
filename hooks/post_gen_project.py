import io
import json
import tarfile
from pathlib import Path
from typing import List, Union
from urllib.request import urlopen

github_url = "https://api.github.com/repos"
navigation_url = f"{github_url}/meatballs/anvil-navigation"


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


def inject_dependencies(repo_url: str, files: Union[List[Path], Path]) -> None:
    """Fetch the latest source code and extract files to the project folder"""
    if isinstance(files, Path):
        files = [files]
    tarball_url = github_latest_tarball_url(repo_url)
    tarball = latest_tarball(tarball_url)
    for file in files:
        extract_file(tarball, file)


if __name__ == "__main__":
    inject_dependencies(navigation_url, Path("client_code", "navigation.py"))