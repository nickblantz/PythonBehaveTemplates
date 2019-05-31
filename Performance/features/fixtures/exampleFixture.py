from behave import fixture


@fixture
def test_fixture(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    print("\nSTART OF FIXTURE\n")
    yield 1
    # -- CLEANUP-FIXTURE PART:
    print("\nEND OF FIXTURE\n")
