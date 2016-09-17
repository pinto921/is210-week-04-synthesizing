#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""farenheit to celsius"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')

    def farenheit_to_celcius(degrees):
    """farenheit to celcius

    Args:
        degrees: degree in farenheit

    Returns:
        decimal: degree in celsius

    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('-3.11722222222222222222'

    """
    degrees = decimal.Decimal(degrees)
    degrees = (degrees - 32) * 5/9
    return degrees

    def celsius_to_kelvin

    """celsius to kelvin

    Args:
        degrees: degrees in celsius

    Returns:
        decimal: degree in kelvin

    Examples:
        >>>celsius_to_kelvin
        Decimal('373.15')

        >>>celsius_to_kelvin
        Decimal('323.15')

    """
    degrees = degrees + ABSOLUTE_DIFFERENCE
    return degrees

    def fahrenheit_to_kelvin(degrees):
    """ fahrenheit to kelvin
    Args:
        degrees: degree in fahrenheit

    returns:
        decimal: degree in kelvin

    examples:
        >>>fahrenheit_to_kelvin(212)
        Decimal('373.15')

        >>>fahrenheit_to_kelvin(100)
        decimal('310.92777777777777777778'

        """
    degrees = fahrenheit_to_celsius(degrees)
    degrees = celsius_to_kelvin(degrees)
    return degrees
