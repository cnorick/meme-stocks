(function () {

    var app = angular.module('app');

    var reportsDefinitions = [
    {
           name: '',
           templateUrl: '',
           route: ''
           }
    ];


    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {

        $routeProvider

                // route for the home page
                .when('/', {
                    templateUrl: 'app/components/dashboard/dashboardView.html',
                    reloadOnSearch: false
                })

                .otherwise({
                    templateUrl: 'app/components/dashboard/dashboardView.html',
                    reloadOnSearch: false
                })

        ;


        // builds the routes for all our reports
        angular.forEach(reportsDefinitions, function (report) {
            $routeProvider.when(report.route, {
                templateUrl: report.templateUrl,
                reloadOnSearch: false
            });
        });

        // use the HTML5 History API
        $locationProvider.html5Mode(true);
    }
    ]);


    app.run(['$rootScope', function ($rootScope) {
        $rootScope.reportsDefinitions = reportsDefinitions;
    }]);


})();

