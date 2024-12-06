################################################################################
# SMTP configuration settings.
################################################################################
smtp = {
    'username': 'username',
    'password': 'password',
    'host': 'email-smtp.example.com',
    'port': 587,
    'from_email': 'email-used-to-send-letters@example.com',
}

################################################################################
# This the secret santa letter template that is used to send everyone the email.
# Note that {santa} and {recipient} are automatically replaced by the secret
# santa's name, and his/her recipient of their gift.
################################################################################
email_template = {
    'from_name': 'Secret Santa',
    'from_email': smtp['from_email'],
    'subject': 'Family Christmas',
    'body': """
Ho Ho Ho!

{santa}, you are {recipient}'s secret Santa!

Merry Christmas!
"""
}

################################################################################
# The complete list of all the secret santa's and their email addresses.
################################################################################
santas = {
    'James': 'james@example.com',
    'Mary': 'mary@example.com',
    'Nancy': 'nancy@example.com',
    'John': 'john@example.com',
    'Michael': 'michael@example.com',
    'Lisa': 'lisa@example.com',
    'David': 'david@example.com',
    'Linda': 'linda@example.com',
}

################################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values).
#
# If there are no incompatibles, leave this dictionary empty.
################################################################################
incompatibles = {
    
    'James': ('Mary',),

}

################################################################################
# DON'T ENTER INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
################################################################################
secret_santa_record_file = 'dont-open-me.txt'
