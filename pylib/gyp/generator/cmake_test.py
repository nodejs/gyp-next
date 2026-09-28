#!/usr/bin/env python3

"""Unit tests for the cmake.py file."""

import io
import unittest

from gyp.generator import cmake


class TestCustomCommandComment(unittest.TestCase):
    def test_ActionMessageIsQuotedAndEscaped(self):
        output = io.StringIO()
        action = {
            "action_name": "gen",
            "inputs": ["in.txt"],
            "outputs": ["out.txt"],
            "action": ["python", "gen.py"],
            "message": 'Generating "out.txt"; (see #1)',
        }
        cmake.WriteActions("tgt", [action], [], [], ".", output)
        self.assertIn(
            '  COMMENT "Generating \\"out.txt\\"\\; (see #1)"\n', output.getvalue()
        )

    def test_ActionWithoutMessageUsesTargetName(self):
        output = io.StringIO()
        action = {
            "action_name": "gen",
            "inputs": [],
            "outputs": ["out.txt"],
            "action": ["python", "gen.py"],
        }
        cmake.WriteActions("tgt", [action], [], [], ".", output)
        self.assertIn('  COMMENT "tgt__gen"\n', output.getvalue())

    def test_RuleMessageKeepsVariableReferences(self):
        output = io.StringIO()
        rule = {
            "rule_name": "compile",
            "outputs": ["${RULE_INPUT_ROOT}.o"],
            "action": ["cc", "${RULE_INPUT_PATH}"],
            "rule_sources": ["foo.c"],
            "message": "Compiling ${RULE_INPUT_NAME}",
        }
        cmake.WriteRules("tgt", [rule], [], [], ".", output)
        self.assertIn('  COMMENT "Compiling ${RULE_INPUT_NAME}"\n', output.getvalue())

    def test_CopiesMessageIsQuoted(self):
        output = io.StringIO()
        copies = [{"files": ["a.txt"], "destination": "out"}]
        cmake.WriteCopies("tgt", copies, [], ".", output)
        self.assertIn('COMMENT "Copying for tgt"\n', output.getvalue())


if __name__ == "__main__":
    unittest.main()
