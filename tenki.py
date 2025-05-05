from flask import Flask , request , render_template 
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
Api_Key = os.getenv("Api_Key")

def get_weather(ido,keido):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={ido}&lon={keido}&appid={Api_Key}&units=metric&lang=ja"
    
   
  
    try: 
       res = requests.get(url)
       res.raise_for_status()
       data = res.json()
       print(data)
       name= data["name"]
       temp = data["main"]["temp"]
       temp_max = data["main"]["temp_max"]
       temp_min = data["main"]["temp_min"]
       description = data["weather"][0]["description"]
       windspeed= data["wind"]["speed"]
       return f"{name}の天気：{description}、{temp}℃（最高{temp_max}℃／最低{temp_min}℃）、風速{windspeed}m/s"
    except: 
       return "天気を取得できませんでした"
   
@app.route("/", methods= ["GET","POST"])
def index():
    result=""
    if request.method == "POST": 
        lat = request.form["lat"]
        lon = request.form["lon"]
        result = get_weather(lat,lon)  
    return render_template("index.html", result=result)
   
if __name__ == "__main__":
    app.run(debug=True)
   
