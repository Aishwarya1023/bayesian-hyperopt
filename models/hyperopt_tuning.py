import numpy as np
import pandas as pd
import time
import hyperopt.pyll.stochastic

from hyperopt import fmin, hp, tpe, Trials, SparkTrials, STATUS_OK
from functools import partial
from sklearn import datasets
from pyspark.ml.classification import DecisionTreeClassifier, LogisticRegression
from pyspark.ml.feature import StringIndexer, VectorIndexer, VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

def get_sample_data():
  '''
  This function loads and returns the iris datatset for example purposes.
   
  Arguments: None
    
  Returns:
    data {PySpark Dataframe} -- Returns the iris dataset
  '''
  
  iris = datasets.load_iris()
  data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
  data = spark.createDataFrame(data1)
  
  # vectorize all numerical columns into a single feature column
  feature_cols = data.columns[:-1]
  assembler = VectorAssembler(inputCols=feature_cols, outputCol='features')
  data = assembler.transform(data)
  
  # convert text labels into indices
  data = data.select(['features', 'target'])
  label_indexer = StringIndexer(inputCol='target', outputCol='label').fit(data)
  data = label_indexer.transform(data)
  
  # only select the features and label column
  data = data.select(['features', 'label'])
  
  return data

def retrain_full_model(data, model_type, paramMap):
  '''
  This function takes the whole dataset and retrains the given model with best parameters. 
   
  Arguments: 
    data {PySpark Dataframe} -- A PySpark Dataframe containing feature vectors and labels
    paramMap {dict} -- A dictionary of the best parameter values
    model_type {str} -- The type of model to train 
    
  Returns:
    model -- Returns the model retrained on full dataset
  '''
  
  if model_type == 'logistic':
    lr = LogisticRegression()
    model = lr.fit(data, paramMap)
  elif model_type == 'decisiontree':
    dt = DecisionTreeClassifier()
    model = dt.fit(data, paramMap)
  
  return model

def objective(data, arguments):
  '''
  This function takes the training data and hyperparameters as input and \
  trains a model for the chosen set of parameters. It returns the loss, \
  as well as other information in the trials object.
   
  Arguments: 
    data {PySpark Dataframe} -- A PySpark Dataframe containing feature vectors and labels
    params {dict} -- A dictionary of chosen parameter distributions from the search space
    
  Returns:
    results {dict} -- loss, status, and runtime for that trial
  '''
  
  model_type = arguments['model_type']
  paramMap = arguments['search_space']
  train, test = data.randomSplit([0.80, 0.20])
  
  if model_type == 'logistic':
    lr = LogisticRegression()
    model = lr.fit(data, params=paramMap)
  elif model_type == 'decisiontree':
    dt = DecisionTreeClassifier()
    model = dt.fit(train, params=params)
    
  prediction = model.transform(test)
  evaluator = MulticlassClassificationEvaluator(metricName='accuracy')
  accuracy = evaluator.evaluate(prediction)
  
  return {'loss': -accuracy, 'status': STATUS_OK, 'eval_time': time.time()}

def hyperopt_tuning(data, arguments, algo = tpe.suggest, \
                    n_evals = 32, retrain_model = False):
  '''
  This function takes the training data as input and performs baysian hyperopt \
  tuning to generate the best hyperparameters and return the best model. 
   
  Arguments: 
    data {PySpark Dataframe} -- A PySpark Dataframe containing 2 columns "features" and "labels"
    search_space {dict} -- A dictionary of the parameter distributions to search from
    algo {str} -- The search algorithm to be used. By default it is bayesian
    n_evals {int} -- number of hyperparameter combinations to generate
    
  Returns:
    results {tuple} -- Returns (trials, model if retrained)
  '''
  
  train = partial(objective, data)
  trials = Trials()
  best_params = fmin(
    fn=train,
    space=arguments,
    algo=algo,
    trials = trials,
    max_evals=n_evals)
  
  if retrain_model:
    model = retrain_full_model(data, arguments['model_type'], best_params)
    return trials, model
  else:
    return trials