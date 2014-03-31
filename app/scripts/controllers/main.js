'use strict';

angular.module('cheeperApp')
  .controller('MainCtrl', function ($scope, $http) {
    $http({method: 'GET', url: 'http://127.0.0.1:8000/cheeps/'}).
      success(function(data, status, headers, config) {
        $scope.stream = data;
      }).
      error(function(data, status, headers, config) {
    });
    $scope.add = function() {
       $scope.stream.push({
        "id": 8,
        "url": "http://localhost:8000/cheeps/8/",
        "created": "2014-03-25T10:39:35.211Z",
        "modified": "2014-03-25T10:40:42.524Z",
        "author": {
            "id": 3,
            "url": "http://localhost:8000/users/3/",
            "name": "Evil Bob",
            "handle": "bob",
            "thumbnail_url": "http://localhost:8000/media/thumbnails/83TUFUOY_bigger.jpeg"
        },
        "content": $scope.cheep.content
       });
     $scope.cheep.content = '';
    };
});
