"""This file provides with storage related functions and classes.

"""
import os

dbs_registry = {}


def register_db(db=None):
    """
    :param db:
    :return:
    """
    pass


class DBBase(object):
    """
    """

    @classmethod
    def client(cls):
        raise NotImplementedError

    @classmethod
    def name(cls):
        raise NotImplementedError


class FileDB(DBBase):
    """
    """

    @classmethod
    def client(cls):
        raise NotImplementedError

    @classmethod
    def base_path(cls):
        raise NotImplementedError

    @classmethod
    def name(cls):
        raise NotImplementedError

    @classmethod
    def full_path(cls):
        return os.path.join(cls.base_path(), cls.base_path())
