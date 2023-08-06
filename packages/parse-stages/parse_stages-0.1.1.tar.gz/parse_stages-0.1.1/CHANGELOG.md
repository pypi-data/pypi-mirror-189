# Changelog

All notable changes to the parse-stages project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2023-02-05

### Fixes

- Use "precedence" instead of "priority" when discussing operators in
  the README file.
- Do not use the `list` generic type in the definition of the `TaggedFrozen` and
  `Tagged` classes; library consumers may try to use `typing.get_type_hints()` on
  them or on derived classes, and Python < 3.9 would have a problem with that.
- Fill in the module docstring using the text of the README file.
- Fix some problems reported by `ruff`:
    - fix the order of some `import` statements
    - fix the formatting of some docstrings

### Other changes

- Add the `ruff-all` test environment that enables all the checks of the `ruff`
  tool for a certain locked version of `ruff`.
- Add the `tool.test-stages` section in the `pyproject.toml` file to specify
  the order that Tox environments should be run during development using
  the `tox-stages` tool from the `test-stages` Python library.
- Add a lot of `flake8` plugins to the Tox `pep8` test environment
- Use ruff 0.0.241, pylint 2.16.x, and black 23.x.

## [0.1.0] - 2023-01-25

### Started

- First public release.

[Unreleased]: https://gitlab.com/ppentchev/parse-stages/-/compare/release%2F0.1.0...main
[0.1.1]: https://gitlab.com/ppentchev/parse-stages/-/tags/release%2F0.1.1
[0.1.0]: https://gitlab.com/ppentchev/parse-stages/-/tags/release%2F0.1.0
