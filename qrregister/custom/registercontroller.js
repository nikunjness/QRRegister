
var registerModule = angular.module('registerModule', ['SimpleCouch']);
var config = angular.module('Config', ['SimpleCouch']).config(function (couchConfigProvider,$httpProvider) {
                 couchConfigProvider.setServer('http://127.0.0.1:5984');
                 couchConfigProvider.setDB('dbname');

             });


function registerController($scope, couchdb) {
    $scope.Attendee = {};
    $scope.couchdb = couchdb;
    $scope.variable = '';
    $scope.errorWhileSubmit = null;
    $scope.successWhileSubmit = null;
    $scope.couchdb.config.setServer('http://localhost:5984');
    $scope.couchdb.db.use('qrregister');

    $scope.save = function()
    {
        $scope.Attendee._id = $scope.Attendee.email
        $scope.couchdb.doc.post($scope.Attendee,
        function(data){
            $scope.successWhileSubmit = "Data Added Successfully";
            window.setTimeout(function () {
                $scope.$apply(
                    function () {
                        $scope.successWhileSubmit = null;
                    }
                )
            }, 5000);
        },
        function(data){
            if(data.error=="conflict")
                $scope.errorWhileSubmit = "You are already registered. Please check your email for ticket. :) ";
            else
                $scope.errorWhileSubmit = data.reason
            window.setTimeout(function () {
                $scope.$apply(
                    function () {
                        $scope.errorWhileSubmit = null;
                    }
                )
            }, 5000);
            });
    }
};

registerModule.controller('registerController' , registerController);