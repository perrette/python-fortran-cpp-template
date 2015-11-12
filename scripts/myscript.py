#!/usr/bin/env python2.7
"""Template script
"""
import os, sys
from mypackage import py_add, f_mult, c_div

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("-a", type=float, nargs=3, help="first operand", required=True)
    parser.add_argument("-b", type=float, nargs=3, help="second operand", required=True)
    parser.add_argument("-o","--operator", default="py_add", choices=["f_mult", "py_add", "c_div"], help="operator")

    args = parser.parse_args()

    print "operands"
    print " a:",args.a
    print " b:",args.b

    if args.operator == "py_add":
        print "...using python add..."
        res = py_add(args.a, args.b)

    elif args.operator == "f_mult":
        print "...using fortran mult..."
        res = f_mult(args.a, args.b)

    elif args.operator == "c_div":
        print "...using c++ div..."
        res = c_div(args.a, args.b)

    else:
        raise ValueError("that's wrong")

    print "result"
    print res
