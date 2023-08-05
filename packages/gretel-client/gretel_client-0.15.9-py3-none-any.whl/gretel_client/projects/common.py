from enum import Enum
from pathlib import Path
from typing import Iterator, Optional, Union

from smart_open import open

from gretel_client.projects.exceptions import DataSourceError, DataValidationError
from gretel_client.readers import CsvReader, JsonReader

try:
    from pandas import DataFrame as _DataFrameT
except ImportError:
    pd = None

    class _DataFrameT:
        ...  # noqa


Pathlike = Union[str, Path]
DataSourceTypes = Union[str, Path, _DataFrameT]
RefDataTypes = Union[Path, str, _DataFrameT]


def validate_data_source(data_source: Pathlike) -> bool:
    """Validates the input data source. Returns ``True`` if the data
    source is valid, raises an error otherwise.

    A data source is valid if we can open the file and successfully
    parse out JSON or CSV like data.

    Args:
        data_source: The data source to check.

    Raises:
        :class:`~gretel_client.projects.exceptions.DataSourceError` if the
            file can't be opened.
        :class:`~gretel_client.projects.exceptions.DataValidationError` if
            the data isn't valid CSV or JSON.
    """
    try:
        with open(data_source) as ds:
            ds.seek(1)
    except Exception as ex:
        raise DataSourceError(f"Could not open the file '{data_source}'") from ex
    try:
        peek = JsonReader(data_source)
        return _validate_from_reader(peek)
    except Exception:
        pass
    try:
        peek = CsvReader(data_source)
        return _validate_from_reader(peek)
    except Exception:
        pass

    ext = _get_extension(data_source)
    if ext and ext in {".parquet", ".parq"}:
        return True

    raise DataValidationError(
        f"Data validation checks for '{data_source}' failed. "
        "Are you sure the file is valid JSON, CSV or Parquet?"
    )


def _get_extension(data_source: Pathlike) -> Optional[str]:
    try:
        if isinstance(data_source, str):
            return Path(data_source).suffix

        elif isinstance(data_source, Path):
            return data_source.suffix
    except Exception:
        pass

    return None


def _validate_from_reader(peek: Iterator, sample_size: int = 1) -> bool:
    """Perform a set of light-weight checks to ensure that the
    data is valid.

    Raises:
        :class:`~gretel_client.projects.exceptions.DataSourceError` if the
            data source can't be validated.
    """
    # TODO(dn): add additional checks to ensure the data is valid
    sample_set = None
    try:
        sample_set = [next(peek) for _ in range(sample_size)]
        assert sample_set
    except Exception as ex:
        raise DataSourceError(
            "Trying to validate data sample. "
            f"Could not read forward {sample_size} records."
        ) from ex

    return True


MANUAL = "manual"


class ModelArtifact(str, Enum):
    MODEL = "model"
    REPORT = "report"
    REPORT_JSON = "report_json"
    DATA_PREVIEW = "data_preview"
    MODEL_LOGS = "model_logs"


class ModelRunArtifact(str, Enum):
    RUN_REPORT_JSON = "run_report_json"
    DATA = "data"
    RUN_LOGS = "run_logs"
    OUTPUT_FILES = "output_files"


class f:
    """Rest api field constants."""

    DATA = "data"
    URL = "url"
    STATUS = "status"
    ERROR_MSG = "error_msg"
    TRACEBACK = "traceback"
    UID = "uid"
    MODEL_KEY = "model_key"
    WORKER_KEY = "worker_key"
    LOGS = "logs"
    MODEL = "model"
    RUNNER_MODE = "runner_mode"
    CONTAINER_IMAGE = "container_image"
    HANDLER = "handler"
    EMAIL = "email"


YES = "yes"
NO = "no"

WAIT_UNTIL_DONE = -1
