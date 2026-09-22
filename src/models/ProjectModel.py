from .BaseDataModel import BaseDataModel
from .db_schemes import Project
from .enums import DataBaseEnum

class ProjectModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client)
        self.db_client = db_client

    @classmethod
    async def create_instance(cls, db_client: object):
        instance = cls(db_client)
        return instance


    async def create_project(self, project: Project) -> str:
        result = await self.collection.insert_one(project.dict(by_alias=True, exclude_unset=True))
        project.project_id = result.inserted_id
        return project

    async def get_project_or_create_one(self, project_id: str) -> Project:
        project = await self.collection.find_one({"project_id": project_id})
        if project is None:
            new_project = Project(project_id=project_id)
            new_project = await self.create_project(new_project)
            return new_project
        return Project(**project)

    async def get_all_projecs(self, page: int = 1, page_size: int = 10):

        # calculate total number of documents
        total_documents = await self.collection.count_documents({})

        # calculate total number of pages
        total_pages = (total_documents + page_size - 1) // page_size

        cursor =self.collection.find().skip((page - 1) * page_size).limit(page_size)
        projects = []

        async for document in cursor:
            projects.append(Project(**document))

        return projects, total_pages