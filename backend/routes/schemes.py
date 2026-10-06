from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Scheme
from schemas import (
    SchemeCreate,
    SchemeResponse
)


router = APIRouter(
    prefix="/schemes",
    tags=["Schemes"]
)


@router.post(
    "/",
    response_model=SchemeResponse
)
def create_scheme(
    scheme: SchemeCreate,
    db: Session = Depends(get_db)
):

    new_scheme = Scheme(
        name=scheme.name,
        category=scheme.category,
        description=scheme.description,
        benefits=scheme.benefits,
        documents=scheme.documents,
        deadline=scheme.deadline,
        official_url=scheme.official_url,
        source_name=scheme.source_name,
        last_verified=scheme.last_verified,
        eligibility=scheme.eligibility
    )

    db.add(new_scheme)

    db.commit()

    db.refresh(new_scheme)

    return new_scheme


@router.get(
    "/",
    response_model=list[SchemeResponse]
)
def get_schemes(
    db: Session = Depends(get_db)
):

    schemes = db.query(
        Scheme
    ).all()

    return schemes


@router.get(
    "/{scheme_id}",
    response_model=SchemeResponse
)
def get_scheme(
    scheme_id: int,
    db: Session = Depends(get_db)
):

    scheme = db.query(
        Scheme
    ).filter(
        Scheme.id == scheme_id
    ).first()

    if scheme is None:

        raise HTTPException(
            status_code=404,
            detail="Scheme not found"
        )

    return scheme