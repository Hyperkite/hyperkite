.. _Algorithms:

**********
Algorithms
**********

Hyperkite supports the following hyperparameter optimization algorithms:

================== ================================================================================================================================================================================================ ======
Algorithm          Description                                                                                                                                                                                      Source
================== ================================================================================================================================================================================================ ======
**Random Search**  The **Random Search** finds the optimal hyperparameter values by randomly sampling from the distribution that defines the hyperparameter space.                                                  `Random Search <https://en.wikipedia.org/wiki/Random_search>`_
**Hyperopt**       The **Hyperopt / TPE** or Tree-structured Parzen Estimator is a Bayesian optimization method that uses a Gaussian Process to model the hyperparameter space in order to explore it efficiently.  `Hyperopt <http://hyperopt.github.io/hyperopt/>`_, 
                                                                                                                                                                                                                    `Paper <https://papers.nips.cc/paper/4443-algorithms-for-hyper-parameter-optimization.pdf>`_

================== ================================================================================================================================================================================================ ======

More optimization algorithms will be supported in the near future.
