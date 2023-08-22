import requests
API_KEY="333145fa34d0e9742aeb51446ff958dd"
def get_data(place,forecast_days=None,kind=None,):
    url = f"http://api.openweathermap.org/data/2.5/forecast?id={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    return data

if __name__=="__main__":
    print(get_data(place="Tokyo"))
