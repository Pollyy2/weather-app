# Weather App

A simple weather application built with **Python** and **Fasthtml**. Users can enter a city name to check the current temperature, and get alerts if the temperature is below 0°C or above 15°C.

## Live Demo

Try it online: [Weather App](https://weather-app-cya8.onrender.com)

## Features

- Input any city to get the current temperature.
- Visual alerts for extreme temperatures.
- Simple, responsive interface.

## Installation

Clone the repository: `git clone https://github.com/Pollyy2/weather-app.git`, install dependencies: `pip install -r requirements.txt`, and run the app locally (optional): `gunicorn main:app -k uvicorn.workers.UvicornWorker`.

## Tech Stack

- Python 3  
- Fasthtml (for fast web rendering)  
- Shad4fast (UI components)  
- Gunicorn & Uvicorn (ASGI server)


