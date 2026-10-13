from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)

# Initial opportunity data for API testing
OPPORTUNITIES = [
    {
        "id": 1,
        "title": "Government Scholarships",
        "sector": "Government",
        "category": "Education",
        "type": "Scholarship",
        "description": "Explore government scholarships available to eligible students.",
        "official_url": "https://scholarships.gov.in/"
    },
    {
        "id": 2,
        "title": "UP Scholarship",
        "sector": "Government",
        "category": "Education",
        "type": "Scholarship",
        "description": "Check Uttar Pradesh scholarship announcements and eligibility.",
        "official_url": "https://scholarship.up.gov.in/"
    },
    {
        "id": 3,
        "title": "NEET UG",
        "sector": "Government",
        "category": "Education",
        "type": "Exam",
        "description": "Check official NEET examination notifications.",
        "official_url": "https://neet.nta.nic.in/"
    },
    {
        "id": 4,
        "title": "SSC Recruitment",
        "sector": "Government",
        "category": "Jobs",
        "type": "Job",
        "description": "Explore Staff Selection Commission recruitment notifications.",
        "official_url": "https://ssc.gov.in/"
    },
    {
        "id": 5,
        "title": "National Career Service",
        "sector": "Private",
        "category": "Jobs",
        "type": "Job",
        "description": "Explore job opportunities and career services.",
        "official_url": "https://www.ncs.gov.in/"
    },
    {
        "id": 6,
        "title": "Internship Opportunities",
        "sector": "Private",
        "category": "Training",
        "type": "Internship",
        "description": "Explore available internships and training opportunities.",
        "official_url": "https://www.ncs.gov.in/"
    }
]


@router.get("/")
def get_opportunities(
    sector: str = Query(default="All"),
    category: str = Query(default="All"),
    search: str = Query(default="")
):
    results = OPPORTUNITIES.copy()

    # Filter by sector
    if sector.strip().lower() != "all":
        results = [
            item for item in results
            if item["sector"].lower() == sector.strip().lower()
        ]

    # Filter by category or opportunity type
    if category.strip().lower() != "all":
        results = [
            item for item in results
            if item["category"].lower() == category.strip().lower()
            or item["type"].lower() == category.strip().lower()
        ]

    # Search by title, description, category, or type
    if search.strip():
        keyword = search.strip().lower()
        results = [
            item for item in results
            if keyword in item["title"].lower()
            or keyword in item["description"].lower()
            or keyword in item["category"].lower()
            or keyword in item["type"].lower()
        ]

    return {
        "total": len(results),
        "opportunities": results
    }