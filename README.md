# Hello World, DNS Pinger?
Not the Hello World your thinking...

I am going to get to the point, this is a pinging site, it is very simple, all it does is ping DNS servers to check if they are up, and how long it takes to get from there, and back, that is all, it pings all 17 DNS servers I have in this list every 3 secs.

The webpage is very simeple, it checks for the `Server.Data` file every 3 secs. and updates the page to show if they are online or offline, and the times, it also makes a sonar-like sound just for fun :)

## Files:

`index.html`: The main website page.

`Ping.Data`: A downloadable file that shows the lates ping data, in a readable format.

`Ping.Servers`: A ling of servers that it pings.

`Server.Data`: A file that the webpage uses to put the data on the website.

`Ping.wav`: A ping sound the website places when it updates the values.

Note: All values in the `Ping.Data` and `Server.Data` and just examples, and will be over-writed when you run the python program.

## To make this work, do the following:

First: Put the `index.html`, `Server.Data`, `Ping.Data`, and `Ping.Servers` info the same place/folder in `public_html`.

Next: Put the `Ping.py` folder in a folder outside of `public_html`.

Next: Open `Ping.py` and follow the comments.

Lastly: Run `Ping.py`, and your done!

Questions? Open a Issue, or contact me on Discord at Dan_foodz#0751
