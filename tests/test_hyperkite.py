import json
from unittest import skipIf
from unittest.mock import Mock, patch

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from nose.tools import assert_true, assert_false, assert_equal, assert_is_none, assert_is_not_none

from hyperkite.hyperkite import Study, Trial
from hyperkite.constants import BASE_URL, TEST_STUDY_KEY

@skipIf(not TEST_STUDY_KEY, 'Skipping real study tests, because constants.TEST_STUDY_KEY is empty')
def test_study_integration():
    # Test request real API
    study = Study(TEST_STUDY_KEY)
    trial_from_real = study.new_trial()

    # Create mock
    with patch('hyperkite.hyperkite.requests.post') as mock_post:
        mock_post.return_value.ok = True
        mock_json = {'trial_key': '1ab23456cdef7gh8i9jk012l',
                     'values': {'test_param': 1.234}}
        mock_post.return_value = Mock()
        mock_post.return_value.json.return_value = mock_json

        # Test request mocked API
        study = Study(TEST_STUDY_KEY)
        trial_from_mocked = study.new_trial()

    # Assert
    assert_is_not_none(trial_from_real)
    assert_is_not_none(trial_from_mocked)

    assert_equal(type(trial_from_real._study_key), type(trial_from_mocked._study_key))
    assert_equal(type(trial_from_real._trial_key), type(trial_from_mocked._trial_key))
    assert_equal(type(trial_from_real.values), type(trial_from_mocked.values))


class TestStudy(object):
    @classmethod
    def setup_class(cls):
        cls.mock_post_patcher = patch('hyperkite.hyperkite.requests.post')
        cls.mock_post = cls.mock_post_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_post_patcher.stop()

    def test_new_trial_ok(self):
        self.mock_post.return_value.ok = False

        # Create mock
        mock_json = {'trial_key': '1ab23456cdef7gh8i9jk012l',
                     'values': {'test_param': 1.234}}
        self.mock_post.return_value = Mock()
        self.mock_post.return_value.json.return_value = mock_json

        # Test trial request
        study_key = '9zy87654xggf3gh2i1jk098l'
        study = Study(study_key)
        trial = study.new_trial()

        # Assert called correctly
        self.mock_post.assert_called_with(urljoin(BASE_URL, "api/new_trial"),
                                          data=json.dumps({'study_key': study_key}),
                                          headers={'Content-Type': 'application/json'})

        # Assert correct trial is returned
        assert_is_not_none(trial)
        assert_equal(trial._study_key, study_key)
        assert_equal(trial._trial_key, mock_json['trial_key'])
        assert_equal(trial.values, mock_json['values'])

    def test_new_trial_missing_trial_key(self):
        self.mock_post.return_value.ok = True

        # Create mock
        mock_json = {'values': {'test_param': 1.234}}
        self.mock_post.return_value = Mock()
        self.mock_post.return_value.json.return_value = mock_json

        # Test trial request
        study_key = '9zy87654xggf3gh2i1jk098l'
        study = Study(study_key)
        trial = study.new_trial()

        # Assert return None
        assert_true(self.mock_post.called)
        assert_is_none(trial)

    def test_new_trial_empty_trial_key(self):
        self.mock_post.return_value.ok = True

        # Create mock
        mock_json = {'trial_key': '',
                     'values': {'test_param': 1.234}}
        self.mock_post.return_value = Mock()
        self.mock_post.return_value.json.return_value = mock_json

        # Test trial request
        study_key = '9zy87654xggf3gh2i1jk098l'
        study = Study(study_key)
        trial = study.new_trial()

        # Assert return None
        assert_true(self.mock_post.called)
        assert_is_none(trial)

    def test_new_trial_wrong_trial_key_type(self):
        self.mock_post.return_value.ok = True

        # Create mock
        mock_json = {'trial_key': 123,
                     'values': {'test_param': 1.234}}
        self.mock_post.return_value = Mock()
        self.mock_post.return_value.json.return_value = mock_json

        # Test trial request
        study_key = '9zy87654xggf3gh2i1jk098l'
        study = Study(study_key)
        trial = study.new_trial()

        # Assert return None
        assert_true(self.mock_post.called)
        assert_is_none(trial)

    def test_new_trial_missing_values(self):
        self.mock_post.return_value.ok = True

        # Create mock
        mock_json = {'trial_key': '1ab23456cdef7gh8i9jk012l'}
        self.mock_post.return_value = Mock()
        self.mock_post.return_value.json.return_value = mock_json

        # Test trial request
        study_key = '9zy87654xggf3gh2i1jk098l'
        study = Study(study_key)
        trial = study.new_trial()

        # Assert return None
        assert_true(self.mock_post.called)
        assert_is_none(trial)

    def test_new_trial_empty_values(self):
        self.mock_post.return_value.ok = True

        # Create mock
        mock_json = {'trial_key': '1ab23456cdef7gh8i9jk012l',
                     'values': ''}
        self.mock_post.return_value = Mock()
        self.mock_post.return_value.json.return_value = mock_json

        # Test trial request
        study_key = '9zy87654xggf3gh2i1jk098l'
        study = Study(study_key)
        trial = study.new_trial()

        # Assert return None
        assert_true(self.mock_post.called)
        assert_is_none(trial)


    def test_new_trial_wrong_values(self):
        self.mock_post.return_value.ok = True

        # Create mock
        mock_json = {'trial_key': '1ab23456cdef7gh8i9jk012l',
                     'values': 123}
        self.mock_post.return_value = Mock()
        self.mock_post.return_value.json.return_value = mock_json

        # Test trial request
        study_key = '9zy87654xggf3gh2i1jk098l'
        study = Study(study_key)
        trial = study.new_trial()

        # Assert return None
        assert_true(self.mock_post.called)
        assert_is_none(trial)


class TestTrial(object):
    @classmethod
    def setup_class(cls):
        cls.mock_post_patcher = patch('hyperkite.hyperkite.requests.post')
        cls.mock_post = cls.mock_post_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_post_patcher.stop()

    def test_report_loss_ok(self):
        self.mock_post.return_value = Mock(ok=True)

        # Input
        study_key = '9zy87654xggf3gh2i1jk098l'
        trial_key = '1ab23456cdef7gh8i9jk012l'
        loss = 1.23

        # Test trial request
        trial = Trial(study_key=study_key,
                                trial_key=trial_key,
                                values={})
        response = trial.report_loss(loss)

        # Assert response True
        self.mock_post.assert_called_with(urljoin(BASE_URL, "api/report_loss"),
                                          data=json.dumps({'study_key': study_key,
                                                           'trial_key': trial_key,
                                                           'loss': loss}),
                                          headers={'Content-Type': 'application/json'})
        assert_true(response.ok)

    def test_report_loss_not_ok(self):
        self.mock_post.return_value = Mock(ok=False)

        # Input
        study_key = '9zy87654xggf3gh2i1jk098l'
        trial_key = '1ab23456cdef7gh8i9jk012l'

        # Test trial request
        trial = Trial(study_key=study_key,
                                trial_key=trial_key,
                                values={})

        response = trial.report_loss(1.23)

        # Assert response False
        self.mock_post.called
        assert_false(response.ok)

    
