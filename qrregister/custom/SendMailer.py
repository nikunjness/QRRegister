"""Simple HTTP Server.

This module builds on BaseHTTPServer by implementing the standard GET
and HEAD requests in a fairly straightforward manner.

"""


__version__ = "0.6"

__all__ = ["SimpleHTTPRequestHandler"]

import os
import posixpath
import BaseHTTPServer
import urllib
import cgi
import sys
import shutil
import mimetypes
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email import encoders
import urlparse

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    """Simple HTTP request handler with GET and HEAD commands.

    This serves files from the current directory and any of its
    subdirectories.  The MIME type for files is determined by
    calling the .guess_type() method.

    The GET and HEAD requests are identical except that the HEAD
    request omits the actual contents of the file.

    """

    server_version = "SimpleHTTP/" + __version__


    def do_PUT(self):

        """Serve a PUT request."""
        #message = self.__attr__
        # Extract and print the contents of the POST
        length = int(self.headers['Content-Length'])
        post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
        for key, value in post_data.iteritems():
            print "%s=%s" % (key, value)

        me = "yourmail@hostname.com"     #your sender mail here
        you = post_data['email'][0]

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Google I/O Extended Ahmedabad | Ticket"
        msg['From'] = me
        msg['To'] = you
        msg.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msg.attach(msgAlternative)

        msgText = MIMEText('Find attached entry ticket for the event. '
                           'If you are unable to find the QRCode or facing any other '
                           'issue plese drop a mail at Amitraj.tyagi@ishisystems.com')
        msgAlternative.attach(msgText)

        # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText('<table><tr><td colspan="2" align="center"><h4> Google I/O Extended Ahmedabad </h4></td></tr>'
                           '<tr><td colspan="2" align="center"><h5>Entry Ticket</h5></td></tr>'
                           '<tr><td align="left">'+post_data['name'][0] + '</td>'
                           '<td align="right"> <img src="cid:image1" width="98" height="98"></td></tr>'
                           '<tr><td colspan="2" align="left">Venue : <b>Ishi Systems</b> <br />'
                           'A 6/7, 6th Floor, <br />Safal Profitaire, <br />Near Auda Garden, <br />Prahlad Nagar Corp Road,<br />'
                           'Opp Ramada Hotel, <br />Ahmedabad</td></tr></table>', 'html')
        msgAlternative.attach(msgText)

        img_data = post_data['data'][0]
        msgImage = MIMEImage(img_data, 'gif', _encoder=encoders.encode_noop)
        msgImage.add_header('Content-ID', '<image1>')
        msgImage.add_header('Content-Transfer-Encoding', 'base64')
        msg.attach(msgImage)

        # Send the message via local SMTP server.
        s = smtplib.SMTP('emailhostname:port') #('smtp.gmail.com:587')
        s.set_debuglevel(1)
        s.starttls()
        s.login('username','password') # your credentials here
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(me, you, msg.as_string())
        s.quit()
        self.send_response(200)
        self.end_headers()


def test(HandlerClass = SimpleHTTPRequestHandler,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()

