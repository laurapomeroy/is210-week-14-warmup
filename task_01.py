#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dog class with subclass Pet"""

import pet


class Dog(pet.Pet):
    """A dog class."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the Dog class that has two major
        parameters.

        Args:
            has_shots(boolean, optional): Defaults to False
            **kwargs: arbitrary arguments dictionary.
        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
