# musical_time_machine
This Python script allows users to create a Spotify playlist of the Billboard Top 100 songs for a specific date. It uses web scraping with BeautifulSoup to extract the song titles from the Billboard website and the Spotipy library to search for and add the songs to a new playlist on the user's Spotify account.


To use the script, users need to have a Spotify account and register their app on the Spotify Developer Dashboard to obtain a client ID and secret key. The script prompts the user to enter a date in the format "YYYY-MM-DD" and uses it to generate a URL to the corresponding Billboard chart. It then extracts the song titles from the chart and searches for each song on Spotify using the Spotipy library. If a song is found, its Spotify URI is added to a list of song URIs, and if not, the script prints a message indicating that the song was skipped. Finally, the script creates a new private playlist on the user's Spotify account with the date and chart name in the title and adds all the songs to the playlist.

This project is useful for anyone who wants to explore Billboard chart history and discover popular music from past years. It demonstrates how to use web scraping and API integration to automate the process of creating a playlist based on a specific set of criteria.
