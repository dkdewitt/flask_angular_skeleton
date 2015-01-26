angular.module('userController', [])
.controller('LoginController', function($scope, $http, $window, $location,userLoginService) {
  //Login Function
  $scope.login = function (user) {
    userLoginService.login(user).then(function(d){
      userLoginService.setApiKey(d.api_key);
    })
  };
  $scope.logout = function(){
  }
})
.controller('RegisterController', function($scope, $http, $window, $location, userLoginService) {
  $scope.registerUser = function(user) {

    $http
      .post('/api/register/', $scope.user)
      .success(function(data, status, headers, config) {
        console.log(data);
        userLoginService.setApiKey( data.api_key);
        userLoginService.setUsername(user.firstname);
        $scope.message = 'Welcome';
        $location.path('/');
      })
      .error(function(data, status, headers, config) {
        // Erase the token if the user fails to log in
  
        delete $window.sessionStorage.api_key;
        // Handle login errors here
        $scope.message = 'Error: Invalid user or password';
      });
  };
})
.controller('LogoutController', function($scope, $http, $window, $location) {
    
    delete $window.sessionStorage.api_key;
    delete $window.sessionStorage.token ;
    delete $window.sessionStorage.userName ;
    delete $window.sessionStorage.apiKey ;
    $location.path('/');
});
