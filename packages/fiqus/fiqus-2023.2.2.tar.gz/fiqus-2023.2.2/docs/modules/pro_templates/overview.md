# Overview of .pro templates of FiQuS

The templating of .pro templates is based on python's jinja2 library.

The python code using this library is in the pro_assemblers folder.

Two types of templates are foreseen in FiQuS:
1. Combined - a single .pro template file that covers all objects needed by GetDP.
2. Separated - many .pro template files distributed across folders corresponding to objects in GetDP.

Only combined templates are implemented so far in FiQuS as this is a good starting point for understanding what would be needed for separated template files.