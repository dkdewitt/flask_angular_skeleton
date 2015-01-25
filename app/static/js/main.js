angular.module('app', ['ngRoute','ui.bootstrap'                  
                             ], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    
});