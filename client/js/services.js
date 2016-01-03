
angular.module('recordlyApp.services', []).factory('Album', function($resource) {
    return $resource('http://127.0.0.1:8000/albums/:id', {
        id: '@id'
    }, {
        update: {
            method: 'PUT'
        }
    });
}).service('popupService', function($window) {
    this.showPopup = function(message) {
        return $window.confirm(message);
    }
});