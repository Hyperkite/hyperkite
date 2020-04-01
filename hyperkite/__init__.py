from hyperkite.hyperkite import Study, Trial

def new_trial(study_key: str):
    study = Study(study_key)
    trial = study.new_trial()
    
    return trial

def get_best_values(study_key: str):
    study = Study(study_key)
    best_trial = study.get_best_trial()

    return best_trial.values
