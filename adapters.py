import json
import os
import sys
from io import StringIO
from chatterbot.logic import LogicAdapter
from pylint.reporters.json import JSONReporter
from chatterbot.conversation import Statement
from pylint import lint


class WritableObject(object):
    """Dummy output stream for pylint"""

    def __init__(self):
        self._content = []

    def write(self, txt):
        self._content.append(txt)

    def read(self):
        return self._content


class NullIO(StringIO):
    def write(self, txt):
        pass


def silent(fn):
    """Decorator to silence functions."""

    def silent_fn(*args, **kwargs):
        saved_stderr = sys.stderr
        sys.stderr = NullIO()
        result = fn(*args, **kwargs)
        sys.stderr = saved_stderr
        return result

    return silent_fn


run_pylint = silent(lint.Run)


class PylintAdapter(LogicAdapter):
    rcfilename = 'pylintrc'

    def __init__(self, **kwargs):
        self._filepath = 'chatbot.py'
        super().__init__(**kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement):
        confidence = 1

        pylint_output = self._run_pylint()

        selected_statement = Statement(pylint_output[0]['message'])
        selected_statement.confidence = confidence

        return selected_statement

    def _run_pylint(self):
        if not os.path.isfile(self.rcfilename):
            self._create_rcfile()

        args = ["-r", "y", "--rcfile=pylintrc"]
        pylint_output = WritableObject()
        run_pylint([self._filepath] + args, reporter=JSONReporter(pylint_output), exit=False)

        json_str = ''.join(pylint_output.read())

        return json.loads(json_str)

    def _create_rcfile(self):
        with open(self.rcfilename, 'w') as rcfile:
            rcfile.write('')
