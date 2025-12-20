from sqlmodel import Field, SQLModel

class Posts(SQLModel, table=True):
	id: int = Field(primary_key=True, nullable=False)
	title: str = Field(nullable=False)
	content: str = Field(nullable=False)
	published: bool = Field(default=False, sa_column_kwargs={"server_default": "false"}, nullable=False)