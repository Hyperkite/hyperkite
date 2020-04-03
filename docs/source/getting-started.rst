.. _Getting Started:

***************
Getting Started
***************

In this short introduction we will show how to optimze hyperparameters using Hyperkite_.

This tutorial is also available as an `iPython notebook`_.


Installation
============

Install the Hyperkite package using your terminal:

.. code:: bash

    pip install hyperkite

For other ways to install Hyperkite, check out the `Installation`_ page.

Dummy Problem
=============

In a typical Machine Learning scenario, we aim to find the optimal hyperparameter values that result in the lowest loss on the validation set. For simplicity's sake, we avoid having to train and validate an entire model on every iteration and will show how to find the optimal parameters of the following dummy function:

.. figure:: _static/black-box-function.png
    :scale: 80
    :alt: Dummy black-box function that we will optimize (best parameters at param_a = 1 and param_b = 1.5). 
    :figclass: align-center

The function takes two parameters as input ``param_a`` and ``param_b`` and achieves the lowest loss at parameter values ``param_a = 1`` and ``param_b = 1.5``. Let's see if we can find these optimal values using Hyperkite.

Defining the hyperparameter space
=================================

Sign in to Hyperkite_, and press the **Create Study** button.

.. figure:: _static/screenshot_a.png
    :scale: 50
    :alt: After logging in you, press the **Create Study** button.
    :figclass: align-center

In the Study creation screen we can name our study ``getting_started_tutorial`` and create two hyperparmeters:

* A ``Categorical`` parameter named ``param_a`` with number of categories set to ``3``.
* A ``Uniform Range`` parameter named ``param_b`` between ``-10`` and ``10``.

Your screen should look like this:

.. figure:: _static/screenshot_b.png
    :scale: 50
    :alt: Hyperkite interface for hyperparameter selection.
    :figclass: align-center


After defining the hyperparameters you want to optimize in your Study, you will obtain an unique Study `key` which is all we need to access the study from our python code.

.. figure:: _static/screenshot_c.png
    :scale: 50
    :alt: Hyperkite will give you a unique Study key.
    :figclass: align-center

Make sure you keep a copy of the Study ``key`` on hand, as we will need it later in this tutorial.
 
Optimizing
==========


Now, we request a new set of hyperparameters we can create a new trial using ``trial = hyperkite.new_trial(study_key)``, which contains a dictionary of all hyperparameter values in ``trial.values``. After tring out these hyperparameter values we can report back the validation loss using ``trial.report_loss(loss)``.


.. code:: python

    import hyperkite

    number_of_iterations = 100

    for i in range(number_of_iterations):
        # Request new trial
        trial = hyperkite.new_trial(STUDY_KEY)

        # Try out hyperparameter values
        param_a = trial.values['param_a']
        param_b = trial.values['param_b']

        loss = black_box_function(param_a=param_a, param_b=param_b)

        # Report back loss
        trial.report_loss(loss)


View optimal values
===================

The optimal hyperparameter values can be viewed in the online interface, or requested directly using ``hyperkite.get_best_values(study_key)`` function:

.. code:: python

    print(hyperkite.get_best_values(STUDY_KEY))

If everything went well, a dictionary that looks like this will be printed: ``{'param_a': 1, 'param_b': 1.5092954608845162}``.

Sweet! As we can see, we were able to find hyperparameter values very close to our optimal point.


What's next?
============

Now that you have learned how to use Hyperkite to optimize hyperparameters you can start applying this knowledge on your own machine learning models. Try to replace the MultiLayerPerceptron in the tutorial with other models from sklearn, or start training more advanced deep learning models using Tensorflow_ or PyTorch_ and try to tweak them using Hyperkite_.

    
.. _iPython Notebook: https://github.com/hyperkite/hyperkite/blob/master/tutorial/Getting%20Started.ipynb

.. _Hyperkite: https://hyperkite.ai/
.. _Digit Dataset: https://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html
.. _PyTorch: https://pytorch.org/tutorials/
.. _Keras: https://keras.io/#getting-started-30-seconds-to-keras
.. _Tensorflow: https://www.tensorflow.org/tutorials/quickstart/beginner
