import os
import platform
import itermate
import itertools


try:
    # on py27 make map/filter behave like an iterator
    map = itertools.imap
    filter = itertools.ifilter
except AttributeError:
    # py3+
    pass



def where( filename ):
    """ Returns all matching file paths. """

    return list(iwhere(filename))


def first( filename ):
    """ Returns first matching file path. """

    try:
        return next(iwhere(filename))
    except StopIteration:
        return None


def iwhere( filename ):
    """ Like where() but returns an iterator. """

    possible_paths =      _gen_possible_matches( filename )
    existing_file_paths = filter( os.path.isfile, possible_paths )
    return existing_file_paths


def _gen_possible_matches( filename ):
    path_parts =     os.environ.get("PATH", "").split( os.pathsep )
    path_parts =     itertools.chain( (os.curdir,), path_parts )
    possible_paths = map( lambda path_part: os.path.join(path_part, filename), path_parts )

    if platform.system() == "Windows":
        possible_paths = itermate.imapchain( lambda path: (path, path+".bat", path+".com", path+".exe"), possible_paths )

    possible_paths = map( os.path.abspath, possible_paths )

    result = itermate.unique( possible_paths )

    return result
