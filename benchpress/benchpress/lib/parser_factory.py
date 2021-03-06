#!/usr/bin/env python3
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

from benchpress.lib.factory import BaseFactory
from benchpress.lib.parser import Parser
from benchpress.plugins.parsers import register_parsers


ParserFactory = BaseFactory(Parser)

# register third-party parsers with the factory
register_parsers(ParserFactory)
