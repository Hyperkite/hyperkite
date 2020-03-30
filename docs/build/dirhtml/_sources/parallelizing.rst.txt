.. _Parallelizing:

*************
Parallelizing
*************

Hyperkite is designed to support evaluations in parallel without any modifications.

Let's say we start two trials at the same time:

.. code:: python

    import hyperkite

    study_key = 'INSERT_KEY'
    first_trial = hyperkite.new_trial(key=study_key)
    second_trial = hyperkite.new_trial(key=study_key)
    
Then we can report back results using the ``report_loss`` function in any order without running into problems:

.. code:: python

    second_trial_report_loss(400)
    first_trial.report_loss(500)
    
    
