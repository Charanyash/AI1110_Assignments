from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt


venn3(subsets=(30,30,10,20,6,4,5), set_labels =('Event A','Event B','Event C'),alpha = 0.5)


plt.show()
