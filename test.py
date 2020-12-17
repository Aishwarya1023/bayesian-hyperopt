from models.hyperopt_tuning import get_sample_data, hyperopt_tuning

#DEFINE ARGUMENTS
data = get_sample_data()

logistic_arguments = {
                    'model_type': 'logistic',
                    'search_space': {
                                    'regParam': hp.uniform('regParam', 0, 1),
                                    'elasticNetParam': hp.uniform('elasticNetParam', 0, 1),
                                    'maxIter': hp.quniform('maxIter', 50,150, 1)
                                    }
                      }

decisiontree_arguments = {
                    'model_type': 'decisiontree',
                    'search_space': {
                                    'maxDepth': hp.choice('maxDepth', range(1,20)),
                                    'impurity': hp.choice('impurity', ["gini", "entropy"])
                                    }
                      }

trials = hyperopt_tuning(data, arguments = logistic_arguments, \
                         n_evals = 2, retrain_model = False)

#GET BEST PARAMETERS

#Case 1: Logistic Regression, Without Retraining on best params
trials = hyperopt_tuning(data, arguments = logistic_arguments, \
                         n_evals = 2, retrain_model = False)
best_params = trials.best_trial['misc']['vals'] 
print("Case 1 Best Params: ", best_params)

#Case 2: Logistic Regression, With Retraining on best params
trials = hyperopt_tuning(data, arguments = logistic_arguments, \
                         n_evals = 2, retrain_model = True)
best_params = trials.best_trial['misc']['vals'] 
print("\n Case 2 Best Params: ", best_params)

#Case 3: Decision Tree, Without Retraining on best params
trials = hyperopt_tuning(data, arguments = decisiontree_arguments, \
                         n_evals = 2, retrain_model = False)
best_params = trials.best_trial['misc']['vals'] 
print("\n Case 3 Best Params: ", best_params)

#Case 4: Decision Tree, With Retraining on best params
trials = hyperopt_tuning(data, arguments = decisiontree_arguments, \
                         n_evals = 2, retrain_model = True)
best_params = trials.best_trial['misc']['vals'] 
print("\n Case 4 Best Params: ", best_params)





