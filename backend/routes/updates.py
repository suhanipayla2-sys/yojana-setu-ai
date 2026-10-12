from fastapi import APIRouter

router = APIRouter(
    prefix="/updates",
    tags=["Latest Updates"]
)

# Sample Government Updates
GOVERNMENT_UPDATES = [
    {
        "id": 1,
        "title": "National Scholarship Portal",
        "text": "Students can check available scholarship schemes.",
        "source": "National Scholarship Portal",
        "url": "https://scholarships.gov.in/",
        "published_at": None,
        "deadline": None,
        "is_extension": False
    },
    {
        "id": 2,
        "title": "National Career Service",
        "text": "Explore government employment opportunities.",
        "source": "National Career Service",
        "url": "https://www.ncs.gov.in/",
        "published_at": None,
        "deadline": None,
        "is_extension": False
    }
]

# Sample Private Updates
PRIVATE_UPDATES = [
    {
        "id": 3,
        "title": "Private Job Opportunities",
        "text": "Explore private-sector career opportunities.",
        "source": "National Career Service",
        "url": "https://www.ncs.gov.in/",
        "published_at": None,
        "deadline": None,
        "is_extension": False
    },
    {
        "id": 4,
        "title": "Skill Development Opportunities",
        "text": "Explore training and skill development opportunities.",
        "source": "Skill India Digital",
        "url": "https://www.skillindiadigital.gov.in/",
        "published_at": None,
        "deadline": None,
        "is_extension": False
    }
]


@router.get("/")
def get_updates():
    return {
        "government": GOVERNMENT_UPDATES,
        "private": PRIVATE_UPDATES
    }