.. _Parallelizing:

*************
Parallelizing
*************

Hyperkite is designed to support evaluations in parallel without any modifications.

Let's say we start two trials at the same time:

.. code:: python

    import hyperkite

    STUDY_KEY = 'INSERT_KEY'

    trial_1 = hyperkite.new_trial(STUDY_KEY)
    trial_2 = hyperkite.new_trial(STUDY_KEY)
    
Then we can report back results using the ``report_loss`` function in any order (e.g. reversed) without running into problems:

.. code:: python

    trial_2.report_loss(400)
    trial_1.report_loss(500)
    
    
