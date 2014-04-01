'use strict';

angular.module('cheeperApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/users/:userId/', {
        templateUrl: 'views/user-detail.html',
        controller: 'UserDetailCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
  // .run(function($cookieStore, $rootScope, $http) {
  //   if ($cookieStore.get('JWT')) {
  // 	console.log($cookieStore.get('JWT'));
  // 	$http.defaults.headers.common['Authorization'] = 'JWT ' + $cookieStore.get('JWT');
  //   } else {
  //   // TODO: Do login stuff
  //   }
  // });


