# prettytable: package/library/module
# PrettyTable: class

from prettytable import PrettyTable
# table: object
table = PrettyTable()

# add_colum(): Method, two inputs, string, list
table.add_column("Pockmon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# align: Attribute

table.align = 'l'
table.align["Type"] = 'l'
print(table)
