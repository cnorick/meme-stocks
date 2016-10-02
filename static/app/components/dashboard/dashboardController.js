(function () {
    'use strict';

    angular
        .module('app')
        .controller('dashboard', dashboard);

    dashboard.$inject = ['$scope', '$http'];

    function dashboard($scope, $http) {

        function statsUrl () {
            var today = new Date();
            var url = 'api/memeStats';
            url += '?start=' + (new Date(today.getTime() - (7 * 24 * 60 * 60 * 1000))).toUTCString();
            url += '&end=' + today.toUTCString();
            return url;
        }

        getMemeStats();

        function getMemeStats(){
          console.log(statsUrl());
            $http.get(statsUrl())
                .then(function success(response){
                    console.log(response);
                }, function failure(response){
                    console.log(response);
                });
        }
    }
})();
