### * Description

SCRIPT_DESCRIPTION = (""
 "Extract random lines from a file, based on probabilities. "
 "Lines in the output are in the same order as in the input file.")

### * Setup

### ** Import

import os
import sys
import argparse
import random

### * Main script functions

### ** _main(argv = None, stdout = None, stderr = None)

def _main(argv = None, stdout = None, stderr = None) :
    """Entry point for the command line script

    Args:
        argv (list of str): List of command line arguments, if None use
          sys.argv
        stdout (file): Writable stdout stream (sys.stdout if None)
        stderr (file): Writable stderr stream (sys.stderr if None)
 
    Returns:
        None

    """
    if argv is None :
        argv = sys.argv
    if stdout is None :
        stdout = sys.stdout
    if stderr is None :
        stderr = sys.stderr
    parser = _makeParser()
    args = parser.parse_args(argv[1:])
    p = sorted(set(args.prob))
    i = [0] * len(p)
    o = [open(args.output + str(x), "w") for x in p]
    n = 0
    for inputFile in args.input_file :
        with open(inputFile, "r") as fi :
            for l in fi :
                n += 1
                d = random.random()
                for (j, toWrite) in enumerate([d <= x for x in p]) :
                    if toWrite :
                        o[j].write(l)
                        i[j] += 1
    [x.close() for x in o]
    for j in range(len(p)) :
        stderr.write("Prob " + str(p[j]) + ": " + str(i[j]) +
                     " lines kept out of " + str(n) + " input lines " +
                     "(" + str(i[j] * 1. / n) + ")\n")

### ** _makeParser()

def _makeParser() :
    """Build the argument parser for the main script.
    
    Returns:
        argparse.ArgumentParser() object: An argument parser object ready to be
        used to parse the command line arguments

    """
    parser = argparse.ArgumentParser(
        description = SCRIPT_DESCRIPTION)
    # Input files
    parser.add_argument("input_file", nargs = "+", type = str,
                        help = "Input file(s)")
    # Probability
    parser.add_argument("-p", "--prob", nargs = "*", type = float,
                        help = "Probabilities of keeping a line (float between "
                        "0 and 1, default: 1)")
    # Output
    parser.add_argument("-o", "--output", type = str,
                        metavar = "PREFIX", default = "pick",
                        help = "Prefix for output files (default: \"pick\")")
    return parser

### ** __main__

if (__name__ == "__main__") :
    _main()

