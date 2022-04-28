import requests
from requests.exceptions import RequestException


# Returns random facts for website in specified output and language
def generate_random_fact(output_format: str, language: str):
    # language must be english or german
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")
    # must be in specified format
    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    if response.status_code == 200:
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact
