from helpers.config import get_settings, Settings
import os
import uuid

class BaseController:
    def __init__(self):
        self.app_settings: Settings = get_settings()
        self.base_dir = os.path.dirname( os.path.dirname(__file__) )
        self.files_dir = os.path.join(self.base_dir, "assets/files") 

    def get_unique_string(self, length: int = 12) -> str:
        return uuid.uuid4().hex[:length]