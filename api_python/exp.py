import requests
r = requests.get("https://example.com")
print(r.status_code)  # Должно быть 200


# % python3 -m pytest --alluredir=allure-results/ api_python/tests
#  % python3 -m pytest api_python/tests