'use strict';

angular.module('cheeperApp')
  .controller('UserDetailCtrl', function ($scope, $http, $routeParams) {
    $http({method: 'GET', url: 'http://127.0.0.1:8000/users/2/cheeps/'}).
      success(function(data, status, headers, config) {
        $scope.stream = data;
      }).
      error(function(data, status, headers, config) {
    });
//    $scope.user = User.get({userId: $routeParams.userId});
//    $scope.stream = user.cheeps;
  });
