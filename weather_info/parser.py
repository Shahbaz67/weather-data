import requests
from bs4 import BeautifulSoup

def parse():
    """
    Parse weather data and save in Summary model
    """
    url = "https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-and-regional-series#yearOrdered"

    response = requests.get(url)
    html_content = response.content

    # parses the html content
    soup = BeautifulSoup(html_content, "html.parser")

    # Get required tags - order, region, parameter
    form = soup.find(id="download-form")
    orders = form.find("fieldset").find_all("input")
    regions = form.find("select", id="region").find_all("option")[1:]
    parameters = form.find("select", id="parameter").find_all("option")[1:]

    # Saving the weather-data
    for order in orders:
        for region in regions:
            for parameter in parameters:

                # Set the values of radio button and dropdowns
                order["checked"] = True
                region["selected"] = True
                parameter["selected"] = True

                # Extract the selected values
                order_value = order["value"]
                region_value = region["value"]
                parameter_value = parameter["value"]

                # Making another request to download the data based on order, region & parameter values
                url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter_value}/{order_value}/{region_value}.txt"
                
                response = requests.get(url)

                # parse the text file data using python itself
                text = response.content.decode().strip()
                text_list = text.split('\n')[5:]
                text_list = [text.split() for text in text_list]
                header = text_list[0]  # headers
                data_table = text_list[1:]  # tabular data

                # Make a list of dict of dict to represent the tabular data
                data_value= []
                for data_row in data_table:
                    row_dict = {}
                    # Deal with 2 representaions separately: rank-order and year-order
                    if order_value == "ranked":   #rank-order
                        for i in range(0, len(data_row), 2):
                            if i % 2 == 0:
                                row_dict[header[i]] = {
                                    header[i+1]: data_row[i+1],
                                    "value": data_row[i]
                                }
                    else:                        #year-order
                        dict_ = {}
                        for i in range(1, len(data_row)):
                            dict_[header[i]] = data_row[i]
                        row_dict[data_row[0]] = dict_ 
                    data_value.append(row_dict)

                # Create Summary Model object 
                from weather_info.models import Summary
                Summary.objects.create(
                    order=order["id"],
                    region=region_value,
                    parameter=parameter_value,
                    data=data_value
                )

