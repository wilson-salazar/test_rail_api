from src.models.case_model import CaseModel


class TestModelCase:

    def test_create_new_test_case_be(self):
        case_model = CaseModel()
        response = case_model.create_new_test_case_be(45895)
        assert response > 0

    def test_create_new_test_case_fe(self):
        case_model = CaseModel()
        response = case_model.create_new_test_case_fe(46160)
        assert response > 0
