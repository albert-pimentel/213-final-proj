# -*- coding: utf-8 -*-
"""Part 2 Deliverable 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xLkVORP_DAm-mkK6sKBFhABN2vJKT7TC
"""

import pandas as pd
import csv
import math
import csv

qc_sample_input = pd.read_csv('QC_Sample_Input.csv')

def select_qualified_worker(qc_sample):
  qc_sample_copy = qc_sample.copy()
  WIds = qc_sample_copy['WorkerId'].tolist()
  qc0 = qc_sample_copy['Answer.qual_ctrl_0'].tolist()
  qc1 = qc_sample_copy['Answer.qual_ctrl_1'].tolist()
  qc2 = qc_sample_copy['Answer.qual_ctrl_2'].tolist()
  good_workers = []

  for i in range(0,len(WIds)):
    if (qc0[i] <= 3 and qc1[i] <= 3):
      good_workers.append(WIds[i])
      qc_sample_copy.loc[i,'Qualified_worker'] = "True"
    else:
      if (qc1[i] <= 3 and qc2[i] <= 3):
        good_workers.append(WIds[i])
        qc_sample_copy.loc[i,'Qualified_worker'] = "True"
      else: 
        if (qc0[i] <= 3 and qc2[i] <= 3):
          good_workers.append(WIds[i])
          qc_sample_copy.loc[i,'Qualified_worker'] = "True"
        else:
          qc_sample_copy.loc[i,'Qualified_worker'] = "False"

  return qc_sample_copy

def aggregate_good_data(qc_sample2):
  qc_sample_copy2 = qc_sample2.copy()
  qual_worker = qc_sample_copy2['Qualified_worker'].tolist()
  for i in range(0,len(qual_worker)):
    if (qc_sample_copy2.loc[i,'Qualified_worker'] == "False"):
      qc_sample_copy2 = qc_sample_copy2.drop([i])
  
  return qc_sample_copy2

qc_sample_output = select_qualified_worker(qc_sample_input)
agg_sample_output = aggregate_good_data(qc_sample_output)
qc_sample_output.to_csv("QC_Output.csv", index = False, header = True)
agg_sample_output.to_csv("AGG_Output.csv", index = False, header = True)