# Gradebook average calculator

def calculate_average(scores):
    if not scores:
        return 0.0
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    else:
        return "F"


def process_students(student_data):
    results = {}
    for name, scores in student_data.items():
        avg = calculate_average(scores)
        results[name] = {
            "average ": avg,
            "grade": get_grade(avg)
        }
    return results


def print_report(results):
    list = sorted(results.keys())
    for name in list:
        data = results[name]
        print(f"{name}: avg={data['average ']:.1f}, grade={data['grade']}")
    print("---")
    averages = [r[" average "] for r in results.values()]
    top = max(averages)
    print(f"Top average: {top:.1f}")
    print(f"Class size: {list(results.keys())}")


students = {
    "Alice": [88, 92, 79, 95],
    "Bob": [72, 68, 74, 70],
    "Carol": [95, 98, 100, 97],
}

report = process_students(students)
print_report(report)