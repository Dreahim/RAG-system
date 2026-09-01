from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import re
from .ProjectController import ProjectController
import os

class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def validate_uploaded_file(self, file: UploadFile) -> (bool, str):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_NOT_SUPPORTED.value
        if file.size > self.app_settings.FILE_MAX_SIZE_MB * 1024 * 1024:
            return False, ResponseSignal.FILE_TOO_LARGE.value
        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value

    def generate_unique_file_name(self, original_file_name: str, project_id: str):
        # Generate a unique key and clean the original file_name
        unique_key = self.get_unique_string()
        cleaned_file_name = self.clean_file_name(original_file_name)

        # Get the project directory path
        project_dir = ProjectController().get_project_path(project_id)

        # Generate a new file path with the unique key and cleaned file_name
        new_file_path = os.path.join(project_dir, f"{unique_key}_{cleaned_file_name}")

        # Ensure the file_name is unique within the project directory
        while os.path.exists(new_file_path):
            unique_key = self.get_unique_string()
            new_file_path = os.path.join(project_dir, f"{unique_key}_{cleaned_file_name}")

        return new_file_path, f"{unique_key}_{cleaned_file_name}"


    def clean_file_name(self, orig_file_name: str) -> str:

        #remove any special characters, except for underscores and .
        cleaned_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        #replace spaces with underscores
        cleaned_name = cleaned_name.replace(' ', '_')

        return cleaned_name