angular.module('routes', ["ngRoute"])


.config(function($routeProvider,$locationProvider) {


    $locationProvider.html5Mode(true);
    $routeProvider

    .when('/register', {
        templateUrl: '/static/templates/user_templates/register.html',
        //controller: 'groupsController'
    })

    .when('/login', {
        templateUrl: '/static/templates/user_templates/login.html',
        //controller: 'groupsController'
    })



    .when('/logout', {template: ' ', controller: 'LogoutController',})  
    .when('/', {
            templateUrl: '/static/templates/home.html',
           

    })

    .otherwise({
       redirectTo: '/',  
        });
    
    });