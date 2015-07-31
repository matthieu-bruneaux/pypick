Extract random lines from an arbitrarily large input file

Description
===========

Pypick is a simple utility to extract a random subset of lines for a large
input file. It reads the input file line by line and write the output line by
line, so the input file can be arbitrarily large and still be processed (as
long as each line can fit into memory).

It can be particularly useful when trying to estimate the run time and memory
requirements of running another program on the original, large input
file. Small subsets of the original input file of increasing sizes can be used
for benchmarking with the program of interest, and run time and memory
requirements can then be extrapolated to the original input size.

Quick install
-------------
::
   
  pip install --user --upgrade git+https://github.com/matthieu-bruneaux/pypick
  # Check that it worked
  pypick -h

(see *Local install troubleshooting* below if ``pypick`` is not found after
installation).
  
Example usage
-------------

If ``blastp.output`` is a large file with 1e9 lines, subsets can be created
with::

  pypick blastp.output -p 0.0001 0.0004 0.0016 0.0064 -o out.

In this case, four files with randomly selected lines will be created, holding
approximatively 0.01, 0.04, 0.16 and 0.64% of the original file.

Note that the four files represent **nested subsets** of the original file::

  out.0.0001 < out.0.0004 < out.0.0016 < out.0.0064

where ``A < B`` means that all the lines in A are also in B.


Details
-------

The order of lines in the output is the same as in the input (so the program
does not shuffle them, whereas the GNU program ``shuf`` does for example).

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

User install (recommended)
--------------------------

Simply type::

  pip install --user --upgrade git+https://github.com/matthieu-bruneaux/pypick

Test if it worked with::

  pypick -h

You're ready to go!
  
Local install troubleshooting
-----------------------------

The local install with ``pip install --user ...`` will install the executables
in ``~/.local/bin/`` and the Python module in
``~/.local/lib/python2.7/site-packages/``.

To run the executables from the command line, you might need to add
``~/.local/bin/`` to the ``$PATH`` variable in your ``~/.bashrc`` file::

  # Lines to add in your ~/.bashrc file, if needed
  PATH=$PATH:~/.local/bin
  export PATH

System install (with **sudo**)
------------------------------

Type::

  sudo pip install --upgrade git+https://github.com/matthieu-bruneaux/pygenbank

Test if it worked with::

  pypick -h

Related links and projects
==========================

This `post on stackoverflow
<http://stackoverflow.com/questions/692312/randomly-pick-lines-from-a-file-without-slurping-it-with-unix>`_
has one-liners to do the same with ``awk`` or ``perl``. However, ``pypick``
might be more useful when several output files of different sizes have to be
generated since it can do so in only one pass over the input file.

A similar and more advanced project for picking up random elements from a list
is `pypicker <https://github.com/JasonBristol/pypicker>`_ from Jason
Bristol. There are probably more out there, the previous one was found by
searching for `pypick` on GitHub.


