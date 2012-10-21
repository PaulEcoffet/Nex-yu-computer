# -*- coding: utf-8 -*-

import string
import random


def code_generator(size=6, chars=string.ascii_uppercase +\
                    string.ascii_lowercase + string.digits):
    """Generate a random string of length 'size' and with chars 'chars'"""
    return ''.join(random.choice(chars) for dummy in range(size))
