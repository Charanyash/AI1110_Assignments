#Values are taken from the venn diagram
Pr_A_or_B_or_C = 105/105

Pr_A = 51.0/105

Pr_B = 49.0/105

Pr_C = 35.0/105

Pr_AB = 15.0/105

Pr_BC = 9.0/105

Pr_CA = 11.0/105

Pr_ABC = 5.0/105

LHS = Pr_A_or_B_or_C

RHS = Pr_A + Pr_B + Pr_C - Pr_AB - Pr_BC - Pr_CA + Pr_ABC
if LHS == RHS:
    print("The identity is verified succesfully with LHS=RHS=",RHS)
