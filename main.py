"""Contoso Travel API: proste API z danymi pogodowymi dla miast.

Projekt szkoleniowy. Dane są zmyślone.
"""

import json
from os.path import abspath, dirname, join
from typing import List

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

current_dir = dirname(abspath(__file__))
data_path = join(current_dir, "cities.json")

app = FastAPI(title="Contoso Travel API")

with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)


@app.get("/")
def root():
    """Przekierowuje na dokumentację API pod adresem /docs."""
    return RedirectResponse(url="/docs", status_code=301)


@app.get("/countries")
def countries() -> List[str]:
    """Zwraca listę krajów dostępnych w danych."""
    return list(data.keys())


@app.get("/cities")
def all_cities() -> List[str]:
    """Zwraca listę miast ze wszystkich krajów."""
    return [city for country_cities in data.values() for city in country_cities]


@app.get("/countries/{country}/cities")
def cities(country: str) -> List[str]:
    """Zwraca listę miast w podanym kraju."""
    return list(data[country].keys())


@app.get("/countries/{country}/{city}/{month}")
def monthly_average(country: str, city: str, month: str):
    """Zwraca średnie temperatury w mieście w podanym miesiącu."""
    return data[country][city][month]

# funkcja zamieniajaca stopnie Fahrenheita na Celsjusza
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Zamienia stopnie Fahrenheita na Celsjusza."""
    return (fahrenheit - 32) * 5.0 / 9.0

