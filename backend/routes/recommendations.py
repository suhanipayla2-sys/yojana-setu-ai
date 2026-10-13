from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("/")
def get_recommendations(
    age: int = Query(default=18, ge=0, le=120),
    state: str = Query(default=""),
    occupation: str = Query(default=""),
    annual_income: float = Query(default=0, ge=0),
    category: str = Query(default="All")
):
    recommendations = []

    # Basic demonstration response
    if age <= 25:
        recommendations.append({
            "title": "Government Scholarships",
            "category": "Education",
            "description": "Explore scholarships for eligible students.",
            "official_url": "https://scholarships.gov.in/"
        })

    if occupation.strip().lower() in ["student", "unemployed", "job seeker"]:
        recommendations.append({
            "title": "National Career Service",
            "category": "Jobs",
            "description": "Explore jobs and career services.",
            "official_url": "https://www.ncs.gov.in/"
        })

    if not recommendations:
        recommendations.append({
            "title": "Government Scheme Directory",
            "category": "General",
            "description": "Explore government schemes and verify eligibility on official portals.",
            "official_url": "https://www.myscheme.gov.in/"
        })

    if category.strip().lower() != "all":
        recommendations = [
            item for item in recommendations
            if item["category"].lower() == category.strip().lower()
        ]

    return {
        "total": len(recommendations),
        "profile": {
            "age": age,
            "state": state,
            "occupation": occupation,
            "annual_income": annual_income
        },
        "recommendations": recommendations,
        "disclaimer": "These are preliminary suggestions, not confirmation of eligibility. Verify scheme rules on official portals."
    }