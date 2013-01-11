#!/bin/python
# -*- coding: utf-8 -*-


class watchedDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.callback = None

    def setCallback(self, callback):
        self.callback = callback

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        if self.callback is not None:
            self.callback.itemSet(key, value)

    def set(self, key, value):
        dict.set(self, key, value)
        if self.callback is not None:
            self.callback.itemSet(key, value)

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        if self.callback is not None:
            self.callback.itemDeleted(key)
