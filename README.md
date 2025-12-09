# GitHub-Python-Module
Final Assignment for the Python for Networking course.

This project is the culmination of my work in the Python for Networking course at Mohawk College. The goal was to create a module/package that can be imported into a user's system and access the HOSTS file. A command line interface is presented to the user so they can block a FQDN by updating the HOSTS table entry with the FQDN and sending it to a DNS blackhole (0.0.0.0). 

THe module is designed to function on any operating system, and incorporates error handling, File I/O, imported modules and command line arguments. If a user wants to use this module, they will need to have the following 3rd party modules imported in their python environment:

sys, os, platform, re, argparse, and from setuptools, setup and find_packages.



