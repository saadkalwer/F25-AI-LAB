# AI Lab 1 - Saad Ahmed (009)

def rule_based(score, documents_complete, attendance, clear_record):
    reasons = []
    if score < 70:
        reasons.append("Score is below 70")
    if documents_complete == False:
        reasons.append("Documents are incomplete")
    if attendance < 75:
        reasons.append("Attendance is below 75%")
    if clear_record == False:
        reasons.append("Disciplinary record is not clear")

    if len(reasons) == 0:
        return "Review", "All conditions are passed"
    return "Hold", ", ".join(reasons)

def probability_based(probability):
    if probability >= 0.70:
        return "Review"
    return "Hold"

test_cases = [
    ("Pass case", 82, True, 90, True, "Review"),
    ("Attendance failure", 82, True, 74, True, "Hold"),
    ("Record failure", 82, True, 90, False, "Hold"),
    ("Boundary case", 70, True, 75, True, "Review")
]

print("LAB 1: RULE-BASED SCHOLARSHIP CHECKER")
for name, score, documents, attendance, record, expected in test_cases:
    result, reason = rule_based(score, documents, attendance, record)
    print("\nCase:", name)
    print("Expected:", expected)
    print("Actual:", result)
    print("Reason:", reason)

print("\nSYMBOLIC AND PROBABILITY COMPARISON")
comparison_cases = [
    (82, True, 0.81),
    (68, True, 0.74),
    (91, False, 0.88),
    (70, True, 0.70)
]
for score, complete, probability in comparison_cases:
    symbolic = "Review" if complete and score >= 70 else "Hold"
    probability_result = probability_based(probability)
    print(score, complete, probability, "->", symbolic, "/", probability_result)
