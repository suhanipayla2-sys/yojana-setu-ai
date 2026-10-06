from sqlalchemy import Column, Integer, String, Float, Text, JSON

from database import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    age = Column(Integer, nullable=False)

    income = Column(Float, nullable=False)

    education = Column(String(100), nullable=False)

    location = Column(String(100), nullable=False)

    occupation = Column(String(100), nullable=False)

    interests = Column(JSON, nullable=True)


class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(200), nullable=False)

    category = Column(String(100), nullable=False)

    description = Column(Text, nullable=False)

    benefits = Column(JSON, nullable=True)

    documents = Column(JSON, nullable=True)

    deadline = Column(String(100), nullable=True)

    official_url = Column(String(500), nullable=False)

    source_name = Column(String(200), nullable=False)

    last_verified = Column(String(100), nullable=True)

    eligibility = Column(JSON, nullable=False)