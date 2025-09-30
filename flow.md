```mermaid
flowchart TD
    A[Data Sources] --> B[Feature Engineering]
    B --> C[Model Families]
    C --> D[Outputs]

    A --- A1[Logs]
    A --- A2[Access Records]
    A --- A3[Network Activity]
    A --- A4[HR Data]

    B --- B1[User Behavior Profiles]
    B --- B2[Access Patterns]
    B --- B3[Temporal Sequences]
    B --- B4[Graph Structures]

    C --- C1[Supervised: RF, SVM, NN]
    C --- C2[Unsupervised: Autoencoders, Isolation Forest]
    C --- C3[Sequential: HMM, LSTM]
    C --- C4[Graph-Based: GNNs, Community Detection]
    C --- C5[Hybrid/Ensemble]

    D --- D1[Anomaly Scores]
    D --- D2[Risk Alerts]
    D --- D3[SOC Dashboard Insights]
