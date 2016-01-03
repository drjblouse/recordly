
describe('AlbumListController', function() {
    var scope, ctrl, mockBackend, expectedData;
    beforeEach(angular.mock.module('recordlyApp'));
    beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
        mockBackend = _$httpBackend_;
        expectedData = [
            {
                "id": 4,
                "url": "http://127.0.0.1:8000/albums/4",
                "title": "Dr Rap",
                "genre": "lll",
                "label": "Lab",
                "released": "2012-02-01",
                "artist_id": null,
                "favorite": false
            }
        ]
        mockBackend.expectGET('http://127.0.0.1:8000/albums').respond(expectedData);
        mockBackend.expectGET('partials/albums.html').respond()
        scope = $rootScope.$new();
        ctrl = $controller('AlbumListController', { $scope: scope });
    }));

    it('should return the album above', function() {
        mockBackend.flush();
        expect(scope.albums[0]['id']).toEqual(expectedData[0]['id']);
        expect(scope.albums[0]['title']).toEqual(expectedData[0]['title']);
    });
});
