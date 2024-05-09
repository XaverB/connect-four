import matplotlib.pyplot as plt

# Data for Minimax performance using ">" and "<="
greater_than = [1426, 925, 867, 1657]
less_than_equal = [1208, 771, 817, 1337]

# Creating a standard boxplot (without the notched design) to compare performance
fig, ax = plt.subplots()
ax.boxplot([greater_than, less_than_equal], patch_artist=True, labels=['<, >', '<=, >='])
ax.set_title('Comparison of Moves Evaluated: Greater/Lesser vs EGreater/ELesser')
ax.set_ylabel('Number of Moves Tried')

plt.show()