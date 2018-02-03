# -*-: encoding: utf-8 -*-

from common.common_util import *
import json
import os
import operator
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


file_path = '../pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(file_path)]
tz_list = [record["tz"] for record in records if "tz" in record]
### get top elements of a list
# counts = get_count_of_list(tz_list)
# print(counts)
# top_tz = top_count_of_list(tz_list, 10)
# print(top_tz)
### collections.Counter class
# counts = Counter(tz_list)
# print(counts.most_common(10))

frame = DataFrame(records)
# print(frame)
# print(frame.columns)
### get top elements
# print(frame['tz'][:10])
# tz_counts = frame['tz'].value_counts()
# print(tz_counts)

### fillna function
# origin_tz = frame['tz']
# print(origin_tz)
# clean_tz = frame['tz'].fillna('Missing')
# clean_tz[clean_tz==''] = 'Unkonwn'
# tz_counts = clean_tz.value_counts()
# print(tz_counts)

### Making a horizontal bar plot can be accomplished using the plot method on the counts objects:
# tz_counts[:10].plot(kind='bar', rot=0)
# plt.show()

# a_pd = frame['a']
# results = Series([x.split()[0] for x in a_pd.dropna()])
# print(results[:5])
# print(results.value_counts()[:8])


### working with missing data
# df = DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
# df['four'] = 'bar'
# df['five'] = df['one'] > 0
# df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print(df2)
# print(df2['one'])
# print(pd.isna(df2['one']))
# print(df2['four'].notna())
# print(df2.isna())

# np.random.seed(2)
# ser = Series(np.arange(1, 10.1, 0.25)**2 + np.random.randn(37))
# bad = np.array([4, 13, 14, 15, 16, 17, 18, 20, 29])
# ser[bad] = np.nan
# methods = ['linear', 'quadratic', 'cubic']
# df = pd.DataFrame({m: ser.interpolate(method=m) for m in methods})
# print(df)
# df.plot()
# plt.show()

# d = {'a': list(range(4)), 'b': list('ab..'), 'c': ['a', 'b', np.nan, 'd']}
# df = DataFrame(d)
# print(df)
# df2 = df.replace('.', np.nan)
# print(df2)
# df3 = df.replace(r'\s*\.\s*', np.nan, regex=True)
# print(df3)
# df4 = df.replace(['a', '.'], ['b', np.nan])
# print(df4)

# df = DataFrame(np.random.randn(10, 2))
# df[np.random.rand(df.shape[0]) > 0.5] = 1.5
# df2 = df.replace(1.5, np.nan)
# print(df2)

# operating_system = np.where(a_pd.str.contains('Windows'), 'Windows', 'Not Windows')
# print(operating_system[:5])

# print(frame['a'])
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe.a.str.contains('Windows'), 'Windows', 'Not Windows')
# print(operating_system[:5])
by_tz_os = cframe.groupby(['tz', operating_system])
print(by_tz_os)
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts)