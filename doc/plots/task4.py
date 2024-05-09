import matplotlib.pyplot as plt

# Data for original and deep pruning
original_moves = [1426, 925, 867, 1657]
deep_pruning_moves = [993, 642, 676, 1145]

# Creating a boxplot to compare the number of moves evaluated under original and deep pruning conditions
fig, ax = plt.subplots()
ax.boxplot([original_moves, deep_pruning_moves], patch_artist=True, labels=['Original Pruning', 'Deep Pruning'])
ax.set_title('Comparison of Moves Evaluated: Original vs. Deep Pruning')
ax.set_ylabel('Number of Moves Evaluated')

plt.show()