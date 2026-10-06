def check_eligibility(age, income, education, scheme):
    if (scheme["min_age"] <= age and
        income <= scheme["max_income"] and
        (scheme["education"] == education or
         scheme["education"] == "Any")):
        return True

    return False


def find_matches(age, income, education, schemes):
    matched = []

    for scheme in schemes:
        if check_eligibility(age, income, education, scheme):
            matched.append(scheme)

    return matched