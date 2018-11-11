var gulp = require('gulp');
var watch = require('gulp-watch');
var livereload = require('gulp-livereload');
const imagemin = require('gulp-imagemin');
const autoprefixer = require('gulp-autoprefixer');
const cssmin = require('gulp-cssmin');
const rename = require('gulp-rename');
const minify = require('gulp-minify');
var spawn = require('child_process').spawn;
var open = require('gulp-open');


var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

gulp.task('css-minify', function() {
    gulp.src('./salon/static/css/style.css')
        .pipe(cssmin())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./salon/static/css'))
});

gulp.task('js-minify', function() {
    gulp.src('./salon/static/js/main.js')
        .pipe(minify({ext:{min:'.min.js'}, noSource: true,}))
        .pipe(gulp.dest('./salon/static/js'))
});

gulp.task('uri', function(){
  gulp.src(__filename)
  .pipe(open({uri: 'http://practicelab.sytes.net'}));
});


gulp.task('django', function() {

    var runserver = spawn(
        'python',
        ['manage.py', 'runserver','192.168.0.105:80'],
        { stdio: 'inherit' }
    );
    runserver.on('close', function(code) {
        if (code !== 0) {
            console.error('Django runserver exited with error code: ' + code);
        } else {
            console.log('Django runserver exited normally.');
        }
    });
});

gulp.task('go', function() {
    livereload.listen();
    gulp.watch("salon/static/css/style.css", ["css-minify"]);
    gulp.watch("salon/static/js/main.js", ['js-minify']);m
    gulp.watch(["salon/static/js/main.js", "salon/templates/*", "salon/static/css/style.css"]).on('change', livereload.changed);
});

gulp.task('default', ['django', 'go', 'uri']);