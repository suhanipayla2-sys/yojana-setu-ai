from fastapi import APIRouter

router = APIRouter(
    prefix="/updates",
    tags=["Updates"]
)

GOVERNMENT_UPDATES = [
    {
        "id": 1,
        "title": "Government Scheme Updates",
        "description": "Explore government schemes and verify eligibility.",
        "official_url": "https://www.myscheme.gov.in/",
        "sector": "government"
    },
    {
        "id": 2,
        "title": "Scholarship Updates",
        "description": "Check scholarship announcements and application details.",
        "official_url": "https://scholarships.gov.in/",
        "sector": "government"
    },
    {
        "id": 3,
        "title": "Government Job Updates",
        "description": "Check official recruitment notifications.",
        "official_url": "https://ssc.gov.in/",
        "sector": "government"
    }
]

PRIVATE_UPDATES = [
    {
        "id": 4,
        "title": "Career Opportunities",
        "description": "Explore job opportunities and career services.",
        "official_url": "https://www.ncs.gov.in/",
        "sector": "private"
    },
    {
        "id": 5,
        "title": "Internship Opportunities",
        "description": "Explore internship and training opportunities.",
        "official_url": "https://www.ncs.gov.in/",
        "sector": "private"
    }
]


@router.get("/")
def get_updates():
    return {
        "government": GOVERNMENT_UPDATES,
        "private": PRIVATE_UPDATES,
        "government_updates": GOVERNMENT_UPDATES,
        "private_updates": PRIVATE_UPDATES
    }