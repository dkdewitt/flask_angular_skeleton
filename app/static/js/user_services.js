 angular.module('userService', [])
 .service('userLoginService', function($http, $window) {

     var apiKey = null;
     var userName = null;
     this.login = function(user) {
         return $http.post('/api/users/', user);
     }

     this.setApiKey = function(apiKeyIn) {
         apiKey = apiKeyIn;
         $window.sessionStorage.apiKey = apiKey;
     };
     this.getApiKey = function() {
         return $window.sessionStorage.apiKey;
     };
     this.setUserName = function(userNameIn) {
         userName = userNameIn;
         $window.sessionStorage.userName = userName;
     };
     this.getUserName = function() {
         return $window.sessionStorage.userName;
     };
     this.isLoggedIn = function() {
         if ($window.sessionStorage.apiKey != null) {

             return true;
         } else {
             return false;
         }
     };

 });