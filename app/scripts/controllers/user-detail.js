'use strict';

angular.module('cheeperApp')
  .controller('UserDetailCtrl', function ($scope, $http, $routeParams) {
    $http({method: 'GET', url: 'http://127.0.0.1:8000/users/' + $routeParams.userId }).
      success(function(data) {
        $scope.user = data;
      }).
      error(function(data) {
    });
    $http({method: 'GET', url: 'http://127.0.0.1:8000/users/' + $routeParams.userId + '/cheeps/'}).
      success(function(data) {
        $scope.stream = data;
      }).
      error(function(data) {
    });
  });
