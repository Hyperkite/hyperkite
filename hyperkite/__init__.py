from hyperkite.hyperkite import Study

def new_trial(key: str):
    study = Study(key)
    trial = study.new_trial()
    
    return trial
