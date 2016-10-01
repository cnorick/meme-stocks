"use strict";
(function () {


    google.load('visualization', '1', { packages: ['corechart', 'table', 'line'] });
  
    // Creates the angular applications
    var app = angular.module('app', [

   // Angular modules
//    'ngAnimate',
 //   'ngRoute',

    // Custom modules - code in this app - look under scripts/factories
    

    // 3rd Party Modules
//    'ui.bootstrap',
    //'chart.js',
 //   'googlechart',
  //  'ngLocationUpdate',
   // 'angular-loading-bar'

    ])
    .config(['cfpLoadingBarProvider', function (cfpLoadingBarProvider) {
        cfpLoadingBarProvider.parentSelector = '#loading-bar-container';
    }]);


})();

