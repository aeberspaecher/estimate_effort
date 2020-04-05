#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Perform PERT estimation of efforts.
"""

from math import sqrt


def pert(optimistic, realisitic, pessimistic):
    # PERT distribution
    exp = (optimistic + 4*realisitic + pessimistic)/6.
    simga = (pessimistic - optimistic)/6.

    return exp, simga


def geo_mean(min_guess, max_guess):
    # geometric mean

    return sqrt(min_guess*max_guess)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=
                                     '''Perform PERT or geometric mean estimation.
                                     Two arguments (min, max): geometric mean;
                                     Three arguments (optimistic, realisitic, pessimistic): PERT''')

    parser.add_argument('guesses', action='store', metavar='guesses', nargs="+", type=float,
                        help='Guesses (arbitrary order)')
    args = parser.parse_args()

    if len(args.guesses) == 3:
        mean, sigma = pert(*sorted(args.guesses))
        print("PERT estimate: {:.1f} ± {:.1f} (2σ / 95% confidence) [time units]".format(mean, 2*sigma))
    elif len(args.guesses) == 2:
        guess = geo_mean(*sorted(args.guesses))
        print("Geometric mean estimation: {:.1f} [time units]".format(guess))
    else:
        print("Use either two or three arguments.")
