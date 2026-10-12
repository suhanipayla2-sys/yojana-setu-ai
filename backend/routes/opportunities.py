from fastapi import APIRouter, Query, HTTPException

router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)

OPPORTUNITIES = [
    {
        "id": 1,
        "sector": "Government",
        "type": "Scholarship",
        "category": "Scholarship",
        "title": "Government Scholarship Opportunities",
        "icon": "fa-graduation-cap",
        "color": "purple",
        "description": "Explore central and state scholarship programmes for eligible students.",
        "eligibility": "Eligibility, marks, family income and category rules vary by programme.",
        "benefits": ["Education funding opportunities", "Compare programme requirements"],
        "documents": ["Check the specific scheme for marksheets, income certificate and identity documents."],
        "deadline": "Check the latest notice from the scholarship provider.",
        "source": "National Scholarship Portal",
        "url": "https://scholarships.gov.in/",
        "tags": ["Education", "Financial Support"],
        "qualifications": ["10th", "12th", "Diploma", "Undergraduate", "B.Tech", "Graduate", "Postgraduate", "PhD"]
    },
    {
        "id": 2,
        "sector": "Government",
        "type": "Scheme",
        "category": "Healthcare",
        "title": "Government Healthcare Support",
        "icon": "fa-heart-pulse",
        "color": "green",
        "description": "Explore public healthcare services and eligible health-benefit programmes.",
        "eligibility": "Eligibility and benefits depend on the specific healthcare programme.",
        "benefits": ["Find public healthcare information", "Review programme benefits"],
        "documents": ["Check the official portal for required documents."],
        "deadline": "Varies by programme.",
        "source": "Ministry of Health and Family Welfare",
        "url": "https://mohfw.gov.in/",
        "tags": ["Healthcare", "Schemes"],
        "qualifications": []
    },
    {
        "id": 3,
        "sector": "Government",
        "type": "Job",
        "category": "Railways",
        "title": "Railway Recruitment Information",
        "icon": "fa-train",
        "color": "orange",
        "description": "Find official railway recruitment notices and post-wise information.",
        "eligibility": "Age, qualification and selection criteria depend on each recruitment notice.",
        "benefits": ["Explore railway recruitment notices", "Review post-wise eligibility"],
        "documents": ["Follow the original recruitment notice."],
        "deadline": "Check the current recruitment notice.",
        "source": "Indian Railways",
        "url": "https://indianrailways.gov.in/",
        "tags": ["Railways", "Jobs"],
        "qualifications": ["10th", "12th", "Diploma", "Undergraduate", "B.Tech", "Graduate"]
    },
    {
        "id": 4,
        "sector": "Government",
        "type": "Job",
        "category": "Jobs",
        "title": "Government Job Search",
        "icon": "fa-briefcase",
        "color": "blue",
        "description": "Explore job listings and career services through the National Career Service portal.",
        "eligibility": "Every vacancy has its own age, education and selection criteria.",
        "benefits": ["Search job opportunities", "Explore career guidance services"],
        "documents": ["Follow the individual vacancy notice."],
        "deadline": "Varies by vacancy.",
        "source": "National Career Service",
        "url": "https://www.ncs.gov.in/",
        "tags": ["Jobs"],
        "qualifications": ["10th", "12th", "Diploma", "Undergraduate", "B.Tech", "Graduate", "Postgraduate", "PhD"]
    },
    {
        "id": 5,
        "sector": "Government",
        "type": "Internship",
        "category": "Internships",
        "title": "Government Internship Opportunities",
        "icon": "fa-laptop-file",
        "color": "teal",
        "description": "Explore public-sector training and internship notices.",
        "eligibility": "Eligibility and duration depend on the organisation.",
        "benefits": ["Practical learning", "Workplace exposure"],
        "documents": ["Check the relevant official notice."],
        "deadline": "Check the current programme listing.",
        "source": "MyGov",
        "url": "https://www.mygov.in/",
        "tags": ["Internships", "Training"],
        "qualifications": ["Undergraduate", "B.Tech", "Graduate", "Postgraduate", "PhD"]
    },
    {
        "id": 6,
        "sector": "Government",
        "type": "Scheme",
        "category": "Financial Support",
        "title": "Government Financial Assistance",
        "icon": "fa-hand-holding-dollar",
        "color": "green",
        "description": "Explore government assistance and welfare programme information.",
        "eligibility": "Income, category and residence criteria differ by programme.",
        "benefits": ["Find assistance programmes", "Review application instructions"],
        "documents": ["Check each programme's official document checklist."],
        "deadline": "Varies by programme.",
        "source": "National Portal of India",
        "url": "https://www.india.gov.in/",
        "tags": ["Financial Support", "Schemes"],
        "qualifications": []
    },
    {
        "id": 7,
        "sector": "Government",
        "type": "Training",
        "category": "Skills & Startups",
        "title": "Skill Development Opportunities",
        "icon": "fa-certificate",
        "color": "pink",
        "description": "Explore training and skill development options through public programmes.",
        "eligibility": "Entry criteria depend on the particular course and provider.",
        "benefits": ["Skill development", "Career preparation"],
        "documents": ["Check the programme portal for requirements."],
        "deadline": "Check the programme listing.",
        "source": "Skill India Digital",
        "url": "https://www.skillindiadigital.gov.in/",
        "tags": ["Skills & Startups", "Training"],
        "qualifications": ["10th", "12th", "Diploma", "Undergraduate", "B.Tech", "Graduate"]
    },
    {
        "id": 8,
        "sector": "Private",
        "type": "Job",
        "category": "Jobs",
        "title": "Private IT & Software Careers",
        "icon": "fa-laptop-code",
        "color": "blue",
        "description": "Explore private-sector technology roles in development, data, testing and support.",
        "eligibility": "Qualifications and skills depend on the employer and vacancy.",
        "benefits": ["Browse career roles", "Compare requirements"],
        "documents": ["Follow the employer's job listing."],
        "deadline": "Depends on the opening.",
        "source": "Naukri",
        "url": "https://www.naukri.com/",
        "tags": ["Jobs", "Technology"],
        "qualifications": ["Diploma", "Undergraduate", "B.Tech", "Graduate", "Postgraduate"]
    },
    {
        "id": 9,
        "sector": "Private",
        "type": "Job",
        "category": "Healthcare",
        "title": "Private Healthcare Careers",
        "icon": "fa-user-doctor",
        "color": "teal",
        "description": "Explore hospital, diagnostics and healthcare support roles.",
        "eligibility": "Clinical positions may require recognised qualifications or registration.",
        "benefits": ["Explore healthcare careers", "Review role requirements"],
        "documents": ["Check the employer's listing."],
        "deadline": "Depends on the employer and vacancy.",
        "source": "LinkedIn Jobs",
        "url": "https://www.linkedin.com/jobs/",
        "tags": ["Healthcare", "Jobs"],
        "qualifications": ["Diploma", "Undergraduate", "B.Tech", "Graduate", "Postgraduate", "PhD"]
    },
    {
        "id": 10,
        "sector": "Private",
        "type": "Internship",
        "category": "Internships",
        "title": "Private-Sector Internships",
        "icon": "fa-laptop-file",
        "color": "orange",
        "description": "Explore internships in technology, marketing, design, finance and research.",
        "eligibility": "Student status and skills vary by listing.",
        "benefits": ["Practical experience", "Build professional skills"],
        "documents": ["Resume and documents requested by the employer."],
        "deadline": "Check each listing.",
        "source": "Internshala",
        "url": "https://internshala.com/internships/",
        "tags": ["Internships", "Private"],
        "qualifications": ["Undergraduate", "B.Tech", "Graduate", "Postgraduate"]
    },
    {
        "id": 11,
        "sector": "Private",
        "type": "Job",
        "category": "Jobs",
        "title": "Graduate & Fresher Hiring",
        "icon": "fa-user-tie",
        "color": "green",
        "description": "Explore entry-level, graduate trainee and fresher roles.",
        "eligibility": "Degree, graduation year, marks and skills vary by opening.",
        "benefits": ["Explore fresher roles", "Compare requirements"],
        "documents": ["Resume and educational details requested by the employer."],
        "deadline": "Varies by employer.",
        "source": "Naukri Fresher Jobs",
        "url": "https://www.naukri.com/fresher-jobs",
        "tags": ["Jobs", "Freshers"],
        "qualifications": ["Undergraduate", "B.Tech", "Graduate", "Postgraduate"]
    },
    {
        "id": 12,
        "sector": "Private",
        "type": "Scholarship",
        "category": "Scholarship",
        "title": "Private Scholarships & Student Grants",
        "icon": "fa-award",
        "color": "purple",
        "description": "Explore scholarships and grants offered by private trusts and organisations.",
        "eligibility": "Provider criteria may involve marks, course, income and location.",
        "benefits": ["Explore student funding", "Review provider requirements"],
        "documents": ["Follow the specific provider's checklist."],
        "deadline": "Check the provider's current schedule.",
        "source": "Buddy4Study",
        "url": "https://www.buddy4study.com/",
        "tags": ["Scholarship", "Education"],
        "qualifications": ["10th", "12th", "Diploma", "Undergraduate", "B.Tech", "Graduate", "Postgraduate"]
    },
    {
        "id": 13,
        "sector": "Private",
        "type": "Training",
        "category": "Skills & Startups",
        "title": "Private Skill & Certification Programs",
        "icon": "fa-certificate",
        "color": "pink",
        "description": "Explore private training and certification programmes.",
        "eligibility": "Course entry criteria, costs and recognition vary by provider.",
        "benefits": ["Develop skills", "Compare learning options"],
        "documents": ["Check prerequisites and fees with the provider."],
        "deadline": "Check the provider's current page.",
        "source": "Coursera",
        "url": "https://www.coursera.org/",
        "tags": ["Training", "Skills"],
        "qualifications": ["12th", "Diploma", "Undergraduate", "B.Tech", "Graduate", "Postgraduate"]
    },
    {
        "id": 14,
        "sector": "Private",
        "type": "Job",
        "category": "Railways",
        "title": "Private Rail & Transport Careers",
        "icon": "fa-train-subway",
        "color": "orange",
        "description": "Explore private-sector roles in metro, transport, logistics and infrastructure.",
        "eligibility": "Criteria vary by role and employer.",
        "benefits": ["Explore transport careers", "Review job requirements"],
        "documents": ["Follow the employer's vacancy instructions."],
        "deadline": "Depends on the live vacancy.",
        "source": "LinkedIn Jobs",
        "url": "https://www.linkedin.com/jobs/",
        "tags": ["Railways", "Jobs"],
        "qualifications": ["Diploma", "Undergraduate", "B.Tech", "Graduate"]
    }
]


@router.get("/")
def get_opportunities(
    sector: str = Query(default="All"),
    category: str = Query(default=None),
    type: str = Query(default=None)
):
    results = OPPORTUNITIES.copy()

    if sector.lower() != "all":
        results = [
            item for item in results
            if item["sector"].lower() == sector.lower()
        ]

    if category:
        results = [
            item for item in results
            if item["category"].lower() == category.lower()
            or category.lower() in [tag.lower() for tag in item["tags"]]
        ]

    if type:
        results = [
            item for item in results
            if item["type"].lower() == type.lower()
        ]

    return {
        "total": len(results),
        "opportunities": results
    }


@router.get("/{opportunity_id}")
def get_opportunity(opportunity_id: int):
    for item in OPPORTUNITIES:
        if item["id"] == opportunity_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Opportunity not found"
    )