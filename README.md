# Device Tracker using Flask

### Used Software Applications:
#### 1. Mapbox 
#### 2. Flask

<br><br>

This was made sepecifically for Raspberry Pi. Where the GPS Module send latitide and longitide data to sqlite3 database and which is then fetched using flask Application.

## To Make in Work

#### pip3 install flask

1. wget "https://github.com/v-senthil/Device-Tracker-using-Flask"
2. unzip the file
3. Go to templates/tracker.html
4. Change the Mapbox YOUR_API_KEY (get it from https://www.mapbox.com/)
5. In your terminal run - python3 main.py
6. Go to http://127.0.0.1:5000/
7. Enter Latitude and Logitide Value into Database (data.db)
   - syntax: INSERT INTO map VALUES (datetime('now','localtime'), LATITUDE, LONGITUDE)
   - INSERT INTO map VALUES (datetime('now','localtime'), 21.56463, 77.464734)
8. See that the rocket image in the map changes the location according to the location you give


## For using it all over the World

1. Create a account in https://ngrok.com/
2. Download ngrok accoring to your system
3. Unzip the file and place it in your desired location
4. Change directory to the place where ngrok file is present
5. Run - ./ngrok authtoken YOU_AUTH_TOKEN (which will be available in https://dashboard.ngrok.com/get-started/setup )
6. Run - ./ngrok http 5000
7. Copy the link and paste it in templates/track.html line 65 with an extension '/locationdata'
   - eg: var url = 'https://cfa635282g00.ngrok.io/locationdata';

#### Now the site in the port 5000 is globally avaliable all over the world
