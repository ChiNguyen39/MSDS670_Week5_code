#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Mon Sep 26 17:50:10 2022

@author: Khanh Chi Nguyen
Purpose: Week 5, 6 assignment
'''
#%%
# Import libraries

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

dpi = 300

#%%
# Set working path for this project
project_dir = os.getcwd()
df_filename = 'SalesCallData.csv'

# Import data about Sales Call:
df = pd.read_csv(project_dir + '/' + df_filename)

#%%
# Do some EDA
# Have an overview about the data:
df
df.info()

# The data seems good to go.

#%%
# Analysis
# Rename column names for further analysis:
df.columns = df.columns.str.replace(' ' , '_')

# Check the data again
df.info()

for i in df.columns:
    print(i)
    print(df[i].unique())

#%%
# PLOT THE DATA
# Plot 1: Number of call by Branch
branch_count = df['Branch'].value_counts(ascending = True)
branch = pd.Series(list(branch_count.index))
branch_count.index = range(len(branch_count))

fig, ax = plt.subplots(figsize = (8, 3))
ax.barh(branch, branch_count)
ax.set_title('Number of call by Branch')
ax.set_xlabel('Call')
ax.set_ylabel('Branch')
ax.set_xticklabels(branch, fontsize=10)
plt.tight_layout()
# Save the first barchart into png image for presentation
plot1_name = 'Number_of_call_by_branch.png'
fig.savefig(project_dir + "/Chart/"+ plot1_name, dpi = dpi)

# Plot 2: Number of call by Purpose by Branch
df_pivot_call_branch = pd.pivot_table(df, values = 'Calls', index = 'Call_Purpose', columns = 'Branch', aggfunc = np.sum)
ax = df_pivot_call_branch.plot(kind = 'bar')
fig = ax.get_figure()
fig.set_size_inches(10,13)
ax.legend()
ax.set_xlabel('Call Purpose', fontsize = 14,labelpad = 15)
ax.set_ylabel('Count of call', fontsize = 14,labelpad = 15)
ax.set_title('Number of Call Purpose by Branch',fontsize =16, pad =15)
for bar in ax.patches:
    bar_value = bar.get_height()
    text = f'{bar_value:,}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + bar_value
    bar_color = bar.get_facecolor()
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color, size=12)
plt.show()

plot2_name = 'Number_of_call Purpose_by_branch.png'
fig.savefig(project_dir + "/Chart/"+ plot2_name, dpi = dpi)

# Plot 3: Run line plot to have a look at Incoming and Outgoing Call by Hours
df_pivot_hour = pd.pivot_table(df, values = 'Calls', index = 'Hours', columns = 'Incoming_or_Outgoing', aggfunc = np.sum)
ax = df_pivot_hour.plot(kind = 'line')
fig = ax.get_figure()
fig.set_size_inches(10,8)
ax.legend()
ax.set_xlabel('Hours', fontsize = 14,labelpad = 15)
ax.set_ylabel('Count of call', fontsize = 14,labelpad = 15)
ax.set_title('Incoming and Outgoing Call by hours in a day',fontsize =16, pad =15)
line = ax.lines[0]
plt.show()

# Plot 4: View the Sale result by Shift
df_pivot_sales = pd.pivot_table(df, values = 'Calls', index = 'Shift', columns = 'Sale', aggfunc = np.sum)
ax = df_pivot_sales.plot(kind = 'bar')
fig = ax.get_figure()
fig.set_size_inches(10,13)
ax.legend()
ax.set_xlabel('Shift', fontsize = 14,labelpad = 15)
ax.set_ylabel('Count of Sale', fontsize = 14,labelpad = 15)
ax.set_title('Number of Sale by shift',fontsize =16, pad =15)
for bar in ax.patches:
    bar_value = bar.get_height()
    text = f'{bar_value:,}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + bar_value
    bar_color = bar.get_facecolor()
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color, size=12)
plt.show()

plot4_name = 'Number of Sale by Shift.png'
fig.savefig(project_dir + "/Chart/"+ plot4_name, dpi = dpi)

# Plot 5: View the work of each Rep_ID
ax = sns.catplot(x="Shift", y="Waiting_Minutes", col="Rep_ID", 
                kind="bar", data=df, ci=None, sharex=False, hue='Call_Purpose',
               col_wrap=4)
plt.show()
plot5_name = 'Waiting minutes each Shift by Rep_ID.png'
fig.savefig(project_dir + "/Chart/"+ plot5_name, dpi = dpi)


