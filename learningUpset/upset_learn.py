
import upsetplot as us
from upsetplot import UpSet, generate_counts
import pandas as pd
import os


print(pd.__version__)
print(us.__version__)
example_counts = generate_counts()

ax_dict = UpSet(example_counts).plot()
