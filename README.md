# weather-data
Django app to parse summarised weather data available from UK MetOffice

# Step to run this django application locally
```
git clone https://github.com/Shahbaz67/weather-data.git
docker compose up --build
```
This build would take 5-10 mins as it parses the UK weather-data website

# Test Endpoint
Endpoint: '/summary'\
Select order, region, parameter from the dropdowns to get filtered time-series weather-data

# Tech Stack used
- Django Rest framework\
- PostgreSQL\
- Docker\

