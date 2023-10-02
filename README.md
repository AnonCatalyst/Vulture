

## Discontinued
// Do to a problem with the googlesearch module suddenly not working with no explanation on why. This tool is now discontinued. Instead look forward to a new tool thats in development. Ominis Osint Tool is in development. it will have all the features of Vulture but it will be more advanced and have more to it. stay tuned for the Ominis Osint Tool drop as a enhanced better version of Vulture

# Vulture
is a unique username search tool witch validates if username exists on websites located in a urls.txt file.
it also looks for domains with the username contained in it.
it aswell searches for the username with a advanced google search method.

Vulture is a very good tool for osint Enthusiasts and forensics professionals.
and has been tested on Windows/Android/Linux for all around user support.

![My Image](img/screenshot.png)

# How to use:
```
sudo apt install exiftool
git clone https://github.com/AnonCatalyst/Vulture.git
cd Vulture
pip install -r requriments.txt
python vulture.py
```
> [ Vulture ] Has a total of 64 urls to search with and I plan to add more soon.

# Features
- Username Search
- keyword googlesearch
- advanced google search
- instagram & github profile information
- instagram profile download
- checks for metadata in img files from the folder created by the instagram profile download
- threading for speed
- status code for profile page validation

# Coming Features
> More profile pages to gather information from!
-
> More urls to search with

# Issues
> added randomized user agent with connection error handler as an attempt to fix the 429 too many requests issue. i also added platform detection so that if the user is on arch then it will not print the banner

* Problem with error handle for too many google search requests. currently my main priority to fix

# Developers
* Main Developer > AnonCatalyst 
* Optimization & Threads Developer > Gotr00t0day 
