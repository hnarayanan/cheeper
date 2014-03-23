'use strict';

angular.module('cheeperApp')
  .controller('MainCtrl', function ($scope, $http) {
    $http({method: 'GET', url: 'http://127.0.0.1:8000/cheeps/'}).
      success(function(data, status, headers, config) {
        $scope.stream = data;
      }).
      error(function(data, status, headers, config) {
    });
});
