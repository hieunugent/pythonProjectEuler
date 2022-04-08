# sort_values()
# .head()
# .tail()
# .insert()
# .min()
# .idxmin()
# .idxmax()
# .count()
# .sum().

# .shape
# .fillna()
# .isna().values.any() is any number in data NAN
# plt.figure(figsize=(16, 10))
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Number of Posts', fontsize=14)
# plt.ylim(0, 35000)
# for column in reshape_df.columns:
#   plt.plot(reshape_df.index, reshape_df[column],
#            linewidth=3, label=reshape_df[column].name)
# plt.legend(fontsize=16)


# used .groupby() to explore the number of posts and entries per programming language

# converted strings to Datetime objects with to_datetime() for easier plotting

# reshaped our DataFrame by converting categories to columns using .pivot()

# used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()

# created(multiple) line charts using .plot() with a for-loop

# styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.

# added a legend to tell apart which line is which by colour

# smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.


# .agg()
# .nuique()
# .merge/join()

# DataFrame("id":value1, "set_count": value2, "set_size": value3)
# In this lesson we looked at how to:

#     # and how to embed images with the <img> tag.
# use HTML Markdown in Notebooks, such as section headings

# combine the groupby() and count() functions to aggregate data

# use the .value_counts() function

# slice DataFrames using the square bracket notation e.g., df[:-2] or df[:10]

# use the .agg() function to run an operation on a particular column

# rename() columns of DataFrames

# create a line chart with two separate axes to visualise data that have different scales.

# create a scatter plot in Matplotlib

# work with tables in a relational database by using primary and foreign keys

# .merge() DataFrames along a particular column

# create a bar chart with Matplotlib
