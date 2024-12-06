# Secret Santa Mailer

Ho Ho Ho! Holidays are Coming!
This script will automatically get a recipient for
every secret santa and send a notification email to each santa's inbox
of who their gift recipient is.

It ensures that no one knows who their secret santa is... **not even you**! (That
is, unless you really want to know).


# Requirements

*  Python
*  SMTP server


# Instructions

## 1. Get The Script

Clone this repository
```
git clone https://github.com/afonsoingles/secret-santa.git
```

## 2. Modify the Configuration File

Make your desired modifications to the `config.py` configuration file.

In it, you must specify:

*  Your SMTP settings.
*  An email template.
*  The list of secret santas.
*  (Optional) a lookup of anyone who should not be someone elses santa.


## 3. Perform a Dry Run

```
$ ./main.py
```

This will read the configuration file and perform a "dry run" of the various
pairings between secret Santas and recipients. It will generate an output file
as specified by the `secret_santa_record_file` setting in `config.py`.

This record file is saved as `dont-open-me.txt` by default.



### Test Your SMTP configuration

Send a test email to confirm that the SMTP configuration is set up correctly:

```
$ ./main.py --send-test-email you@example.com
```

If it runs without any errors, then you're ready to send the secret Santa
emails.


## 5. Send the emails!

```
$ ./main.py --official
```

This will dispatch the emails and record what emails it sent to the file
specified by the `secret_santa_record_file` setting in `config.py`.

*Don't look at the contents of this file, unless you want to know who everyone's
secret Santa is.*

It will sequentially send emails to everyone.

Enjoy and have a Merry Christmas!


### Issues
If you got an error, please create a issue on GitHub.
