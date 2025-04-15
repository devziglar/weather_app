import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"


def get_weather():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            result_label.config(text="City not found.")
            return

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"].title()
        location = f"{data['name']}, {data['sys']['country']}"

        result = f"{location}\n{condition}\nTemperature: {temp}°F"
        result_label.config(text=result)

    except Exception as e:
        result_label.config(text="Error retrieving weather.")

root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter City:", bg="#f0f0f0").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Helvetica", 10))
result_label.pack(pady=10)

root.mainloop()
