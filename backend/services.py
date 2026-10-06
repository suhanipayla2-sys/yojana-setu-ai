from matching import find_matching_schemes


def generate_recommendations(user, schemes):
    results = find_matching_schemes(user, schemes)
    return results