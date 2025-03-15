from src.utils.convert_test_cases_to_json_be import ConvertTestCasesToJsonBe
from src.utils.convert_test_cases_to_json_fe import ConvertTestCasesToJsonFe
from src.api.testrail_client import TestRailClient

class CaseModel:

    @staticmethod
    def create_new_test_case_be(section_id: int):
        count = 0
        client = TestRailClient()
        new_cases_json_list = ConvertTestCasesToJsonBe.convert_test_cases_to_json_be()
        for new_case_json in new_cases_json_list:
            client.add_new_test_case(section_id, new_case_json)
            count += 1

        return count

    @staticmethod
    def create_new_test_case_fe(section_id: int):
        count = 0
        client = TestRailClient()
        new_cases_json_list = ConvertTestCasesToJsonFe.convert_test_cases_to_json_fe()
        for new_case_json in new_cases_json_list:
            client.add_new_test_case(section_id, new_case_json)
            count += 1

        return count
