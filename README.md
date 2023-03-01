# Fresh Air
 POV: You use Vim for some odd reason and have been slaving away at the command line for the past 5 hours. Your eyes are red, neck is hunched, all your muscles are tense, and you're probably losing your mind.\
 Looks like its time to go out on that daily walk and get some fresh air. Check the weather from within your terminal before you go out!

 ## How to use
 Install the FreshAir Package from [https://pypi.org/project/FreshAir](https://pypi.org/project/FreshAir/)
 ```bash
 pip install FreshAir
 ```
 Create an account and get your api key from [Open Weather Map](https://api.openweathermap.org)

 Navigate to ```FreshAir.py```. It should be in the source code for the package you just downloaded. For reference, mine is located at ```/Users/rayyaan/opt/anaconda3/lib/python3.9/site-packages/FreshAir.py```
 
Update the __api key__ variable with your respective key.

Now just run the following command in your terminal whenever you feel like heading out on that wonderful mid-day walk!
```bash 
FreshAir
``` 

## Purpose
I always wondered what was happening behind the scenes when I would write something like `pip install pandas` in the terminal. I decided to set out in building my own python package and publishing it on PyPi to learn more about this process. You can read my article [here](https://medium.com/@Rayyaan/create-your-own-python-package-and-publish-on-pypi-in-10-minutes-bb955a26029) if you want to learn how to make a package of your own!
