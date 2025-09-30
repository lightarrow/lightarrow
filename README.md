### Author Ronald Johnson on risk calculations using cybersecurity data. 
We will use a data pipeline to process our data. 

### 1. Data Sources
Logs  
Access Records  
Network Activity  
HR Data  

### 2. Feature Engineering
User Behavior Profiles  
Access Patterns  
Temporal Sequences  
Graph Structures  

### 3. Model Families
Supervised: RF, SVM, NN  
Unsupervised: Autoencoders, Isolation Forest  
Sequential: HMM, LSTM  
Graph-Based: GNNs, Community Detection  
Hybrid/Ensemble  

### 4. Outputs
Anomaly Scores  
Risk Alerts  
SOC Dashboard Insights  

We will lookat the risks faced by organizations and employees. 
![img.png](img.png)

Sample Threat Scenario
“A member of a group decimated by layoffs suffers a drop in job satisfaction. Angry at the company, the employee uploads documents to Dropbox, planning to use them for personal gain.”
This scenario would result in a number of observables in the generated data:
Data streams end for laid-off co-workers, and they disappear from the LDAP directory.
As evidenced by logon and logoff times, subject becomes less punctual because of a drop in job satisfaction.
HTTP logs show document uploads by subject to Drop-box.

Using data from a IEEE data generation set.
J. Glasser and B. Lindauer, "Bridging the Gap: A Pragmatic Approach to Generating Insider Threat Data," 2013 IEEE Security and Privacy Workshops, San Francisco, CA, USA, 2013, pp. 98-104, doi: 10.1109/SPW.2013.37. keywords: {Testing;Social network services;Organizations;Topology;Generators;Data privacy;Data models;Insider Threat;Synthetic Data;Modeling and Simulation},


We will apply some different models to understand what the human behaviour.  

Supervised Learning: Best when labeled insider/non-insider data is available; useful for classification.
Unsupervised Learning: Detects anomalies without labels; valuable for spotting new, unseen threats.
Sequential / Time-Series Models: Capture temporal trends in behavior, such as shifts in login or access patterns.
Graph-Based Models: Model relationships between users, systems, and data; powerful for spotting unusual access paths.
Hybrid & Ensemble Approaches: Combine multiple methods for improved detection and fewer false positives.
