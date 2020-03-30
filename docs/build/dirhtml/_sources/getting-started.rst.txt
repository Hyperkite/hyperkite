.. _Getting Started:

***************
Getting Started
***************

This short introduction uses Hyperkite_ to:

1. Build a neural network that classifies images.

2. Train the model and optimize hyperparameters.

3. And, finally, evaluate the accuracy of the model.


This tutorial is also available as an `iPython notebook`_.


Installation
============

Install the Hyperkite package using your terminal:

.. code:: bash

    pip install git+git://github.com/hyperkite/hyperkite.git

For other ways to install Hyperkite, check out the `Installation`_ page.

Define parameter space
======================

Sign in to Hyperkite_, and press the **Create Study** button.

.. figure:: _static/screenshot_a.PNG
    :scale: 50
    :alt: After logging in you, press the **Create Study** button.
    :figclass: align-center

Enter a study name, and select a **Uniform Range** hyperparameter between ``10`` and ``1000`` named ``n_layers``. Keep the default ``Hyperopt`` optimizer. Your screen should look like this:

.. figure:: _static/screenshot_b.PNG
    :scale: 50
    :alt: Hyperkite interface for hyperparameter selection.
    :figclass: align-center

When your done creating your Study, you will receive a unique Study ``key`` that we will need later in this tutorial to allow the Python code to communicate with the Study we have just created.

.. figure:: _static/screenshot_c.PNG
    :scale: 50
    :alt: Hyperkite will give you a unique Study key.
    :figclass: align-center

Make sure you keep a copy of the Study `key` on hand, as we will need it later in this tutorial.
 
Loading a Dataset
=================

Load the handwritten digits `Digit Dataset`_ from sklearn:

.. code:: python

    from sklearn import datasets

    # Load dataset
    digits = datasets.load_digits()

Split the dataset in ``training``, ``validation`` and ``testing`` subsets.

==========  =========  ========
Split       # Samples  Description
==========  =========  ========
Training    1400       The largest portion of the data samples are used to train the actual models. 
Validation  150        A small portion the data is used to evaluate models with different hyperparameters. 
Testing     247        Another portion is witheld until the very end to evaluate the final performance after tuning the model.
==========  =========  ========

.. code:: python

    # Use the first 1400 digits for training
    train_data = digits.data[:1400]
    train_labels = digits.target[:1400]

    # Use the next 150 digits for validation
    val_data = digits.data[1500:1650]
    val_labels = digits.target[1500:1650]

    # Use the last (247) digits for testing
    test_data = digits.data[1650:]
    test_labels = digits.target[1650:]
    
    
Train the model
===============

Let's use the ``MLPClassifier`` neural network classifier from ``sklearn`` to fit our data.

.. code:: python

    import hyperkite

    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import log_loss

    for _ in range(100):
        # Define model with Hyperkite
        trial = hyperkite.new_trial(key='INSERT_KEY')

        model = MLPClassifier(alpha=trial['alpha'],
                              learning_rate_init=trial['learnig_rate'])

        # Train model
        model.fit(train_data, train_labels)

        # Report back validation loss
        val_loss = log_loss(val_labels, model.predict_proba(val_data))
        hyperkite.report_loss(val_loss)

    # Calculate accuracy on validation set
    val_accuracy = sum(val_predictions == val_labels) / len(val_labels)
    print('Validation accuracy:', val_accuracy)

The ``hyperkite.new_trial`` function, with as argument the Study ``key`` is used to obtain values for the hyperparameters.
After fitting our model, ``trial.report_loss(loss)`` is used to report the validation loss to Hyperkite.

Evaluate final performance
==========================

After running our Hyperparameter optimization, we can view the best combination of hyperparameters in our browser.
Alternatively, let's use ``hyperkite.get_best_parameter`` to query the best set of hyperparameters.

.. code:: python


    hyperkite.get_best_parameters(key='')

    # Set-up best found settings
    model = MLPClassifier(alpha=trial['alpha'],
                          learning_rate_init=trial['learnig_rate'])

    # Train model
    model.fit(train_data, train_labels)

    # Evaluate final performance on test set
    predictions = model.predict(test_data)
    accuracy = sum(predictions == test_labels) / len(test_labels)
    print('Final accuracy with Hyperkite:', accuracy)


Sweet! The model performs a lot better than without hyperparameter tuning. Also note that using our study ``key`` we can request the best parameter values from hyperkite at any time later.



What's next?
============

Well, now that you have learned how to use Hyperkite to optimize hyperparameters you can start applying this knowledge on your own machine learning models. Try to replace the MultiLayerPerceptron in the tutorial with other models from sklearn, or start training more advanced deep learning models using Tensorflow_ or PyTorch_ and try to tweak them using Hyperkite_.

    
.. _iPython Notebook: https://github.com/hyperkite/hyperkite/blob/master/tutorial/Getting%20Started.ipynb

.. _Hyperkite: https://hyperkite.ai/
.. _Digit Dataset: https://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html
.. _PyTorch: https://pytorch.org/tutorials/
.. _Keras: https://keras.io/#getting-started-30-seconds-to-keras
.. _Tensorflow: https://www.tensorflow.org/tutorials/quickstart/beginner
