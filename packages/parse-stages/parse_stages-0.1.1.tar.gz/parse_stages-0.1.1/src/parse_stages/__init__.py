# Copyright (c) Peter Pentchev <roam@ringlet.net>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
"""Parse a mini-language for selecting objects by tag or name.

This library is mostly useful for command-line parsing by other tools like
`tox-stages` and `nox-stages`. It may be used to parse e.g. a command-line
specification like `@check and not pylint` or `@tests or ruff` and then
match it against a list of objects that have names and lists of tags.

Parse stage specifications
--------------------------
The `parse_spec()` function parses a string specification into
a `BoolExpr` object that may later be used to select matching objects
(e.g. test environments).

The specification mini-language may roughly be described as:

    expr ::= and_expr ["or" and_expr...]
    and_expr ::= not_expr ["and" not_expr...]
    not_expr ::= ["not"] atom
    atom ::= tag | keyword
    tag ::= "@" characters
    keyword ::= characters
    characters ::= [A-Za-z0-9_-]+

Thus, all of the following:

- `@check`
- `@check and @quick`
- `@tests and not examples`
- `not @tests`
- `pep8 or not @quick and @check`

...are valid expressions,
with the "not", "and", and "or" keywords having their usual precedence
(`pep8 or not @quick and @check` is parsed as
`pep8 or ((@not quick) and @check)`, but the mini-language does not
support parentheses yet).

Check whether an object matches a parsed specification
------------------------------------------------------
The `parse-stages` library provides two base dataclasses for objects that
may be matched against parsed expressions: `TaggedFrozen` and `Tagged`.
Both classes have the same members:

- `name`: a string
- `tags`: a list of strings
- `get_keyword_haystacks()`: a method that returns a list of strings,
  `[self.name]` unless overridden

When a `BoolExpr` object's `evaluate()` method is called for a specific
`TaggedFrozen` or `Tagged` object, it checks whether the specification
matches the tags and keywords defined for this object. Tags are matched
exactly, while a keyword is considered to match if it is contained in
the checked string; e.g. `pep` would match both `pep8` and `exp_pep563`,
while `@black` would not match a `black-reformat` tag.

The `get_keyword_haystacks()` method returns the strings to look in for
matching keywords. By default, it only returns the `name` field;
however, it may be extended, e.g. for Nox sessions it may also return
the name of the Python function that implements the session, for test
classes with methods it may return the class name and the method name, etc.

Examples
--------
Parse a list of stage specifications into expressions that may later be
matched against test environment definitions:

    e_check = parse_stages.parse_spec("@check")
    e_check_quick = parse_stages.parse_spec("@check and @quick")
    e_check_no_ruff = parse_stages.parse_spec("@check and not ruff")

    specs = [(spec, parse_stages.parse_spec(spec)) for spec in args.stage_specs]

Select the test environments that match the specification:

    # Obtain a list (okay, a dictionary) of test environments in some way
    tox_envs = get_tox_environments()  # {"ruff": {"tags": ["check", "quick"]}, ...}

    # Convert them to objects that the parsed expressions can match
    all_envs = [
        parse_stages.TaggedFrozen(name, env["tags"])
        for name, env in tox_envs.items()
    ]

    # Or define our own class that may hold additional information
    @dataclasses.dataclass(frozen=True)
    class TestEnv(parse_stages.TaggedFrozen):
        ...

    all_envs = [TestEnv(name, env["tags"], ...) for name, env in tox_envs.items()]

    # Select the ones that match the "@check" expression
    matched = [env for env in all_envs if e_check.evaluate(env)]

    # Or if we only care about the names...
    quick_names = [env.name for env in all_envs if e_check_quick.evaluate(env)]
"""

from .defs import Tagged, TaggedFrozen, VERSION
from .expr import BoolExpr, OrExpr, AndExpr, NotExpr, TagExpr, KeywordExpr
from .p_pyp import parse_spec, parse_stage_ids


__all__ = [
    "Tagged",
    "TaggedFrozen",
    "BoolExpr",
    "OrExpr",
    "AndExpr",
    "NotExpr",
    "TagExpr",
    "KeywordExpr",
    "parse_spec",
    "parse_stage_ids",
    "VERSION",
]
