from pulp import LpMaximize, LpProblem, LpVariable

prob = LpProblem(name="Maximize_Profit", sense=LpMaximize)

y1 = LpVariable(name="y1_FACTORY_MORATUWA", cat="Binary")  ##Cat can be Integer or default binary
y2 = LpVariable(name="y2_FACTORY_NEGAMBO", cat="Binary")
y3 = LpVariable(name="y3_WAREHOUSE_MORATUWA", cat="Binary")
y4 = LpVariable(name="y4_WAREHOUSE_NEGAMBO", cat="Binary")
y5 = LpVariable(name="y5_RETAILSHOP_MORATUWA", cat="Binary")
y6 = LpVariable(name="y6_RETAILSHOP_NEGAMBO", cat="Binary")

prob += 9 * y1 + 5 + y2 + 6 * y3 + 4 * y4 + 5 * y5 + 3 * y6

prob += 6 * y1 + 3 + y2 + 5 * y3 + 2 * y4 + 3 * y5 + 1 * y6 <= 15, "Constraint1"
prob += y2 >= y4, "Constraint2"
prob += y1 >= y3, "Constraint3"
prob += y1 + y2 <= 2, "Constraint4"
prob += y1 + y3 >= 2 * y4, "Constraint5"
prob += y3 + y4 <= 1, "Constraint6"

prob.solve()

print("Satus", prob.status)
print("Objective value (profit)", round(prob.objective.value(), 2))

for var in prob.variables():
    print(f"{var.name} = {var.value()}")
