from enum import Enum

class ResponseSignal(Enum):
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"

    FILE_NOT_SUPPORTED = "file_not_supported"
    FILE_TOO_LARGE = "file_too_large"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    FILE_UPLOAD_SUCCESS = "file_upload_success"

    FILE_PROCESSING_FAILED = "file_processing_failed"
    FILE_PROCESSING_SUCCESS = "file_processing_success"
    FILE_NO_FILES_ERROR = "not_found_files"
    FILE_ID_ERROR = "no_file_found_with_this_id"
    PROJECT_NOT_FOUND_ERROR = "project_not_found_error"
    INSERT_INTO_VECTORDB_ERROR = "insert_into_vectordb_error"
    INSERT_INTO_VECTORDB_SUCCESS = "insert_into_vectordb_success"
    VECTORDB_COLLECTION_RETRIEVED = "vectordb_collection_retrieved"
    VECTORDB_SEARCH_ERROR = "vectordb_search_error"
    VECTORDB_SEARCH_SUCESS = "vectordb_search_success"
    