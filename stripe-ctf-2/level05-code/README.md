## Level 5

Many attempts have been made at creating a federated identity system for the web (see [OpenID](http://openid.net/), for example). However, none of them have been successful. Until today.

The DomainAuthenticator is based off a novel protocol for establishing identities. To authenticate to a site, you simply provide it username, password, and pingback URL. The site posts your credentials to the pingback URL, which returns either `AUTHENTICATED` or `DENIED`. If `AUTHENTICATED`, the site considers you signed in as a user for the pingback domain.

You can check out the Stripe CTF DomainAuthenticator instance here: https://level05-1.stripe-ctf.com/user-xxxxxxxxxx. We've been using it to distribute the password to access Level 6. If you could only somehow authenticate as a user of a level05 machine...

To avoid nefarious exploits, the machine hosting the DomainAuthenticator has very locked down network access. It can only make outbound requests to other stripe-ctf.com servers. Though, you've heard that someone forgot to internally firewall off the high ports from the Level 2 server.

Interesting in setting up your own DomainAuthenticator? You can grab the source from `git clone https://level05-1.stripe-ctf.com/user-xxxxxxxxxx/level05-code`, or by reading on below.

### Running

- Install bundler: 'gem install bundler'
- Run srv.rb: './srv.rb'
- Point your browser to localhost:4567

### Solution

  * Upload the following `index.php` PHP to your endpoint from Level 2:
  ```php
  #!/usr/bin/env php
  <?php
  echo "AUTHENTICATED\n";
  ```
  * Set `pingback` to `https://level05-1.stripe-ctf.com/user-xxxxxxxxxx/?pingback=https://level02-1.stripe-ctf.com/user-xxxxxxxxxx/uploads/`

Originally posted at [https://stripe-ctf.com/levels/5](https://stripe-ctf.com/levels/5).
