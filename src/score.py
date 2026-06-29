def calculate_score(missing_headers):
    score = 100 - (missing_headers * 5)

    if score < 0:
        score = 0

    print(f"\nSecurity Score: {score}/100")
    return score
