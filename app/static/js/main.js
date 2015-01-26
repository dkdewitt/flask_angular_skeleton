angular.module('app', ['ngRoute','userController', 'routes', 'userService', 'directives'              
                             ], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    
});