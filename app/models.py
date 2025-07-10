from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, func
from app.database import Base

class HotCommandDB(Base):
    __tablename__ = "hot_commands"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    command_name = Column(String, nullable=False)
    query_text = Column(Text, nullable=False)
    query_type = Column(String, nullable=False)
    domain = Column(String, nullable=True)
    category = Column(String, nullable=True)
    parameters = Column(Text, nullable=True)
    metadata = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

class SpaceDB(Base):
    __tablename__ = "spaces"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    space_name = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    content_type = Column(String, nullable=False)
    is_shared = Column(Boolean, default=False)
    shared_with = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
