from enum import Enum

class ResponseSignal(str, Enum):
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"

    FILE_NOT_SUPPORTED = "file_not_supported"
    FILE_TOO_LARGE = "file_too_large"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    FILE_UPLOAD_SUCCESS = "file_upload_success"