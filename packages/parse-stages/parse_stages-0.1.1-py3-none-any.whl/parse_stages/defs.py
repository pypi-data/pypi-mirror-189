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
"""Common definitions for the parse-stages library."""

# Some of this library's consumers need to be able to use typedload on
# Python versions < 3.9, so we cannot use the generic types.
# pylint: disable=deprecated-typing-alias

import dataclasses

from typing import List


@dataclasses.dataclass(frozen=True)
class TaggedFrozen:
    """A base class for representing a constant object that has some tags."""

    name: str
    tags: List[str]

    def get_keyword_haystacks(self) -> List[str]:
        """Get the strings to look for keywords in.

        Default: the object's `name` attribute.
        """
        return [self.name]


@dataclasses.dataclass
class Tagged:
    """A base class for representing an object that has some tags."""

    name: str
    tags: List[str]

    def get_keyword_haystacks(self) -> List[str]:
        """Get the strings to look for keywords in.

        Default: the object's `name` attribute.
        """
        return [self.name]


VERSION = "0.1.1"
