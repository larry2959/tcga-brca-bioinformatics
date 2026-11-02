"""Exploratory tumour-vs-normal differential expression using Mann-Whitney U + BH FDR."""
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests

def run_differential_expression(log_cpm, labels, gene_names=None):
    tumor=labels[labels=="Tumor"].index
    normal=labels[labels=="Normal"].index
    rows=[]
    for gene_id,row in log_cpm.iterrows():
        a=row.loc[tumor].to_numpy()
        b=row.loc[normal].to_numpy()
        if len(a)<2 or len(b)<2: continue
        _,p=mannwhitneyu(a,b,alternative="two-sided")
        rows.append({"gene_id":gene_id,
            "mean_logCPM_tumor":float(np.mean(a)),
            "mean_logCPM_normal":float(np.mean(b)),
            "log2_mean_difference":float(np.mean(a)-np.mean(b)),
            "p_value":float(p)})
    result=pd.DataFrame(rows)
    if result.empty: return result
    result["FDR"]=multipletests(result["p_value"],method="fdr_bh")[1]
    if gene_names is not None:
        result["gene_name"]=result["gene_id"].map(gene_names).fillna(result["gene_id"])
    else: result["gene_name"]=result["gene_id"]
    return result.sort_values("FDR").reset_index(drop=True)
