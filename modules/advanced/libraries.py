# libraries.py

import math
import random
import requests

def calculate_area_of_circle(radius):
    return math.pi * (radius ** 2)

def generate_random_numbers(count, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(count)]

def fetch_website_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Unable to fetch data from {url}. Status code: {response.status_code}"
    except requests.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Example usage
    print(f"Area of the circle with radius 5: {calculate_area_of_circle(5)}")
    print(f"Random numbers: {generate_random_numbers(5)}")

    website_content = fetch_website_content("https://www.example.com")
    print(website_content)  # Output will depend on the website's content
