from generalpackager.api.shared.owner import _SharedOwner
from generalpackager.api.shared.name import _SharedName, _SharedAPI

from generallibrary import Ver, Date, get
from generalfile import Path

import requests
import re


def download(url, path):
    """ Todo: Move download to it's own package. """
    data = requests.get(url)
    if data.status_code != 200:
        raise AttributeError(f"Request for url {url} did not yield a status code of 200, it's {data.status_code}.'")

    path = Path(path)

    with path.lock():
        path.get_parent().create_folder()
        with open(str(path), "wb") as file:
            file.write(data.content)
    return path


class PyPI(_SharedAPI, _SharedOwner, _SharedName):
    """ Tools to interface pypi.org """
    DEFAULT_OWNER = "Mandera"

    def __init__(self, name=None, owner=None):
        pass

    @property
    def url(self):
        return f"https://pypi.org/project/{self.name}/"

    def exists(self):
        """ Return whether this API's target exists. """
        return requests.get(url=self.url).status_code == 200

    def get_tarball_url(self, version=None):
        """ Get URL to download tarball. """
        if version is None:
            version = self.get_version()
        return f"https://pypi.io/packages/source/{self.name[0]}/{self.name}/{self.name}-{version}.tar.gz"

    def download(self, path, version=None, overwrite=False):
        """ Download tar ball to cache, extract it, remove tar ball.
            Returns target folder tarball is extracted in. """
        if version is None:
            version = self.get_version()
        path = Path(path)
        temp = Path.get_cache_dir() / "Python/temp.tar.gz"
        download(self.get_tarball_url(version=version), path=temp)
        temp.unpack(base=path, overwrite=overwrite)
        temp.delete(error=False)
        return path / f"{self.name}-{version}"

    def get_owners_packages(self):
        """ Get a set of a owner's packages' names on PyPI. """
        return set(re.findall("/project/(.*)/", requests.get(f"https://pypi.org/user/{self.owner}/").text))

    def get_version(self):
        """ Get version of latest publish on PyPI.

            Todo: Find a faster fetch for latest PyPI version and datetime. """
        version = get(re.findall(f"{self.name} ([.0-9]+)\n", requests.get(self.url).text), 0)
        return Ver(version) if version else None

    def get_date(self):
        """ Get datetime of latest release. """
        date = get(re.findall('Generated (.+) for commit', requests.get(self.url).text), 0)
        return Date(date) if date else None



























