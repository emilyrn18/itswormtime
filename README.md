# It's Worm Time!
It's Worm Time is a program that uses music from Spotify to generate art using frequencies and beats.

## Getting Started

To start working on this project you will first want to make sure you have VSCode and you have installed the python extension and have it enabled. Here is the VSCode installing link: https://code.visualstudio.com/
<br>You will also want to download GitBash: https://gitforwindows.org/

In git bash install Spotipy and libROSA by typing these commands into the command prompt and pressing ENTER one at a time:

pip install spotipy
<br>pip install LibROSA

Next you will want to clone this repository on your computer in a place you can remember to do this type the command cd Documents or cd Desktop into GitBash. Your gitbash will now be located in either your documents folder or desktop folder. 

Here are the steps to cloning:

1. click the green button that says "Clone or Download" and be sure that you are cloning with HTTPS. Now click the copy button.
2. Next open up GitBash and type in:    git clone https://github.com/emilyrn18/itswormtime.git
3. Once it has finished cloning onto your computer you should be able to see a folder called itswormtime in the place you designated
4. Now type cd itswormtime  into GitBash and press enter (You will now be within the repository and folder itswormtime)

## Commands to Remember for github

git pull
<br>git status
<br>git add .
<br>git commit -m "place your comment here"
<br>git push

# API's and Other Resources:
## Spotipy
Main Spotify for Developers site: https://developer.spotify.com/community/showcase/
<br>A light weight Python library for the Spotify Web API: https://github.com/plamere/spotipy
<br>Getting Started with Spotipy: https://spotipy.readthedocs.io/en/2.7.1/
<br>App for Inspiration: https://spotipy.readthedocs.io/en/2.7.0/
<br>Spotipy Features: https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/
<br>Spotipy Analysis: https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/
<br>Spotipy Currently Playing Track: https://developer.spotify.com/documentation/web-api/reference/player/get-the-users-currently-playing-track/
<br>Connecting program to spotipy library: https://towardsdatascience.com/profiling-my-favorite-songs-on-spotify-through-clustering-33fee591783d
<br>
<br> Song Analysis api: https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/

## How to run
1. Create login to spotify dev with spotify account credentials
2. Create an "app", name, and describe it
3. Then you'll be provided a client ID and a Secret
4. Clone this code and add your client ID and Secret to their designated variables
5. Now open command line and navigate to the cloned directory
6. run    worms.py [INSERT USERNAME HERE]
7. It will tell you to set your Spotify API Credentials as environment variables. Follow those instructions...or just manually set your user environment variables.
8. Run   worms.py [INSERT USERNAME HERE]    again
