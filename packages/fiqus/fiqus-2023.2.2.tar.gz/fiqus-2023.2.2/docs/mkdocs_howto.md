# How to build mkdocs documentation

1. Create `mkdocs.yml` configuration file. This also needs to specify the used docstring style.
2. Create `docs` directory with `index.md` file.
3. Add `mkdocs` and further desired packages to `requirement.txt`. For example, `mkdocstrings` enables the use of auto-documentation of docstrings.
4. Build markdown files generating desired documentation and build navigation in `index.md`. Use `mkdocstring`'s `:::` operator to include docstrings. It seems that an `__init__.py` file is required in all directories used this way. 
5. Call `mkbuild` in parent directory, see `.gitlab-ci.yml`.

## Helpful readings

[CERN ABP computing how to on MkDocs](https://abpcomputing.web.cern.ch/guides/mkdocs_site/)

[IT Guide on documentation in general and Mkdocs](https://how-to.docs.cern.ch/)

[Mkdocstrings](https://mkdocstrings.github.io/)
