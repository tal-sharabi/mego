from prettytable import PrettyTable

# Create a PrettyTable instance
pokemon_table = PrettyTable()

# Define the table headers
pokemon_table.field_names = ["Name", "Type"]

# Add data to the table
pokemon_table.add_row(["Pikachu", "Electric"])
pokemon_table.add_row(["Squirtle", "Water"])

pokemon_table.add_row(["Charmander", "Fire"])

# Print the table
print(pokemon_table)
