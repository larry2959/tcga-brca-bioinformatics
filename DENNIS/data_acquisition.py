"""GDC STAR-count acquisition helpers; integrate with the notebook and test with actual GDC metadata."""
import os
import requests
import pandas as pd

GDC_FILES_URL = "https://api.gdc.cancer.gov/files"
GDC_DATA_URL = "https://api.gdc.cancer.gov/data"
PROJECT_ID = "TCGA-BRCA"

def build_filter(sample_type):
    return {"op":"and","content":[
        {"op":"in","content":{"field":"cases.project.project_id","value":[PROJECT_ID]}},
        {"op":"in","content":{"field":"data_category","value":["Transcriptome Profiling"]}},
        {"op":"in","content":{"field":"data_type","value":["Gene Expression Quantification"]}},
        {"op":"in","content":{"field":"experimental_strategy","value":["RNA-Seq"]}},
        {"op":"in","content":{"field":"analysis.workflow_type","value":["STAR - Counts"]}},
        {"op":"in","content":{"field":"access","value":["open"]}},
        {"op":"in","content":{"field":"cases.samples.sample_type","value":[sample_type]}}
    ]}

def query_gdc_files(sample_type, limit=60):
    fields=["file_id","file_name","file_size","cases.case_id","cases.submitter_id",
            "cases.samples.sample_type","cases.samples.submitter_id"]
    response=requests.post(GDC_FILES_URL,json={
        "filters":build_filter(sample_type),"fields":",".join(fields),
        "format":"JSON","size":500
    },timeout=120)
    response.raise_for_status()
    hits=response.json()["data"]["hits"]
    records=[]
    for hit in hits:
        for case in hit.get("cases",[]):
            for sample in case.get("samples",[]):
                if sample.get("sample_type") == sample_type:
                    records.append({
                        "file_id":hit["file_id"],"file_name":hit.get("file_name"),
                        "case_id":case.get("case_id"),"case_barcode":case.get("submitter_id"),
                        "sample_barcode":sample.get("submitter_id"),
                        "sample_type":sample.get("sample_type")
                    })
    return pd.DataFrame(records).drop_duplicates("file_id").head(limit)

def download_count_file(file_id, file_name, data_dir="data"):
    os.makedirs(data_dir,exist_ok=True)
    path=os.path.join(data_dir,file_name)
    if os.path.exists(path) and os.path.getsize(path)>0:
        return path
    with requests.get(f"{GDC_DATA_URL}/{file_id}",stream=True,timeout=180) as response:
        response.raise_for_status()
        with open(path,"wb") as out:
            for chunk in response.iter_content(1024*1024):
                if chunk: out.write(chunk)
    return path

def parse_star_counts(path):
    df=pd.read_csv(path,sep="\t",comment="#")
    if "gene_id" not in df.columns:
        df=df.rename(columns={df.columns[0]:"gene_id"})
    count_col="unstranded"
    if count_col not in df.columns:
        matches=[c for c in df.columns if "unstranded" in str(c).lower()]
        if not matches: raise ValueError(f"Unstranded count column missing: {df.columns.tolist()}")
        count_col=matches[0]
    keep=["gene_id",count_col]+(["gene_name"] if "gene_name" in df.columns else [])
    out=df[keep].rename(columns={count_col:"count"}).copy()
    out["count"]=pd.to_numeric(out["count"],errors="coerce")
    out=out.dropna(subset=["gene_id","count"])
    return out.loc[~out["gene_id"].astype(str).str.startswith("N_")]
