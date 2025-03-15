import requests
import os
from dotenv import load_dotenv


class TestRailClient:
    """
    Cliente para interactuar con la API de TestRail.
    Maneja la autenticación y las solicitudes HTTP.
    """

    def __init__(self):
        load_dotenv()  # Cargar variables de entorno desde .env

        self.base_url = os.getenv("TESTRAIL_BASE_URL")
        self.username = os.getenv("TESTRAIL_USERNAME")
        self.api_key = os.getenv("TESTRAIL_API_KEY")

        if not all([self.base_url, self.username, self.api_key]):
            raise ValueError("Faltan credenciales en el archivo .env")

        self.headers = {
            "Content-Type": "application/json"
        }
        self.auth = (self.username, self.api_key)

    def send_request(self, method: str, endpoint: str, data: dict = None):
        """
        Método genérico para enviar solicitudes a la API de TestRail.
        :param method: Método HTTP (GET, POST, etc.)
        :param endpoint: Endpoint de la API
        :param data: Datos opcionales para la solicitud
        :return: Respuesta en formato JSON
        """
        url = f"{self.base_url}/index.php?/api/v2/{endpoint}"
        response = requests.request(method, url, auth=self.auth, headers=self.headers, json=data)

        if response.status_code not in [200, 201]:
            raise Exception(f"Error {response.status_code}: {response.text}")

        return response.json()

    def get_test_case(self, case_id: int):
        """
        Obtiene la información de un caso de prueba específico.
        :param case_id: ID del caso de prueba
        :return: Datos del caso de prueba en formato JSON
        """
        return self.send_request("GET", f"get_case/{case_id}")

    def add_test_result(self, test_id: int, status_id: int, comment: str = ""):
        """
        Agrega un resultado a una prueba ejecutada.
        :param test_id: ID de la prueba
        :param status_id: Estado de la prueba (1=Pasó, 2=Falló, etc.)
        :param comment: Comentario opcional
        :return: Respuesta de la API en JSON
        """
        data = {"status_id": status_id, "comment": comment}
        return self.send_request("POST", f"add_result/{test_id}", data)

    def get_test_run(self, run_id: int):
        """
        Obtiene información de una ejecución de prueba.
        :param run_id: ID de la ejecución de prueba
        :return: Datos de la ejecución en JSON
        """
        return self.send_request("GET", f"get_run/{run_id}")

    def close_test_run(self, run_id: int):
        """
        Cierra una ejecución de prueba en TestRail.
        :param run_id: ID de la ejecución de prueba
        :return: Respuesta en JSON
        """
        return self.send_request("POST", f"close_run/{run_id}")

    def add_new_test_case(self, section_id: int, data: dict):
        """
        Agrega un nuevo caso de prueba a TestRail.
        :param section_id: ID de la sección
        :param data: Datos del caso de prueba
        :return: Respuesta en JSON
        """
        return self.send_request("POST", f"add_case/{section_id}", data)


if __name__ == "__main__":
    client = TestRailClient()
    print(client.get_test_case(1))  # Ejemplo de uso
