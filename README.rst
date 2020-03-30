*********
Hyperkite
*********

Hyperkite_ is a simple tool for hyperparmeter optimization.

It is designed to efficiently optimize the hyperparameters of machine learning models, such as gradient boosted trees or deep neural networks. The tool is designed to optimize hyperparameters using a wide range of powerful algorithms, including hyperopt, in a flexible and simple way. The platform supports parallel execution of without any modifications, and is easily extendable.

Getting Started
===============

1. Install Hyperkite.
2. Create a Study on Hyperkite_.
3. Define hyperparameters and copy unique Study key.
4. Use code snippet from code example to get trial variables and report loss.

For a more detailed instructions, please check out the `Getting Started`_ tutorial or the `Documentation`_.

Installation
============

Install the Hyperkite package by running the following command in your terminal:

.. code:: bash

    pip install git+git://github.com/hyperkite/hyperkite.git

For more information about installing Hyperkite, check out the more detailed Installation_ instructions.

Example
=======

Example code snippet explaining how to request new values for hyperparameter trial and how to report back loss.

.. code:: python

    import hyperkite
    trial = hyperkite.new_trial(key='INSERT_STUDY_KEY')

    loss = train_and_evaluate_model(trial.arguments) # Replace this line with own code

    hyperkite.report_loss(loss)


Documentation
=============

An extensive description of the Hyperkite framework can be found in the Documentation_.


.. _Hyperkite: https://hyperkite.ai
.. _Documentation: https://hyperkite.ai/docs
.. _Getting Started: https://hyperkite.ai/docs/getting-started
.. _Installation: https://hyperkite.ai/docs/installation/
