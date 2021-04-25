import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

# Hide y axis
ax.axes.yaxis.set_visible(False)

# Hide the right and top spines
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Move left y-axis and bottom x-axis to centre
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')


# Add zero label
plt.annotate('0', (0, 0), xytext=(0, .51), ha='center')

# Populate ticks
labels = []
locs = []
for sign in [-1, 1]:
    for e in range(-4,1):
        for p in range(16):
            f = sign * p * pow(2, e)
            if f not in locs:
                locs.append(f)
                label = f'{f:g}' if  abs(f) != 0 else ''
                labels.append(label)

# Set ticks
ax.set_xticklabels(labels)
ax.set_xticks(locs)
ax.tick_params('both', length=20, width=1, labelsize=9)
plt.xticks(rotation=90)

# Save output
figure = plt.gcf()
figure.set_size_inches(8, 2)
plt.savefig("floats_distribution.png", dpi=300, transparent=True)
