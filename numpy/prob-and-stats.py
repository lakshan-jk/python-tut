import numpy as np
import scipy.stats as stats

data = np.random.normal(0, 1, 1000)

print("mean", np.mean(data))
print("median", np.median(data))
print("standard", np.std(data))

t_stat, p_value = stats.ttest_1samp(data, 0)
print("t_stat", t_stat)
print("p_value", p_value)
