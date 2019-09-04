import pandas as pd
import numpy as np

def isin_row(a, b, cols=None):
    cols = cols or a.columns
	return reduce(lambda x, y:x&y, [a[f].isin(b[f]) for f in cols])

def get_ci(alpha, scores):
	p = (alpha/2.0)*100
	l = max(0.0, np.percentile(scores, p)
	p = (alpha+((1.0-alpha)/2.0))*100
	u = min(1.0, np.percentile(scores, p))

	print('%.1f confidence interval %.1f%% nad %.1f%%'
	      % (alpha*100, l*100, u*100),'\n',
		  'Avg score: {}'.format(np.average(scores)))
