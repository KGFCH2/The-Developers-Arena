# week6_stats.py
# Probability and Statistical Testing example script
# Usage: python week6_stats.py

import numpy as np
from scipy import stats

def example_ttest():
    # Example: compare two samples (replace with your real groups)
    group1 = np.random.normal(50, 10, 100)
    group2 = np.random.normal(55, 10, 100)
    t_stat, p_val = stats.ttest_ind(group1, group2)
    print('Two-sample t-test: t_stat=%.4f, p-value=%.4f' % (t_stat, p_val))

def example_chi2():
    # Example contingency table
    obs = np.array([[50, 30], [20, 40]])
    chi2, p, dof, expected = stats.chi2_contingency(obs)
    print('Chi-square: chi2=%.4f, p=%.4f, dof=%d' % (chi2, p, dof))
    print('Expected table:\n', expected)

if __name__ == '__main__':
    print('=== T-test example ===')
    example_ttest()
    print('\n=== Chi-square example ===')
    example_chi2()
