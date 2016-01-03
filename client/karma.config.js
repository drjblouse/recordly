
module.exports = function(config) {
  config.set({
    basePath: '',

    frameworks: ['jasmine'],

    files: [
      {pattern: 'lib/angular.js', watch: false},
      {pattern: 'lib/angular-*.js', watch: false},
      'js/app.js',
      'js/controllers.js',
      'js/*.js'
    ],

    exclude: [
      '**/*.swp'
    ],

    preprocessors: {
    },

    reporters: ['progress'],

    port: 9876,

    colors: true,

    logLevel: config.LOG_INFO,

    autoWatch: true,

    browsers: ['PhantomJS'],

    singleRun: false,

    concurrency: Infinity
  })
}
