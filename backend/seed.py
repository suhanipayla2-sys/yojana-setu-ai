from database import Base, engine, SessionLocal
from models import Scheme


Base.metadata.create_all(
    bind=engine
)


def seed_schemes():

    db = SessionLocal()

    existing = db.query(Scheme).count()

    if existing > 0:

        print("Schemes already exist.")
        db.close()

        return

    demo_schemes = [

        Scheme(
            name="DEMO Education Support Scheme",
            category="Education",
            description=(
                "Demo scheme record used for testing "
                "the YojanaSetu recommendation engine."
            ),
            benefits=[
                "Education support",
                "Financial assistance"
            ],
            documents=[
                "Identity proof",
                "Income certificate",
                "Education proof"
            ],
            deadline="Verify on official portal",
            official_url="https://www.india.gov.in/",
            source_name="Demo - Verify with official government source",
            last_verified="Development demo",
            eligibility={
                "min_age": 18,
                "max_age": 30,
                "max_income": 500000,
                "education": [
                    "btech",
                    "graduate",
                    "postgraduate"
                ],
                "locations": [
                    "uttar pradesh",
                    "delhi"
                ],
                "interests": [
                    "education",
                    "technology"
                ]
            }
        ),

        Scheme(
            name="DEMO Employment Support Scheme",
            category="Employment",
            description=(
                "Demo scheme record used to test "
                "employment-related recommendation logic."
            ),
            benefits=[
                "Employment support",
                "Skill development"
            ],
            documents=[
                "Identity proof",
                "Address proof",
                "Education proof"
            ],
            deadline="Verify on official portal",
            official_url="https://www.india.gov.in/",
            source_name="Demo - Verify with official government source",
            last_verified="Development demo",
            eligibility={
                "min_age": 18,
                "max_age": 40,
                "max_income": 600000,
                "locations": [
                    "uttar pradesh",
                    "delhi"
                ],
                "occupation": [
                    "student",
                    "job seeker",
                    "unemployed"
                ],
                "interests": [
                    "employment",
                    "skills",
                    "technology"
                ]
            }
        )

    ]

    db.add_all(
        demo_schemes
    )

    db.commit()

    db.close()

    print("Demo schemes added successfully.")


if __name__ == "__main__":
    seed_schemes()