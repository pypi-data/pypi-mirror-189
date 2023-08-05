
# release level is a alpha, b beta, rc candidate or f final
# (major, minor, micro, release level, release build)
__version_info__ = [0, 0, 0, "b", 1]

__version__ = f"{__version_info__[0]}.{__version_info__[1]}.{__version_info__[2]}"

if __version_info__[3] != 'f':
    __version__ = f"{__version__}{__version_info__[3]}{__version_info__[4]}"
