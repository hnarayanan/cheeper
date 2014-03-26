'use strict';

angular.module('cheeperApp')
  .controller('UserDetailCtrl', function ($scope, $routeParams, User) {
    $scope.pde = User.get({userId: $routeParams.userId});
  });
