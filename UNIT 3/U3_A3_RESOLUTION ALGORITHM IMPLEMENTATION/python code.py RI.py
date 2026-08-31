# ============================================================
# RESOLUTION ALGORITHM
# Implementation of 5 Propositional Logic Problems
# ============================================================

def resolve(clause1, clause2):
    """
    Apply the resolution rule to two clauses.
    Returns a set containing the resolvent(s).
    """
    resolvents = set()

    for literal in clause1:
        # Find the complementary literal in clause2
        if literal.startswith("~"):
            complementary = literal[1:]
        else:
            complementary = "~" + literal

        if complementary in clause2:
            new_clause = (clause1 - {literal}) | (clause2 - {complementary})
            resolvents.add(frozenset(new_clause))

    return resolvents


def resolution(clauses, goal):
    """
    Prove the goal using resolution by contradiction.
    The negation of the goal is added to the clauses.
    """

    # Add negated goal
    clauses = set(frozenset(clause) for clause in clauses)

    if goal.startswith("~"):
        negated_goal = goal[1:]
    else:
        negated_goal = "~" + goal

    clauses.add(frozenset([negated_goal]))

    print("\nInitial Clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"C{i}: {format_clause(clause)}")

    new = set()

    while True:
        clause_list = list(clauses)

        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):

                resolvents = resolve(clause_list[i], clause_list[j])

                for resolvent in resolvents:

                    print(
                        f"Resolve ({format_clause(clause_list[i])}) "
                        f"and ({format_clause(clause_list[j])}) "
                        f"-> {format_clause(resolvent)}"
                    )

                    # Empty clause found
                    if len(resolvent) == 0:
                        print("Result: Empty Clause (□) obtained.")
                        print("Therefore, the goal is PROVED.")
                        return True

                    new.add(resolvent)

        # If no new clauses can be generated
        if new.issubset(clauses):
            print("No new clauses can be generated.")
            print("Therefore, the goal cannot be proved.")
            return False

        clauses.update(new)
        new.clear()


def format_clause(clause):
    """Format a clause for readable output."""

    if len(clause) == 0:
        return "□"

    return " ∨ ".join(sorted(clause))


# ============================================================
# QUESTION 1
# RAIN AND WET GROUND
# ============================================================

print("=" * 70)
print("QUESTION 1: RAIN AND WET GROUND")
print("=" * 70)

print("Goal: Ground is wet")

clauses_q1 = [
    {"~R", "W"},   # R -> W
    {"R"}          # It is raining
]

resolution(clauses_q1, "W")


# ============================================================
# QUESTION 2
# STUDENT ASSIGNMENT SUBMISSION
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 2: STUDENT ASSIGNMENT SUBMISSION")
print("=" * 70)

print("Goal: Rahul receives internal marks")

clauses_q2 = [
    {"~S", "M"},   # S -> M
    {"S"}          # Rahul submitted assignment
]

resolution(clauses_q2, "M")


# ============================================================
# QUESTION 3
# LIBRARY MEMBERSHIP
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 3: LIBRARY MEMBERSHIP")
print("=" * 70)

print("Goal: Priya can borrow books")

clauses_q3 = [
    {"~L", "B"},   # L -> B
    {"L"}          # Priya is a library member
]

resolution(clauses_q3, "B")


# ============================================================
# QUESTION 4
# PLACEMENT ELIGIBILITY
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 4: PLACEMENT ELIGIBILITY")
print("=" * 70)

print("Goal: Arun is eligible for placement")

clauses_q4 = [
    {"~A", "P"},   # A -> P
    {"A"}          # Arun cleared aptitude test
]

resolution(clauses_q4, "P")


# ============================================================
# QUESTION 5
# ACCESS CONTROL SYSTEM
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 5: ACCESS CONTROL SYSTEM")
print("=" * 70)

print("Goal: User is granted access")

clauses_q5 = [
    {"~C", "A"},   # C -> A
    {"~A", "G"},   # A -> G
    {"C"}          # Correct password entered
]

resolution(clauses_q5, "G")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print("Q1 - Ground is wet                         : PROVED")
print("Q2 - Rahul receives internal marks         : PROVED")
print("Q3 - Priya can borrow books                : PROVED")
print("Q4 - Arun is eligible for placement        : PROVED")
print("Q5 - User is granted access                : PROVED")
print("=" * 70)
