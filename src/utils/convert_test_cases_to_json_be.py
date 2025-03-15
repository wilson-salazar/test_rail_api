class ConvertTestCasesToJsonBe:

    @staticmethod
    def convert_test_cases_to_json_be():
        """
        Converts a list of structured test cases into JSON format compatible with TestRail.
        :param test_cases: List of dictionaries containing test case data
        :return: JSON formatted for the TestRail API
        """
        json_cases = []
        epic = "https://www.notion.so/simetrik/URE138-Relate-sources-to-repositories-151ab53b41a180c5be67fd250a0280c8"
        aditional_text_steps = "\nAnd I send the [GET, PUT, POST, DELETE] request <url>\nAnd I send the payload\n\n{}"
        aditional_text_expected = "\nAnd I should receive a valid HTTP response [200, 201, 401]\nAnd should return an answer with the following schema"

        for case in ConvertTestCasesToJsonBe.test_cases:
            json_case = {
                "title": f"FE - {case['title']}",
                "template_id": 4,
                "type_id": 15,
                "priority_id": 2,
                "suite_id": 2,
                "custom_automated": False,
                "custom_stability_test": False,
                "custom_documentation": f"Epic: {epic}\n\nUS: {case['user_story']}\n\nAcceptance criteria: {case['acceptance_criteria']}",
                "custom_steps_separated": [
                    {
                        "content": "\n".join(case['steps']) + aditional_text_steps,
                        "expected": f"{case['expected_result']}{aditional_text_expected}",
                        "additional_info": "",
                        "refs": ""
                    }
                ],
                "custom_examples": "|||:url\n|| https://server.qaminor.simetrik.com/api/v1/reconciliations/{reconciliation_id}/"
            }
            json_cases.append(json_case)

        return json_cases

    # Example usage
    test_cases = [
        {
            "title": "Validate success notification when creating a source",
            "user_story": "US1 - Create Source with Repository",
            "acceptance_criteria": "There should be specific and clear messages providing visible feedback to the user on the reason for failure or success",
            "steps": [
                "Given I create a source with an existing repository",
                "When I complete the configuration",
                "And I save"
            ],
            "expected_result": "Then a confirmation message is displayed indicating that the source was successfully created with a repository link"
        }
    ]
