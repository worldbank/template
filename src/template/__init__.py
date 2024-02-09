from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("datalab")
except PackageNotFoundError:
    # package is not installed
    pass
