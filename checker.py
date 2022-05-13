import json

TESTS = 13
passed_tests = 0

with open("Stats.json") as stats_file:
    stats = json.load(stats_file)

stats_check = {
    "graduating": 193,
    "graduation_rate": 0.8212765957446808,
    "maui_waena_incoming": 41,
    "lokelani_incoming": 63,
    "freshmen": 135,
    "sophomores": 245,
    "juniors": 231,
    "seniors": 249
}

print("Checking stats...")
if stats["graduating"] == stats_check["graduating"]:
    print("graduating:           PASS")
    passed_tests += 1
else:
    print("graduating:           FAIL")
    print("\tYou have the wrong number of students graduating.")
if abs(stats["graduation_rate"] - stats_check["graduation_rate"]) < .01:
    print("graduation_rate:      PASS")
    passed_tests += 1
else:
    print("graduation_rate:      FAIL")
    print("\tYour graduation_rate is incorrect.")
if stats["maui_waena_incoming"] == stats_check["maui_waena_incoming"]:
    print("maui_waena_incoming:  PASS")
    passed_tests += 1
else:
    print("maui_waena_incoming:  FAIL")
    print("\tYou have the wrong number of maui_waena_incoming students.")
if stats["lokelani_incoming"] == stats_check["lokelani_incoming"]:
    print("lokelani_incoming:    PASS")
    passed_tests += 1
else:
    print("lokelani_incoming:    FAIL")
    print("\tYou have the wrong number of lokelani_incoming students.")
if stats["freshmen"] == stats_check["freshmen"]:
    print("freshmen:             PASS")
    passed_tests += 1
else:
    print("freshmen:             FAIL")
    print("\tYou have the wrong number of freshmen.")
if stats["sophomores"] == stats_check["sophomores"]:
    print("sophomores:           PASS")
    passed_tests += 1
else:
    print("sophomores:           FAIL")
    print("\tYou have the wrong number of sophomores.")
if stats["juniors"] == stats_check["juniors"]:
    print("juniors:              PASS")
    passed_tests += 1
else:
    print("juniors:              FAIL")
    print("\tYou have the wrong number of juniors.")
if stats["seniors"] == stats_check["seniors"]:
    print("seniors:              PASS")
    passed_tests += 1
else:
    print("seniors:              FAIL")
    print("\tYou have the wrong number of seniors.")

maui_high_updated = []
with open("MauiHighUpdated.csv") as maui_high_updated_file:
    for student in maui_high_updated_file:
        student = student.split(",")
        student[-1] = student[-1].strip()
        maui_high_updated.append(student)

maui_high_updated_checker = []
with open("MauiHighUpdatedChecker.csv") as maui_high_updated_checker_file:
    for student in maui_high_updated_checker_file:
        student = student.split(",")
        student[-1] = student[-1].strip()
        maui_high_updated_checker.append(student)

print()
print("Checking updated CSV file...")

if len(maui_high_updated) != len(maui_high_updated_checker):
    print("You do not have the correct amount of students in your MauiHighUpdated.csv file.")
    for student in maui_high_updated:
        if student[4] == "True":
            print("It looks like you have an issue with your transfer students.")
            break
    print("You are currently failing all 5 of the CSV tests.")
else:
    name_match = True
    for i in range(len(maui_high_updated)):
        if maui_high_updated[i][0] != maui_high_updated_checker[i][0]:
            name_match = False
            break
    if name_match:
        print("PASS: You have all of the correct students in your MauiHighUpdated.csv file.")
        passed_tests += 1
    else:
        print("FAIL: You do NOT have the correct students in your MauiHighUpdated.csv file.")
    grade_match = True
    for i in range(len(maui_high_updated)):
        if maui_high_updated[i][1] != maui_high_updated_checker[i][1]:
            grade_match = False
            break
    if grade_match:
        print("PASS: Your students all have the correct grade in your MauiHighUpdated.csv file.")
        passed_tests += 1
    else:
        print("FAIL: Your students do NOT all have the correct grade in your MauiHighUpdated.csv file.")
    graduation_requirements_match = True
    for i in range(len(maui_high_updated)):
        if maui_high_updated[i][2] != maui_high_updated_checker[i][2]:
            graduation_requirements_match = False
            break
    if graduation_requirements_match:
        print("PASS: Your graduation_requirements column is correct for all students.")
        passed_tests += 1
    else:
        print("FAIL: Your graduation_requirements column is NOT correct for all students.")
    credits_match = True
    for i in range(len(maui_high_updated)):
        if maui_high_updated[i][3] != maui_high_updated_checker[i][3]:
            credits_match = False
            break
    if credits_match:
        print("PASS: All students have the correct number of credits.")
        passed_tests += 1
    else:
        print("FAIL: NOT all students have the correct number of credits.")
    transferring_match = True
    for i in range(len(maui_high_updated)):
        if maui_high_updated[i][4] != maui_high_updated_checker[i][4]:
            transferring_match = False
            break
    if transferring_match:
        print("PASS: Your transferring column is correct for all students.")
        passed_tests += 1
    else:
        print("FAIL: Your transferring column is NOT correct for all students.")

print()
print("You are currently passing " + str(passed_tests) + " out of " + str(TESTS) + " tests.")