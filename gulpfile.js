var gulp = require('gulp');
livereload = require('gulp-livereload');
cssmin = require('gulp-cssmin');
minify = require('gulp-minify');
rename = require('gulp-rename');
spawn = require('child_process').spawn;
open = require('gulp-open');


gulp.task('css-minify', function() {
    gulp.src(['./salon/static/css/*.css', '!./salon/static/css/*.min.css'])
      .pipe(cssmin())
      .pipe(rename({suffix: '.min'}))
      .pipe(gulp.dest('./salon/static/css'))
});


gulp.task('js-minify', function() {
  gulp.src(["./salon/static/js/*.js", "!./salon/static/js/*.min.js"])
    .pipe(minify({
      ext:{
        min:'.min.js'
      },
      noSource: true,
    }))
    .pipe(gulp.dest('./salon/static/js'));
});

gulp.task('djanger', function() {
    let runserver = spawn(
        './venv/Scripts/python.exe',
        ['manage.py', 'runserver', '192.168.0.105:8000'],
        {stdio: 'inherit'}
    );
    runserver.on('close', function(code) {
        if (code !== 0) {
            console.error('Django runserver exited with error code: ' + code);
        } else {
            console.log('Django runserver exited normally.');
        }
    });
});

gulp.task('watcher', function() {
  gulp.watch(["./salon/static/css/*.css", "!./salon/static/css/*.min.css"], ['css-minify']);
  gulp.watch(["./salon/static/js/*.js", "!./salon/static/js/*.min.js"], ['js-minify']);
});


gulp.task('liver', function() {
    livereload.listen();
    gulp.watch(["./salon/templates/**", "./salon/static/**"]).on('change', livereload.changed);
});

gulp.task('url', function(){
  gulp.src(__filename)
  .pipe(open({uri: 'http://192.168.0.105:8000/'}));
});


gulp.task('default', ['watcher', 'liver', 'djanger', 'url']);
