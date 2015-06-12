Description
===========

Pypick is a simple utility to extract a random subset of lines for a large
input file. It reads the input file line by line and write the output line by
line, so the input file can be **arbitrarily large** and still be processed (as
long as each line can fit into memory).

It can be particularly useful when trying to **estimate the run time and memory
requirements** of running another program on the input file, by benchmarking
the other program on small subsets of the input file of incresing sizes.

Details
-------

The order of lines in the output is the same as in the input (so the program
does not shuffle them, whereas the GNU program `shuf` does for example).

The number of lines to be written to the output is defined by a probability
value. Using a probability of 0.1 will result in an output file with
approximatively 10% of the input lines, taken randomly along the input file.

Several probability values can be given at the command line, resulting in
several output files in one pass over the input file. Note that in this case
output files are nested subsets, i.e. lines from an output file corresponding
to a given probability value are all included in any output file from the same
call with higher probablity values.

Installation
============

Local install (no sudo needed)
------------------------------

Simply type::

  pip install --user --upgrade git+https://github.com/matthieu-bruneaux/pypick

Test if it worked with::

  pypick -h

(see below if this does not work).

Global install (with sudo, not recommended)
-------------------------------------------

Type::

  sudo pip install --upgrade git+https://github.com/matthieu-bruneaux/pygenbank

Test if it worked with::

  pypick -h

Issues with local install
-------------------------

The local install with ``pip install --user ...`` will install the executables
in ``~/.local/bin/`` and the Python module in
``~/.local/lib/python2.7/site-packages/``.

To run the executables from the command line, you might need to add
``~/.local/bin/`` to the ``$PATH`` variable in your ``~/.bashrc`` file::

  # Lines to add in your ~/.bashrc file, if needed
  PATH=$PATH:~/.local/bin
  export PATH
  
Similar projects
================

A similar and more advanced project is
`pypicker<https://github.com/JasonBristol/pypicker>`_ from Jason Bristol. There
are probably more out there, I found the previous one by searching for `pypick`
on GitHub.

