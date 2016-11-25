#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Going shopping"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Takes one argument

    Args:
        shoplist(dict): Key should be the item name as found in FRUIT.

    Examples:

        >>> shoplist = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_cost_per_item(shoplist)
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    
    return {key: FRUIT[key] * shoplist[key] for key in shoplist.iterkeys()
            if key in FRUIT}


def get_total_cost(shoplist):
    """Takes one argument, a dictionary called shoplist.

    Args:
        shoplist(dict): key should be the same name found in FRUIT.

    Examples:

        >>> shoplist = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_total_cost(shoplist)
        112.80
    """
    new_list = get_cost_per_item(shoplist)
    return sum([val for val in new_list.itervalues()])
