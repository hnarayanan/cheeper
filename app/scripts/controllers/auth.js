'use strict';

angular.module('cheeperApp')
  .controller('AuthCtrl', function ($scope, $http) {
    $scope.signin = function() {
      $http
        .post('http://127.0.0.1:8000/auth-token/', $scope.credentials)
        .success(function(data, status, headers, config) {
          $scope.token = data.token;
        })
        .error(function(data, status, headers, config) {
          console.log(data);
        });
    };
});

