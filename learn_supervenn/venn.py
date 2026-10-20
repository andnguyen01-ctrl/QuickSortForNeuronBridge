from supervenn import supervenn
import matplotlib.pyplot as plt

sets = [{1,2,3,4},{3,4,5},{6,7,8}]
supervenn(sets, side_plots=False)

plt.savefig("output.png", dpi = 300, bbox_inches = "tight")
plt.close()