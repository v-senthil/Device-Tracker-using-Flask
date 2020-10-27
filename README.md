# Device Tracker using Flask

## Used Software Applications:
### Mapbox 
### Flask


## To Make in Work

#### pip install flask

1. wget "https://github.com/v-senthil/Device-Tracker-using-Flask"
2. unzip the file
3. Go to templates/tracker.html
4. Change the Mapbox YOUR_API_KEY (get it from https://www.mapbox.com/)
5. In your terminal run python3 main.py
6. Go to http://127.0.0.1:5000/
7. Enter Latitude and Logitide Value into Database (data.db)
   - syntax: INSERT INTO map VALUES (datetime('now','localtime'), LATITUDE, LONGITUDE)
   - INSERT INTO map VALUES (datetime('now','localtime'), 21.56463, 77.464734)
8. See that the rocket image in the map changes the location according to the location you give
