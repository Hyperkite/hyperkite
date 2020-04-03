'''
Study and Trial class
'''

from typing import List, Union
import json
import requests

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from hyperkite.constants import API_URL


class Trial():
    '''
    The Trial object references an trial in the Hyperkite database

    Args:
        study key: The key that references to a particular study in the Hyperkite database
        trial_key: The key that references to a particular trial in the Hyperkite database
        values: A list of the hyperparameter values sampled by Hyperkite
    '''
    def __init__(self, study_key: str, trial_key: str, no_sync=False):
        self.study_key = study_key
        self.trial_key = trial_key
        self._values = None
        
        if not no_sync:
            self._sync_values()

    @classmethod
    def _from_values(cls, study_key: str, trial_key: str, values: dict):
        trial = cls(study_key, trial_key, no_sync=True)
        trial._values = values

        return trial

    def __getattr__(self, name: str) -> Union[float, None]:
        ''' Getattr used to return values '''

        # Return values
        if name == 'values':
            if not self._values:
                self._sync_values()

            return self._values

    def _sync_values(self):
        ''' Request values from trial. '''

        path = urljoin(API_URL, 'studies/{}/trials/{}/values'.format(self.study_key, self.trial_key))

        response = requests.get(path)

        if response.ok:
            response_json = response.json()
            print(response_json)

            try:
                self.values = response_json['values']
            except KeyError as e:
                print('[Error] Wrong response content: {}'.format(e))
        else:
            print('[Error] Wrong response: {}'.format(response))


    def get_loss(self) -> Union[float, None]:
        ''' Request losses from trial and return latest loss.

        Returns: latest loss value from Hyperkite database '''

        path = urljoin(API_URL, 'studies/{}/trials/{}/loss'.format(self.study_key, self.trial_key))

        response = requests.get(path)

        if response.ok:
            response_json = response.json()

            try:
                return response_json['loss'][-1]
            except KeyError as e:
                print('[Error] Wrong response content: {}'.format(e))
        else:
            print('[Error] Wrong response: {}'.format(response))

    def get_losses(self) -> Union[List[float], None]:
        ''' Request and return list of all losses from trial.

        Returns: list of all losses of trial from Hyperkite database. '''

        path = urljoin(API_URL, 'studies/{}/trials/{}/loss'.format(self.study_key, self.trial_key))

        response = requests.get(path)

        if response.ok:
            response_json = response.json()

            try:
                return response_json['loss']
            except KeyError as e:
                print('[Error] Wrong response content: {}'.format(e))
        else:
            print('[Error] Wrong response: {}'.format(response))


    def report_loss(self, loss: float):
        ''' Report loss to Hyperkite database

        Args:
            loss: Loss value (outcome of the performed trial)

        Returns: HTTP Response indicating whether reporting was succesful
        '''

        path = urljoin(API_URL, 'studies/{}/trials/{}/loss'.format(self.study_key, self.trial_key))

        data = {'loss': loss}

        headers = {'Content-Type': 'application/json'}

        response = requests.put(path, data=json.dumps(data), headers=headers)

        return response


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

    def new_trial(self) -> Union[Trial, None]:
        '''Request new trial from Hyperkite '''

        path = urljoin(API_URL, 'studies/{}/trials/new_trial'.format(self.study_key))

        response = requests.put(path)

        if response.ok:
            try:
                response_json = response.json()

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

                return Trial._from_values(self.study_key, trial_key, values)
            except KeyError as e:
                print('[Error] Incomplete response: {}'.format(response))
                return None
        else:
            print('[Error] Wrong response: {}'.format(response))
            return None

    def get_best_trial(self) -> Union[Trial, None]:
        ''' Request best trial from study. '''

        path = urljoin(API_URL, 'studies/{}/best_trial'.format(self.study_key))

        response = requests.get(path)

        if response.ok:
            try:
                response_json = response.json()

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

                return Trial._from_values(self.study_key, trial_key, values)
            except KeyError as e:
                print('[Error] Incomplete response: {}'.format(response))
                return None
        else:
            print('[Error] Wrong response: {}'.format(response))
            return None


