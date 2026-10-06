from typing import List, Optional

from pydantic import BaseModel, Field


class UserProfileCreate(BaseModel):
    name: str = Field(..., min_length=2)

    age: int = Field(
        ...,
        ge=1,
        le=120
    )

    income: float = Field(
        ...,
        ge=0
    )

    education: str = Field(
        ...,
        min_length=2
    )

    location: str = Field(
        ...,
        min_length=2
    )

    occupation: str = Field(
        ...,
        min_length=2
    )

    interests: Optional[List[str]] = []


class UserProfileResponse(UserProfileCreate):
    id: int

    class Config:
        from_attributes = True


class SchemeCreate(BaseModel):
    name: str

    category: str

    description: str

    benefits: List[str] = []

    documents: List[str] = []

    deadline: Optional[str] = None

    official_url: str

    source_name: str

    last_verified: Optional[str] = None

    eligibility: dict


class SchemeResponse(SchemeCreate):
    id: int

    class Config:
        from_attributes = True


class RecommendationRequest(BaseModel):
    user_id: int