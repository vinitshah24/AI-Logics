from logic import *

# ^ AND &
# v OR |
# => Implies >>
# <=> Iff P.iff(Q)
# ~ Negation ~

P,Q,R = vars('P', 'Q', 'R')       

formula = (P.iff(Q)) >> (~P >> ~Q) 
print(f"Formula {formula}")
is_tautology = formula.is_tautology()
print(f"Is Tautalogy: {is_tautology}")
print("Truth Table:")
formula.print_truth_table()

formula_1 = (P & Q) >> R 
formula_2 = P >> (Q >> R)
is_similar = formula_1 == formula_2
print(f"Formula 1: {formula_1}")
print(f"Formula 2: {formula_2}")
print(f"Are both the formulas similar: {is_similar}")

is_contradiction = (P & ~P).is_contingency()
print(f"Check contradiction (P & ~P): {is_contradiction}\n")

print(f"Formula {formula_1}")
# Contingency - if truth table contains at least one T and at least one F
print(f"Check contigency {formula_1.is_contingency()}")
print("Truth table:")
formula_1.print_truth_table()