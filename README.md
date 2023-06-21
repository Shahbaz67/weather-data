# weather-data
Django app to parse summarised weather data available from UK MetOffice \
API service hosted on AWS EC2: http://54.88.21.167:8000/summary/

# Steps to run locally
```
git clone https://github.com/Shahbaz67/weather-data.git
docker compose up --build
```
This build would take around 5 mins as it takes time to parse the UK weather-data website

# Test Endpoint
Endpoint: '/summary'\
Select order, region, parameter from the dropdowns to get filtered time-series weather-data

# Tech Stack used
- Django Rest framework
- PostgreSQL
- Docker

