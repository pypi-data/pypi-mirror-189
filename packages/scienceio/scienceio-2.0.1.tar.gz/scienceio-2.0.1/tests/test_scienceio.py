import pytest
import requests_mock
import time
import uuid

from src.scienceio import HTTPError

from .conftest import (
    ERROR_TEST_CASE_IDS,
    ERROR_TEST_CASES,
    MODEL_TEST_CASE_IDS,
    MODEL_TEST_CASES,
    STRUCTURE_INPUT_TEXT,
    exclude_floats,
)


@pytest.mark.parametrize(
    ("input_obj", "error_match"),
    (
        ({}, "str type expected"),
        ({"text": "nested text"}, "str type expected"),
        # (123, "str type expected"),
        ("", "ensure this value has at least 1 characters"),
    ),
    ids=(
        "empty_dict",
        "nested_dict",
        # "number",
        "empty_string",
    ),
)
def test_invalid_input(scio, input_obj, error_match):
    with pytest.raises(HTTPError, match=error_match):
        scio.structure(text=input_obj)


@pytest.mark.parametrize("model_test_case", MODEL_TEST_CASES, ids=MODEL_TEST_CASE_IDS)
def test_autogenerated__process(scio, model_test_case, snapshot):
    func = getattr(scio, model_test_case.model.name.lower())

    assert func.__doc__ == snapshot(name="docstring")

    output = func(text=model_test_case.input_text)

    assert output == snapshot(name="payload", exclude=exclude_floats)


@pytest.mark.parametrize("model_test_case", MODEL_TEST_CASES, ids=MODEL_TEST_CASE_IDS)
def test_autogenerated__submit_and_poll(scio, model_test_case, snapshot):
    submit_func = getattr(scio, f"submit_{model_test_case.model.name.lower()}_request")
    poller_func = getattr(scio, f"poll_{model_test_case.model.name.lower()}_response")

    assert submit_func.__doc__ == snapshot(name="submit_docstring")
    assert poller_func.__doc__ == snapshot(name="poller_docstring")

    request_id = submit_func(text=model_test_case.input_text)

    # The request id would be a valid UUID string.
    assert isinstance(request_id, str)
    uuid.UUID(request_id)

    time.sleep(10)

    output = poller_func(request_id)

    assert isinstance(output, dict)

    assert output == snapshot(name="payload", exclude=exclude_floats)


@pytest.mark.parametrize("error_test_case", ERROR_TEST_CASES, ids=ERROR_TEST_CASE_IDS)
def test_error_cases(scio, snapshot, error_test_case):
    with requests_mock.mock() as m:
        error_test_case.patch_requests_mocker(requests_mocker=m, api_url=scio.api_url)

        with pytest.raises(HTTPError) as exc_info:
            scio.structure(text=STRUCTURE_INPUT_TEXT)

        exc = exc_info.value

        # We want to match on status code AND error payload contents.
        error_info = {
            "status_code": exc.status_code,
            "serialized_exception": str(exc),
        }

        assert error_info == snapshot
