'use strict';

angular.module('cheeperApp')
  .controller('AuthCtrl', function ($cookieStore, $scope, $http) {
    $scope.signin = function() {
      $http
        .post('http://127.0.0.1:8000/auth-token/', $scope.credentials)
        .success(function(data, status, headers, config) {
          $cookieStore.put('JWT', data.token);
        })
        .error(function(data, status, headers, config) {
          $cookieStore.remove('JWT');
          console.log(data);
        });
    };
});

