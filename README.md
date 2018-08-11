# Web-Scraping-Amazon-MensFashion-Search-Images-Beautiful-Soup-Python

Using Python and Beautiful Soupe this code is able to download images from amazon.com Men's Fashion department in Clothing and download top N images for every search Provided in the keywords file.

What Beautiful Soup does is parses the webpage in its html format so we can easily access any of the html tags, and even refine it with different classes.
It's really easy to use, just check the code and you will get the gist of how it works.

### My Use Case
I have used Amazon's Clothing -> Mens Fashion Department to scrape images form it.
There is a file named keywords.txt which contains all the keywords which will be used to search
The format in which the it should be filled is 
#### "(Number Of Images You Want) (((SINGLE SPACE))) (Keywords seperated by spaces)"
  Example : "12 red jacket"
  So it will download first 12 images when red jacket is searched under amazon's men fashion brand

The Code is quite easy to understand 
 
## Output
![screen shot 2018-08-11 at 11 57 54 pm](https://user-images.githubusercontent.com/15246084/43995240-28c40400-9dc8-11e8-9a2f-55de9a7619e2.png)

### Images stored in individual folder as mentioned in keywords
![screen shot 2018-08-11 at 11 58 02 pm](https://user-images.githubusercontent.com/15246084/43995242-2b359d7a-9dc8-11e8-94f5-40bc1d23d8dc.png)
![screen shot 2018-08-11 at 11 58 55 pm](https://user-images.githubusercontent.com/15246084/43995243-2b792b80-9dc8-11e8-92bf-9033cc55af6b.png)


### Issues with this
You may sometime get an error that says "urllib.error.HTTPError: HTTP Error 503: Service Unavailable"
Dont worry, it happens.
It's because Amazon don't allow automated access to their data, so they're rejecting your request because it didn't come from a proper browser.
So try again after sometime, or maybe the next day, it definitely works.

#### Happy Coding :)
