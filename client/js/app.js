
angular.module('recordlyApp', ['ui.router', 'ngResource',
    'recordlyApp.controllers', 'recordlyApp.services'
]);

angular.module('recordlyApp').config(function($stateProvider, $httpProvider) {
    $stateProvider.state('albums', {
        url: '/albums',
        templateUrl: 'partials/albums.html',
        controller: 'AlbumListController'
    }).state('viewAlbum', {
        url: '/albums/:id/view',
        templateUrl: 'partials/album-view.html',
        controller: 'AlbumViewController'
    }).state('newAlbum', {
        url: '/albums/new',
        templateUrl: 'partials/album-add.html',
        controller: 'AlbumCreateController'
    }).state('editAlbum', {
        url: '/albums/:id/edit',
        templateUrl: 'partials/album-edit.html',
        controller: 'AlbumEditController'
    });
}).run(function($state) {
    $state.go('albums');
});