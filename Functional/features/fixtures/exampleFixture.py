#Author: Nick Thompson
#This file contains fixtures used in environment.py
#fixtures are setup at the start of and closed at the end of any scenario or feature they are called by
from behave import fixture


@fixture
def test_fixture(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    print("\nSTART OF FIXTURE\n")
    yield 1
    # -- CLEANUP-FIXTURE PART:
    print("\nEND OF FIXTURE\n")
