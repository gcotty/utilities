import pandas as pd
import random
from timer.timer import time_this


# Randomly sample a csv
@time_this
def random_sample(filename, p=0.1):
	num_lines = sum(1 for l in open(filename))
	skip_ix = random.sample(range(1, num_lines),
	                             (num_lines - int(num_lines * p)))
	
	df = pd.read_csv(filename, skiprows=skip_ix)
	
	return df

# Randomly downsample a dataframe by binary class
@time_this
def random_downsample(df, class_name, p=0.5):
	class_sizes = dict((c, len(df[df[class_name] ==c])) for c in 
                      df['CLASS'].unique())
	
	r = min(class_sizes.values()) / p
	
	maj_class = max(class_sizes, key=class_sizes.get)
	min_class = min(class_sizes, key=class_sizes.get)

	maj_resamp = df[df[class_name] == maj_class].sample(int(r))
	resamp = pd.concat([maj_resamp, 
	                    df[df[class_name] == min_class]])
	
	return resamp
