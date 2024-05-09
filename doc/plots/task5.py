import matplotlib.pyplot as plt
# Data for Minimax performance using ">" and "<="
wihtout_pruning = [4680, 4680, 4680, 4623]
deep_pruning = [302, 457, 440, 337]
# Creating a standard boxplot (without the notched design) to compare performance
fig, ax = plt.subplots()
ax.boxplot([wihtout_pruning, deep_pruning], patch_artist=True, labels=['Without Pruning', 'Deep Pruning'])
ax.set_title('Comparison of Moves Evaluated: Useful Heuristic')
ax.set_ylabel('Number of Moves Tried')
plt.show()