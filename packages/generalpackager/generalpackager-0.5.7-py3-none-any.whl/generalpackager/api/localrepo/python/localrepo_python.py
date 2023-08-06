import sys

from coverage import Coverage
from generalfile import Path
from generallibrary import Terminal, EnvVar, deco_require, Log, RedirectStdout

from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.api.localrepo.python.metadata_python import Metadata_Python


class LocalRepo_Python(LocalRepo):
    _cls_target = LocalRepo.Targets.python
    _cls_metadata = Metadata_Python

    # Put in generalfile?
    @staticmethod
    def get_python_exe_path():
        """ Return an absolute path to the current python exe filee. """
        return Path(sys.executable)

    def unittest(self):
        """ Run unittests for this repository.
            Sets self.coverage to total percentage with one decimal. """

        with self.get_test_path().as_working_dir():
            Terminal("coverage", "run", "-m", "unittest", "discover", capture_output=False)
            coverage = Coverage()
            coverage.load()
            with RedirectStdout():
                self.coverage = round(coverage.report(), 1)

        # Terminal("-m", "unittest", "discover", str(self.get_test_path()), python=True)

    @deco_require(LocalRepo.exists)
    def pip_install_editable(self):
        """ Install this repository with pip and -e flag. """
        with self.path.get_parent().as_working_dir():
            Log().debug(f"Pip install for {self}")
            Terminal("-m", "pip", "install", "-e", self.name, capture_output=False, python=True)

    @deco_require(LocalRepo.exists)
    def pip_uninstall(self):
        """ Uninstall this repository with pip."""
        Terminal("-m", "pip", "uninstall", "-y", self.metadata.name, python=True)

    @deco_require(LocalRepo.exists)
    def create_sdist(self):
        """ Create source distribution. """
        with self.path.as_working_dir():
            Terminal("setup.py", "sdist", "bdist_wheel", python=True)

    @deco_require(LocalRepo.exists)
    def upload(self):
        """ Upload local repo to PyPI.
            Todo: Make sure twine is installed when trying to upload to pypi.
            Todo: Look into private PyPI server where we could also do dry runs for test.
            https://github.com/pypa/twine/issues/207"""
        if self.metadata.private:
            raise AttributeError("Cannot upload private repo.")

        self.create_sdist()
        with self.path.as_working_dir():
            Terminal("-m", "twine", "upload", "dist/*", python=True)

    @deco_require(LocalRepo.exists)
    def generate_exe(self, file_path=None):
        """ Generate an exe file for target file_path python file. """
        if file_path is None:
            file_path = self.get_exetarget_path()
        assert file_path.exists()

        with self.path.as_working_dir():
            Terminal("-m", "PyInstaller", file_path, "--onefile", "--windowed", python=True)
