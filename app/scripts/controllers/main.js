'use strict';

angular.module('cheeperApp')
  .controller('MainCtrl', function ($scope) {
    $scope.stream = [
      {
        'id': '1',
        'content': 'It\'s true Robin, my cape is black and doubles as a glider. But yours is cool too. It\'s yellow and keeps bullets away. From me.',
        'author': {
          'handle': 'thebatman',
          'name': 'The Batman',
          'thumbnail_url': 'https://pbs.twimg.com/profile_images/792221815/Angry_batman_bigger.JPG'
        }
      },
      {
        'id': '2',
        'content': '#1: Advice for a daughter depends almost entirely on how attractive she is.',
        'author': {
          'handle': '@gselevator',
          'name': 'GS Elevator Gossip',
          'thumbnail_url': 'https://pbs.twimg.com/profile_images/1594623967/LloydBlankfeinLookingSkeptical_bigger.jpg'
        }
      },
      {
        'id': '3',
        'content': 'when a cute boy sneezes i dont say bless u because i see that god already has',
        'author': {
          'handle': 'umsassy',
          'name': 'no',
          'thumbnail_url': 'https://pbs.twimg.com/profile_images/446011173758984193/83TUFUOY_bigger.jpeg'
        }
      },
      {
        'id': '4',
        'content': 'Raisin cookies that look like chocolate chip cookies are the main reason I have trust issues.',
        'author': {
          'handle': 'billmurray',
          'name': 'Bill Murray',
          'thumbnail_url': 'https://pbs.twimg.com/profile_images/3240741454/9080e76653a80e43ae2058432bc76806_bigger.jpeg'
        }
      }
    ];
  });
