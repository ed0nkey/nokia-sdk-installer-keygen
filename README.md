
# Nokia SDK Installer Keygen

Quick and easy script to generate serial numbers for InstallAnywhere Nokia 
SDK setup wizard. Made since forum.nokia.com doesn't exist anymore and 
there is no way to get keys for every installer on the internet.


# Guide

Make sure your setup looks like this one
![setup screen](https://files.catbox.moe/6v6m9h.png)

To get the Product ID and the Secret Key, unpack the setup executable 
(with 7zip, ...) and open the file at 
"InstallerData/Installer.zip/InstallScript.iap_xml". Then just search the 
keywords "PRODUCT_ID" and "SECRET_KEY" and get the values as shown below.
![prod](https://files.catbox.moe/w1s2p5.png)

![key](https://files.catbox.moe/j1ovfk.png)

Run nokia.py and provide those values with a username of your choosing to 
get a valid serial number for the installer.


# Enjoy

I hope this was helpful and if it was, please leave a star on this repo. 
Thanks!


