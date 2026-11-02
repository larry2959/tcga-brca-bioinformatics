"""EDA plotting helpers. Inputs must be aligned project objects from the central notebook."""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA

def plot_library_sizes(counts, labels):
    library_sizes=counts.sum(axis=0)
    qc=pd.DataFrame({"sample":library_sizes.index,"library_size":library_sizes.values,
                     "sample_type":labels.loc[library_sizes.index].values})
    ax=sns.boxplot(data=qc,x="sample_type",y="library_size")
    ax.set_title("Library sizes by sample type")
    ax.set_ylabel("Total raw counts")
    plt.tight_layout()
    return qc, ax.figure

def plot_pca(log_cpm, labels, n_genes=1000, random_state=42):
    genes=log_cpm.var(axis=1).nlargest(min(n_genes,len(log_cpm))).index
    matrix=log_cpm.loc[genes].T
    pcs=PCA(n_components=2,random_state=random_state).fit_transform(matrix)
    frame=pd.DataFrame(pcs,index=matrix.index,columns=["PC1","PC2"])
    frame["sample_type"]=labels.loc[frame.index]
    ax=sns.scatterplot(data=frame,x="PC1",y="PC2",hue="sample_type")
    ax.set_title("PCA of log2(CPM + 1)")
    plt.tight_layout()
    return frame, ax.figure

def plot_variable_gene_heatmap(log_cpm, n_genes=30):
    genes=log_cpm.var(axis=1).nlargest(min(n_genes,len(log_cpm))).index
    fig,ax=plt.subplots(figsize=(12,7))
    sns.heatmap(log_cpm.loc[genes],xticklabels=False,yticklabels=False,cmap="vlag",center=0,ax=ax)
    ax.set_title(f"Heatmap of {len(genes)} most variable genes")
    plt.tight_layout()
    return fig
