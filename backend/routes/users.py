from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import UserProfile
from schemas import (
    UserProfileCreate,
    UserProfileResponse
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/profile",
    response_model=UserProfileResponse
)
def create_profile(
    profile: UserProfileCreate,
    db: Session = Depends(get_db)
):

    new_profile = UserProfile(
        name=profile.name,
        age=profile.age,
        income=profile.income,
        education=profile.education,
        location=profile.location,
        occupation=profile.occupation,
        interests=profile.interests
    )

    db.add(new_profile)

    db.commit()

    db.refresh(new_profile)

    return new_profile


@router.get(
    "/profile/{user_id}",
    response_model=UserProfileResponse
)
def get_profile(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(
        UserProfile
    ).filter(
        UserProfile.id == user_id
    ).first()

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User profile not found"
        )

    return user