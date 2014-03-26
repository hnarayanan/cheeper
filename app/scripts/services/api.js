'use strict';

angular.module('cheeperApp')
  .factory('User', function ($resource) {
      return $resource('http://localhost:8000/users/:userId', {}, {
        query: { params: { userId:'' } }
      });
    });
