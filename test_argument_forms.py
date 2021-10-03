from logic import *

P, Q, R, S = vars('P', 'Q', 'R', 'S')

# valid argument forms
modus_ponens = ArgumentForm(
    P,
    P >> Q,
    conclusion=Q
)
print("Modus Ponens:")
print(f"Is Valid: {modus_ponens.is_valid()}")
print("Truth Table:")
modus_ponens.print_truth_table()

modus_tollens = ArgumentForm(
    P >> Q,
    ~Q,
    conclusion=~P
)
print("Modus Tollens:")
print(f"Is Valid: {modus_tollens.is_valid()}")
print("Truth Table:")
modus_tollens.print_truth_table()

disjunctive_syllogism = ArgumentForm(
    P | Q,
    ~P,
    conclusion=Q
)
print("Disjunctive Syllogism:")
print(f"Is Valid: {disjunctive_syllogism.is_valid()}")
print("Truth Table:")
disjunctive_syllogism.print_truth_table()

hypothetical_syllogism = ArgumentForm(
    P >> Q,
    Q >> R,
    conclusion=R
)
print("Hypothetical Syllogism:")
print(f"Is Valid: {hypothetical_syllogism.is_valid()}")
print("Truth Table:")
hypothetical_syllogism.print_truth_table()

dilemma = ArgumentForm(
    P | Q,
    P >> R,
    Q >> S,
    conclusion=R | S
)
print("Dilemma:")
print(f"Is Valid: {dilemma.is_valid()}")
print("Truth Table:")
dilemma.print_truth_table()

explosion_principle = ArgumentForm(
    False,
    conclusion=P
)
print("Explosion Principle:")
print(f"Is Valid: {explosion_principle.is_valid()}")
print("Truth Table:")
explosion_principle.print_truth_table()

tautology_from_no_premises = ArgumentForm(
    conclusion=True
)
print("Tautology From No Premises:")
print(f"Is Valid: {tautology_from_no_premises.is_valid()}")
print("Truth Table:")
tautology_from_no_premises.print_truth_table()

# invalid argument forms
print("==== Invalid Argument Forms ====")
non_sequitur = ArgumentForm(
    P,
    conclusion=Q
)
print("Non Sequitur:")
print(f"Is Valid: {non_sequitur.is_valid()}")
print("Truth Table:")
non_sequitur.print_truth_table()

affirming_the_consequent = ArgumentForm(
    P >> Q, Q,
    conclusion=P
)
print("Affirming The Consequent:")
print(f"Is Valid: {affirming_the_consequent.is_valid()}")
print("Truth Table:")
affirming_the_consequent.print_truth_table()

denying_the_antecedent = ArgumentForm(
    P >> Q, ~P,
    conclusion=~Q
)
print("Denying The Antecedent:")
print(f"Is Valid: {denying_the_antecedent.is_valid()}")
print("Truth Table:")
denying_the_antecedent.print_truth_table()

fallacy_of_the_excluded_middle = ArgumentForm(
    P | Q, P,
    conclusion=~Q
)
print("Fallacy of Excluded Middle:")
print(f"Is Valid: {fallacy_of_the_excluded_middle.is_valid()}")
print("Truth Table:")
fallacy_of_the_excluded_middle.print_truth_table()

contingency_from_no_premises = ArgumentForm(
    conclusion=P
)
print("Contingency From No Premises:")
print(f"Is Valid: {contingency_from_no_premises.is_valid()}")
print("Truth Table:")
contingency_from_no_premises.print_truth_table()
