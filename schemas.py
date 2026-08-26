from pydantic import BaseModel, ConfigDict, Field


class PostBase(BaseModel):
    title : str = Field(min_length=1, max_length=100)
    content : str = Field(min_length=1)
    author : str = Field(min_length=1, max_length=30)


class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    # this is something that will be returned through api - not sent by client

    model_config = ConfigDict(from_attributes=True)

    id : int
    date_posted : str