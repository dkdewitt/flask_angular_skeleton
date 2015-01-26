 angular.module('directives', [])
  .directive('navigation', function(userLoginService) {
    return {
        replace:'true',
        restrict: 'E',
      templateUrl: '/static/templates/navigation.html',
          link: function ($scope, element, attrs) {

            $scope.$watch( function () {
              
              return userLoginService.isLoggedIn();
               
            },
            function(){
              
              $scope.isLoggedIn = userLoginService.isLoggedIn();
              console.log($scope.isLoggedIn);
              $scope.userName = userLoginService.getUserName();
            });


  }
}
});