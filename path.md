## "A computer program is said to learn from experience with respect to some clas of tasks T and performance measure P, if it's performance at tasks in T, as measured by P, improves with experience E." - Tom Michell
## inference variables risk_per_host
 dependant_variable, independent_variable
## Predictive analytics
## Descriptive analytics 
## Prescriptive analytics 
 reinforcement unsupervised and supervised machine learning.
# LLM
## Discriminative AI 
 categorizing input data or predicting 
## Generative AI 
 create new content based on user input
 Supervised learning
 input -> model -> output -> 
 prediction modeling
 Experience E (training data)
 Class of tasks T (Predict threat)
 Performance Measure P
 reinforcement learning is like a chess game learning machine
 Agent -> environment 
 Action -> 
 Feedback <-
# Policy table to track state. 
## reward column 
## player or agent column
 objective uncover insider threat
 evaluation - assess how well the machine learning approached worked. 
 actionable insight - identify what to do based on the results of the

 Example  Spam filtering requires previously labeled data, which is the domain of supervised learning.

 data exploring
 an instance is like a row
a feature is a column such as amount 
Feature is categorical - attribute hods data stored in discrete form
continuous feature hold data in an integer and infinite in any direction 

feature class is the dependant variable that is categorical 
response is continuous 

dimensionality is number of features in a dataset
sparsity the degree to witch data exists in the dataset. 

Visualization 
Comparison -the difference between two or more Items. 
is a feature important ? does it differ ? 

Relationship visualizations illustrate between two or more variables 
how do they interact? 

Distribution -- show statistical distribution values of a feather. histogram. 
spread or skewness of the data. 

Composition shows makeup of the data. stacked bar charts. 
subgroup contribute to the total? 


## data set preparation
Missing data - changes in collection, error, bias, lack 
imputation - systematic approach to fill in missing data. 
median imputation - input the median value to replace misssing values. 
outliers - why it exists - supervised learning 
Class label and distribution 
Class imbalance - distribution is not uniform. majority class - remove some to even distribution. 

Normalizing data 
values of a features shares a common property 
avoid - log transformation  if you have negative values in your data
Z-score Normalization 
given a feature with the following values 
do v-score normalization 
mean = 0 normalized values are 1

min max normalization 
transforming lower and upper bounding 
v is feature F and v' is the normalized value. 

log transformation - v orig and v' is normalized 
v' = log(v)

center your data on zero and let it distribute out from 0 to max positive and max negative. 
our Z scores help handle it. 

Sampling - population - sample is the subset
selecting a subset of the instances in a dataset as a proxy for the whole. 
historical split to historical and test 

split data via Sampling 

sample is a subset of the population 

sampling wit replacement is known in ML as bootstrapping. 

stratified sampling - 
goal 5 of 20 as a sample. 
stratum or group. 

random sampling stratified. 

Run the data sampling and training on vulnerability data. 

Dimensionality reduction -- the process of reducing the number of feathers in a dataset prior to modeling. 
reduces complexity and helps avoid the curse of dimensionality. 

the curse of dimensionality -- as complexity increases P the amount aof data N need to generalize accurately grows exponentially 

feature selection identify the minimal set of feature need to build a good model 
input data matrix and out put data matrix


variable subset selection 

feature selection 
feature extraction remove independent variables [model] -> dependent variable 




Supervised machine learning. 
Which of these sampling techniques maintains the same class distribution between the sample and the population?

Stratified sampling -- looks good so far. 

Have you put my resume through a sampling test against your population and determined that I meet the required criteria? 
If so what are the features you need for me to fit your model employee in this role. 

# modeling 

Apply a machine learning approach to your data. 


objective supervsed 
model maps input to out put
classification or regressions problem
supervised machine learning problem where the dependent variable is categorical 

# regression›
evaluation of test data 
predictive accuracy measure 
predict and measure the actual 
mean absolute error 

linear regression model in python 
assumption of a leaner relationship between predictors and the response

# Supervised learning modeal. 

## ML models 
Decision tree solves classification and regression problems. 
used when the model needs to be transparent. 

## Nural networks
Deep learning and large language models.  

# Ensamble learning

## Random forests. Gradient boosting machines. they end with a combination function that goes to -> output

# Unsupervised learning - identify inherent patterns structures or grouping in data 
K-means clustering - grouping clustering on different data grouping- customer segmentation, anomaly detection. 
association rules if then statements describe the co-occurrence of items within data. 
used in market

