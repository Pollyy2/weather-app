import requests
import json
from fasthtml.common import *
from shad4fast import *
from fasthtml.svg import *


#creating the app and router
app, rt = fast_app(pico=False, hdrs=(ShadHead(tw_cdn=True),))

#route for the home page
@rt("/")
def get():
    # function thar renders the home page with a form to input the city name
    return (
        Title("Weather App"),
        Div(
            Div(
                # svg icon(sun and cloud)
                Svg(
Path(d="M7.5 1.25C7.91421 1.25 8.25 1.58579 8.25 2V2.5C8.25 2.91421 7.91421 3.25 7.5 3.25C7.08579 3.25 6.75 2.91421 6.75 2.5V2C6.75 1.58579 7.08579 1.25 7.5 1.25ZM3.08086 3.08059C3.37375 2.78769 3.84862 2.78769 4.14152 3.08059L4.35758 3.29665C4.65047 3.58954 4.65047 4.06441 4.35758 4.35731C4.06468 4.6502 3.58981 4.6502 3.29692 4.35731L3.08086 4.14125C2.78796 3.84835 2.78796 3.37348 3.08086 3.08059ZM11.919 3.08073C12.2119 3.37362 12.2119 3.8485 11.919 4.14139L11.7029 4.35745C11.41 4.65034 10.9352 4.65034 10.6423 4.35745C10.3494 4.06456 10.3494 3.58968 10.6423 3.29679L10.8583 3.08073C11.1512 2.78784 11.6261 2.78784 11.919 3.08073ZM1.25 7.5C1.25 7.08579 1.58579 6.75 2 6.75H2.5C2.91421 6.75 3.25 7.08579 3.25 7.5C3.25 7.91421 2.91421 8.25 2.5 8.25H2C1.58579 8.25 1.25 7.91421 1.25 7.5ZM4.35758 10.6427C4.65047 10.9356 4.65047 11.4105 4.35758 11.7034L4.14152 11.9194C3.84862 12.2123 3.37375 12.2123 3.08086 11.9194C2.78796 11.6265 2.78796 11.1516 3.08086 10.8588L3.29692 10.6427C3.58981 10.3498 4.06468 10.3498 4.35758 10.6427Z", fill="yellow"),
Path(d="M16.2857 22C19.4416 22 22 19.4717 22 16.3529C22 13.8811 20.393 11.7802 18.1551 11.015C17.8371 8.19371 15.4159 6 12.4762 6C9.32028 6 6.7619 8.52827 6.7619 11.6471C6.7619 12.3369 6.88706 12.9978 7.11616 13.6089C6.8475 13.5567 6.56983 13.5294 6.28571 13.5294C3.91878 13.5294 2 15.4256 2 17.7647C2 20.1038 3.91878 22 6.28571 22H16.2857Z", fill="white"),
Path(d="M9.81079 5.00423C9.28249 4.68421 8.66276 4.5 8 4.5C6.067 4.5 4.5 6.067 4.5 8C4.5 8.89287 4.83433 9.70764 5.38464 10.326C5.84363 7.88877 7.54928 5.89586 9.81079 5.00423Z", fill="yellow"),
width =24,
height=24,
cls="w-16 h-16 mx-auto mb-4 "),
                Form(
                    H1("Weather App", cls="text-white text-2xl font-bold mb-4"),
                    P("Enter the city name below",
                        cls="text-blue-100 mb-4"),
                    Input(
                        type="text",
                        name="city",
                        placeholder="Enter city name",
                        cls="w-full p-2 rounded mb-4 text-black"
                    ),
                    Button(
                        "Get Weather",
                        type="submit",
                        cls="w-full bg-blue-500 font-semibold p-2 rounded hover:bg-blue-200"
                    ),
                    method="POST",
                    action="/",
                ),
                cls="bg-blue-800 p-8 rounded-xl shadow-lg w-80"
            ),
            cls="min-h-screen flex items-center justify-center bg-blue-400 "
        )
    )
#route that fetch the weather data from the openweathermap API and renders the result
@rt("/", methods=["POST"])
def weather(city: str = Form("city")):
    API_KEY = "0c217f00f3513a677f5a84123eb55b38"
    CITY = city

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    temperature = response.json().get("main", {}).get("temp")
    city = response.json().get("name")
#blocks that check the temperature and display alert messages based on the degree
    if temperature < 0:
        content = (
            Alert(f"Temperature is under 0 °C ({temperature} °C).", cls="alert-danger bg-red-500 text-center text-black font-bold p-2 rounded "),
            H1(f"Weather in {city}", cls="text-white text-xl text-center mt-4"),
            P(f"Temperature: {temperature} °C", cls="text-blue-100 text-center"),
        )
    elif temperature > 15:
        content = (
            Alert(f"Temperature is over 15 °C ({temperature} °C).", cls="alert-warning bg-green-400 text-center text-black font-bold p-2 rounded "),
            H1(f"Weather in {city}", cls="text-white text-xl text-center mt-4"),
            P(f"Temperature: {temperature} °C", cls="text-blue-100 text-center"),
        )
    else:
        content = (
            H1(f"Weather in {city}", cls="text-white text-xl text-center mt-4"),
            P(f"Temperature: {temperature} °C", cls="text-blue-100 text-center"),
        )
#return that displays form with the weather information, svg icon and button to go back to the home page
    return (
        Title("Weather App"),
        Div(
            Div(
                Svg(
Path(d="M7.5 1.25C7.91421 1.25 8.25 1.58579 8.25 2V2.5C8.25 2.91421 7.91421 3.25 7.5 3.25C7.08579 3.25 6.75 2.91421 6.75 2.5V2C6.75 1.58579 7.08579 1.25 7.5 1.25ZM3.08086 3.08059C3.37375 2.78769 3.84862 2.78769 4.14152 3.08059L4.35758 3.29665C4.65047 3.58954 4.65047 4.06441 4.35758 4.35731C4.06468 4.6502 3.58981 4.6502 3.29692 4.35731L3.08086 4.14125C2.78796 3.84835 2.78796 3.37348 3.08086 3.08059ZM11.919 3.08073C12.2119 3.37362 12.2119 3.8485 11.919 4.14139L11.7029 4.35745C11.41 4.65034 10.9352 4.65034 10.6423 4.35745C10.3494 4.06456 10.3494 3.58968 10.6423 3.29679L10.8583 3.08073C11.1512 2.78784 11.6261 2.78784 11.919 3.08073ZM1.25 7.5C1.25 7.08579 1.58579 6.75 2 6.75H2.5C2.91421 6.75 3.25 7.08579 3.25 7.5C3.25 7.91421 2.91421 8.25 2.5 8.25H2C1.58579 8.25 1.25 7.91421 1.25 7.5ZM4.35758 10.6427C4.65047 10.9356 4.65047 11.4105 4.35758 11.7034L4.14152 11.9194C3.84862 12.2123 3.37375 12.2123 3.08086 11.9194C2.78796 11.6265 2.78796 11.1516 3.08086 10.8588L3.29692 10.6427C3.58981 10.3498 4.06468 10.3498 4.35758 10.6427Z", fill="yellow"),
Path(d="M16.2857 22C19.4416 22 22 19.4717 22 16.3529C22 13.8811 20.393 11.7802 18.1551 11.015C17.8371 8.19371 15.4159 6 12.4762 6C9.32028 6 6.7619 8.52827 6.7619 11.6471C6.7619 12.3369 6.88706 12.9978 7.11616 13.6089C6.8475 13.5567 6.56983 13.5294 6.28571 13.5294C3.91878 13.5294 2 15.4256 2 17.7647C2 20.1038 3.91878 22 6.28571 22H16.2857Z", fill="white"),
Path(d="M9.81079 5.00423C9.28249 4.68421 8.66276 4.5 8 4.5C6.067 4.5 4.5 6.067 4.5 8C4.5 8.89287 4.83433 9.70764 5.38464 10.326C5.84363 7.88877 7.54928 5.89586 9.81079 5.00423Z", fill="yellow"),
width =24,
height=24,
cls="w-16 h-16 mx-auto mb-4"),
                Form(
                    H1("Weather App", cls="text-white text-2xl font-bold mb-4 text-center"),
                    *content,
                    Button(
                    "Look about another city",
                    type="button", 
                    onclick="window.history.back()", 
                    cls="w-full bg-blue-500 font-semibold p-4 mt-4 rounded hover:bg-blue-200"
                    ),
        ),
            cls="bg-blue-800 p-8 rounded-xl shadow-lg w-80"
            ),    
        cls="min-h-screen flex items-center justify-center bg-blue-400"
        )
    )


serve()
