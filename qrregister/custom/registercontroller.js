
var registerModule = angular.module('registerModule', ['SimpleCouch']);
var config = angular.module('Config', ['SimpleCouch']).config(function (couchConfigProvider,$httpProvider) {
                 couchConfigProvider.setServer('http://127.0.0.1:5984');
                 couchConfigProvider.setDB('dbname');

             });


function registerController($scope, couchdb) {
    $scope.Attendee = {}
    $scope.couchdb = couchdb
    $scope.variable = '';
    $scope.couchdb.config.setServer('http://localhost:5984')
    $scope.couchdb.db.use('qrregister')
    console.log($scope.couchdb)


    $scope.save = function()
    {
        $scope.Attendee.name= "Amit Bhoot"
        $scope.Attendee.contact = "9898475536"
        $scope.Attendee.email= "something@somone.com"
        $scope.couchdb.doc.post($scope.Attendee, function(data){
        alert(data)
        });

}
};

registerModule.controller('registerController' , registerController);