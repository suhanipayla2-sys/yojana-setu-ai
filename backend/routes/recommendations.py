from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import UserProfile, Scheme
from schemas import RecommendationRequest
from services import generate_recommendations


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.post("/")
def get_recommendations(
    request: RecommendationRequest,
    db: Session = Depends(get_db)
):

    user = db.query(
        UserProfile
    ).filter(
        UserProfile.id == request.user_id
    ).first()

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User profile not found"
        )

    schemes = db.query(
        Scheme
    ).all()

    if not schemes:

        return {
            "user_id": user.id,
            "total_schemes": 0,
            "recommendations": []
        }

    recommendations = generate_recommendations(
        user,
        schemes
    )

    return {
        "user_id": user.id,
        "total_schemes": len(recommendations),
        "recommendations": recommendations
    }