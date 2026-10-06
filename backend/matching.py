def check_eligibility(user, scheme):
    eligibility = scheme.eligibility or {}

    reasons = []
    matched_conditions = []
    missing_conditions = []

    total_conditions = 0
    matched_count = 0

    # -------------------------
    # AGE CHECK
    # -------------------------

    if "min_age" in eligibility:
        total_conditions += 1

        if user.age >= eligibility["min_age"]:
            matched_count += 1

            matched_conditions.append(
                f"Age requirement satisfied: minimum age is "
                f"{eligibility['min_age']}."
            )
        else:
            missing_conditions.append(
                f"Minimum age required is "
                f"{eligibility['min_age']} years."
            )

    if "max_age" in eligibility:
        total_conditions += 1

        if user.age <= eligibility["max_age"]:
            matched_count += 1

            matched_conditions.append(
                f"Age requirement satisfied: maximum age is "
                f"{eligibility['max_age']}."
            )
        else:
            missing_conditions.append(
                f"Maximum age allowed is "
                f"{eligibility['max_age']} years."
            )

    # -------------------------
    # INCOME CHECK
    # -------------------------

    if "max_income" in eligibility:
        total_conditions += 1

        if user.income <= eligibility["max_income"]:
            matched_count += 1

            matched_conditions.append(
                f"Income requirement satisfied. "
                f"Maximum allowed income is ₹{eligibility['max_income']}."
            )
        else:
            missing_conditions.append(
                f"Income must be less than or equal to "
                f"₹{eligibility['max_income']}."
            )

    # -------------------------
    # LOCATION CHECK
    # -------------------------

    if "locations" in eligibility:

        total_conditions += 1

        allowed_locations = [
            location.lower()
            for location in eligibility["locations"]
        ]

        if user.location.lower() in allowed_locations:
            matched_count += 1

            matched_conditions.append(
                f"Location requirement satisfied for "
                f"{user.location}."
            )
        else:
            missing_conditions.append(
                "This scheme is not recorded as available "
                f"for {user.location}."
            )

    # -------------------------
    # EDUCATION CHECK
    # -------------------------

    if "education" in eligibility:

        total_conditions += 1

        required_education = [
            value.lower()
            for value in eligibility["education"]
        ]

        if user.education.lower() in required_education:
            matched_count += 1

            matched_conditions.append(
                "Education requirement appears to be satisfied."
            )
        else:
            missing_conditions.append(
                "The required education level may not match "
                "the user's profile."
            )

    # -------------------------
    # OCCUPATION CHECK
    # -------------------------

    if "occupation" in eligibility:

        total_conditions += 1

        required_occupations = [
            value.lower()
            for value in eligibility["occupation"]
        ]

        if user.occupation.lower() in required_occupations:
            matched_count += 1

            matched_conditions.append(
                "Occupation requirement appears to be satisfied."
            )
        else:
            missing_conditions.append(
                "The user's occupation may not match "
                "the recorded scheme requirement."
            )

    # -------------------------
    # INTEREST CHECK
    # -------------------------

    if "interests" in eligibility:

        required_interests = [
            value.lower()
            for value in eligibility["interests"]
        ]

        user_interests = [
            value.lower()
            for value in (user.interests or [])
        ]

        common_interests = set(required_interests).intersection(
            set(user_interests)
        )

        if common_interests:
            matched_conditions.append(
                "User interests are related to the scheme."
            )

    # -------------------------
    # MATCH SCORE
    # -------------------------

    if total_conditions > 0:
        match_percentage = round(
            (matched_count / total_conditions) * 100
        )
    else:
        match_percentage = 0

    # We call this "eligible" only when all recorded
    # deterministic conditions are satisfied.
    eligible = (
        total_conditions > 0
        and matched_count == total_conditions
    )

    return {
        "scheme_id": scheme.id,
        "scheme_name": scheme.name,
        "category": scheme.category,
        "eligible": eligible,
        "match_percentage": match_percentage,
        "matched_conditions": matched_conditions,
        "missing_conditions": missing_conditions,
        "benefits": scheme.benefits or [],
        "documents": scheme.documents or [],
        "deadline": scheme.deadline,
        "official_url": scheme.official_url,
        "source_name": scheme.source_name,
        "last_verified": scheme.last_verified
    }


def find_matching_schemes(user, schemes):

    results = []

    for scheme in schemes:

        result = check_eligibility(
            user,
            scheme
        )

        results.append(result)

    results.sort(
        key=lambda item: item["match_percentage"],
        reverse=True
    )

    return results