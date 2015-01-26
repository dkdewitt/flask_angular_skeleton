angular.module('app', ['ngRoute','userController', 'routes', 'userService'              
                             ], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    
});