"""Train/test evaluation helpers. Feature ranking is calculated from training data only."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,
                             roc_auc_score,confusion_matrix)

def compare_models(log_cpm, labels, test_size=0.25, random_state=42, n_features=500):
    X=log_cpm.T.copy()
    y=labels.loc[X.index].map({"Normal":0,"Tumor":1}).astype(int)
    X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=test_size,random_state=random_state,stratify=y)
    # Crucial: select features using training data only.
    selected=X_train.var(axis=0).nlargest(min(n_features,X_train.shape[1])).index
    train=X_train[selected]; test=X_test[selected]
    models={
        "Logistic Regression":Pipeline([
            ("imputer",SimpleImputer(strategy="median")),
            ("scaler",StandardScaler()),
            ("model",LogisticRegression(max_iter=3000,class_weight="balanced",random_state=random_state))]),
        "Random Forest":Pipeline([
            ("imputer",SimpleImputer(strategy="median")),
            ("model",RandomForestClassifier(n_estimators=300,class_weight="balanced",
                random_state=random_state,min_samples_leaf=2,n_jobs=-1))])
    }
    fitted={}; rows=[]; predictions={}
    for name,model in models.items():
        model.fit(train,y_train)
        pred=model.predict(test); prob=model.predict_proba(test)[:,1]
        fitted[name]=model
        predictions[name]={"predicted":pred,"probability":prob}
        rows.append({"Model":name,"Accuracy":accuracy_score(y_test,pred),
            "Precision":precision_score(y_test,pred,zero_division=0),
            "Recall":recall_score(y_test,pred,zero_division=0),
            "F1":f1_score(y_test,pred,zero_division=0),
            "ROC_AUC":roc_auc_score(y_test,prob)})
    return pd.DataFrame(rows).sort_values("ROC_AUC",ascending=False), fitted, predictions, y_test, selected, confusion_matrix
