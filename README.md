QRRegister
==========

##Installation

###To install the app on Ubuntu:


* install CouchDB via the command

    ` sudo apt-get install CouchDB `

* open the web interface in your browser at http://localhost:5984/_utils
* create a database, for example named "qrregister"
* in this database, create three documents with id "app" and "libs" and "custom" respectively and save it.
* in the document with id "app", add the file "index.html" as attachment
* in the document with id "libs", add ` angular.min.js ` and ` angular.simplecouch.js ` as attachment
* in the document with id "custom" add ` registercontroller.js ` as attachment


* run the application in your browser via

    ` http://localhost:5984/qrregister/app/index.html `



### References:

* [AngularJS 1.2.17] (https://ajax.googleapis.com/ajax/libs/angularjs/1.2.17/angular.min.js)
* [CouchDB] (http://couchdb.apache.org)
* [angular-simplecouch] (https://github.com/kleingy/angular-simplecouch)


