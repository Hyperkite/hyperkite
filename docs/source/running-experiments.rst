.. _Running Experiments:

*******************
Running Experiments
*******************

Running experiments using Hyperkite is very simple.

Start a new trial by calling the ``new_trial`` function with your study ``key`` as argument:

.. code:: python
    
    trial = hyperkite.new_trial(key='INSERT_KEY')

You will receive a dictionary of hyperparameter values ``trial.values``.
Use your own code to evaluate the performance of the hyperparameter values and report back the valiation loss to Hyperkite using the ``report_loss`` function:

.. code:: python

    trial.report_loss(loss)


For a more complete example including training and evaluation code, check out the :ref:`Getting Started` guide.


