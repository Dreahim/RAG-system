from .BaseDataModel import BaseDataModel
from .db_schemes import DataChunk
from .enums import DataBaseEnum
from bson.objectid import ObjectId
from pymongo import InsertOne

class DataChunkModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client)
        self.db_client = db_client

    @classmethod
    async def create_instance(cls, db_client: object):
        instance = cls(db_client)
        return instance
    
    async def create_data_chunk(self, data_chunk: DataChunk):
        result = await self.collection.insert_one(data_chunk.dict(by_alias=True, exclude_unset=True))
        data_chunk._id = result.inserted_id
        return data_chunk

    async def get_data_chunk(self, chunk_id: str):
        data_chunk = await self.collection.find_one({"_id": ObjectId(chunk_id)})
        if data_chunk is None:
            return None
        return DataChunk(**data_chunk)

    async def insert_many_chunks(self, data_chunks: list, batch_size: int = 100):
        for i in range(0, len(data_chunks), batch_size):
            batch = data_chunks[i:i + batch_size]
            operations = [InsertOne(chunk.dict(by_alias=True, exclude_unset=True)) for chunk in batch]
            await self.collection.bulk_write(operations)

        return len(data_chunks)

    async def delete_chunks_by_project_id(self, project_id: ObjectId):
        result = await self.collection.delete_many({"chunk_project_id": project_id})
        return result.deleted_count

    async def get_project_chunks(self, project_id: ObjectId, page_no: int = 1, page_size: int = 10):
        records = await self.collection.find({
                    "chunk_project_id": project_id,

                }).skip(
                    (page_no-1)*page_size
                ).limit(page_size).to_list(length = None)

        return [
            DataChunk(**rec)
            for rec in records
        ]