from web_maker.utils.information_gatherer import WebAppInformation
from web_maker.gpt.main_model import GptService
import constants
import json
import prompts

class TestGPTQueries():
    def test_gpt_query(self):
        gpt = GptService()
        prompt = constants.PROMPT

        response = gpt.query_gpt(prompt)
        assert response.choices[0].message.content is not None

    def test_gpt_query_contains_correct_filenames(self):
        gpt = GptService(model='gpt-4o')
        prompt = prompts.FILENAME_QUERY_PROMPT

        response = gpt.query_gpt(prompt)
        response_json = json.loads(response.choices[0].message.content)
        files = response_json['files']
        directories = response_json['directories']

        assert files is not None
        assert directories is not None
        assert len(files) > 0
        assert len(directories) > 0

    def test_gpt_query_contains_correct_steps_for_building_application(self):
        gpt = GptService(model='gpt-4o')
        prompt = prompts.STEPS_QUERY_PROMPT

        response = gpt.query_gpt(prompt)
        response_json = json.loads(response.choices[0].message.content)
        steps = response_json['steps']

        assert steps is not None
        assert len(steps) > 0