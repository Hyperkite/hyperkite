'''
Study and Trial class
'''


import json
import requests

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from hyperkite.constants import BASE_URL

SERVER_URL = urljoin(BASE_URL, 'api')


class Study():
    '''
    The Study object references to a study in the Hyperkite database
    and can be used to request (and thereby create) new trials.

    Args:
        key: This key references to a particular study in the Hyperkite database

    Attributes:
        study_key: This key references to a particular study in the Hyperkite database
    '''
    def __init__(self, key: str):
        self.study_key = key

    def new_trial(self):
        '''Request new trial from Hyperkite '''

        path = f'{SERVER_URL}/new_trial'

        data = {
                'study_key': self.study_key
               }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(path, data=json.dumps(data), headers=headers)

        if response.ok:
            try:
                response_json = response.json()
                print('New trial values: {response_json}')

                trial_key = response_json['trial_key']
                values = response_json['values']

                # Check output
                if trial_key == '':
                    print('[Error] Received empty trial key...')
                    return None
                if type(trial_key) is not str:
                    print('[Error] Trial key is not a string...')
                    return None
                if values == '':
                    print('[Error] Received empty values...')
                    return None
                if type(values) is not dict:
                    print('[Error] Arguments are a dict...')
                    return None

                return Trial(self.study_key, trial_key, values)
            except KeyError as e:
                print(f'[Error] Incomplete response: {response}')
                return None
        else:
            print(f'[Error] Wrong response: {response}')
            return None


class Trial():
    '''
    The Trial object references an trial in the Hyperkite database

    Args:
        study key: The key that references to a particular study in the Hyperkite database
        trial_key: The key that references to a particular trial in the Hyperkite database
        values: A list of the hyperparameter values sampled by Hyperkite
    '''
    def __init__(self, study_key: str, trial_key: str, values: dict):
        self._study_key = study_key
        self._trial_key = trial_key
        self.values = values

    def report_loss(self, loss: float):
        '''Report loss to Hyperkite database

        Args:
            loss: Loss value (outcome of the performed trial)

        Returns:
            response: HTTP Response indicating whether reporting was succesful
        '''

        path = f'{SERVER_URL}/report_loss'

        data = {'study_key': self._study_key,
                'trial_key': self._trial_key,
                'loss': loss
               }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(path, data=json.dumps(data), headers=headers)

        return response

