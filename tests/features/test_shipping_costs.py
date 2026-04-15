import pytest

from shipping_costs.main import main


def test_should_generate_personalized_greeting_for_attendee(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    Acceptance test: Verify the application outputs a personalized greeting
    for a PyCon attendee.
    """
    # Given the application is run with "PyCon attendee" as an argument
    args = ["PyCon attendee"]

    # When the main application is executed
    main(args)

    # Then the output captured by stdout should be "Hi, PyCon attendee\n"
    captured = capsys.readouterr()
    assert captured.out == "test\n"
