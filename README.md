QRRegister
==========

##Installation

###To install the app on Ubuntu:


* install CouchDB via the command

    ` sudo apt-get install CouchDB `

* open the web interface in your browser at http://localhost:5984/_utils
* create a database, for example named "qrregister"
* in this database, create a document with id "app" and save it.
* in the document with id "app", add the file "index.html" as attachment
* run the application in your browser via

    ` http://localhost:5984/qrregister/app/index.html `
    
### Send mail script configuration

* Add following handler entry to your couchdb configuration file

        [httpd_global_handlers]
        _sendmail = {couch_httpd_proxy, handle_proxy_req, <<"http://localhost:8005/">>}



### References:

* [AngularJS 1.2.17] (https://ajax.googleapis.com/ajax/libs/angularjs/1.2.17/angular.min.js)
* [CouchDB] (http://couchdb.apache.org)
* [angular-simplecouch] (https://github.com/kleingy/angular-simplecouch)
* [qrcode.js] (http://d-project.googlecode.com/svn/trunk/misc/qrcode/js/qrcode.js)
* [UI Bootstrap] (http://angular-ui.github.io/bootstrap/)
