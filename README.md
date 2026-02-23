# weather-dashboard

"COMPANY*: CODTECH IT SOLUTIONS

NAME: AYESHA SHAIKH

INTERN ID: CTIS4434

"DOMAIN*: PYTHON

"DURATION*: 4 WEEKS

MENTOR: NEELA SANTOSH

project summary:
This project is a simple Python program that collects and displays current weather data for multiple cities and then visualizes that data using charts. It demonstrates how to work with APIs, process data using a data analysis library, and create visualizations to better understand the information.

The main goal of the program is to fetch real-time weather information such as temperature and wind speed for selected cities and present it in a clear and visual format. The cities included in the project are Pune, Mumbai, Delhi, Bangalore, and Chennai. Each city is represented using its geographical coordinates, specifically latitude and longitude, which are required to request weather data from the online weather service.

The program uses an online weather API to get current weather information. An API, or Application Programming Interface, allows different software systems to communicate with each other. In this case, the program sends a request to a weather service along with the coordinates of each city. The API responds with data in JSON format, which contains structured information about the current weather conditions.

After receiving the response from the API, the program extracts the relevant weather details, specifically temperature and wind speed. It does this by accessing the “current_weather” section of the returned data. These values are then stored in a list as small records that include the city name, its temperature, and wind speed.

Once all the data is collected, the program converts this list into a data table using a data analysis library. This table format makes it easier to organize, view, and analyze the information. Each row represents a city, while the columns represent temperature and wind speed values. Printing this table allows users to quickly see the weather conditions across all cities.

The project also focuses on data visualization, which helps in understanding information more easily. Visualization is done using a plotting library that allows creation of graphs and charts. Two types of visualizations are created in this program.

The first visualization is a bar chart showing the temperature of each city. Each bar represents one city, and its height indicates the temperature. This makes it easy to compare which city is hotter or cooler at a glance.

The second visualization is a line graph showing wind speed across the cities. Each point on the graph represents a city’s wind speed, and the line connects these points to show variation. This helps users observe differences in wind conditions among the cities.

Overall, this project demonstrates important programming concepts such as using APIs to fetch real-time data, handling JSON responses, organizing data into structured formats, and creating visualizations to interpret information clearly. It is a practical example of how Python can be used for real-world applications like weather monitoring. The project also helps beginners learn about data collection, processing, and presentation, which are essential skills in data science and software development.

OUTPUT:

![Image](https://github.com/user-attachments/assets/e65204f4-9ce8-42d0-8c54-c845719220ec)

![Image](https://github.com/user-attachments/assets/10736fe2-d99d-43ca-a717-88f5592d65f5)
