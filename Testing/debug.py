string_var = "(950, 1200, -20, 20-30)"
input = str(string_var).replace("(", "").replace(")", "").replace(" ", "").split(",")
parameters = [int(x) if "-" not in x else f"{x}" for x in input]
print(parameters)