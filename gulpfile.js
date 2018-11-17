const gulp = require('gulp');
const watch = require('gulp-watch');
const livereload = require('gulp-livereload');
const cssmin = require('gulp-cssmin');
const rename = require('gulp-rename');
const minify = require('gulp-minify');
const spawn = require('child_process').spawn;
const open = require('gulp-open');
// const imagemin = require('gulp-imagemin');
// const autoprefixer = require('gulp-autoprefixer');


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


gulp.task('django', function() {
    const runserver = spawn(
        'C:\\Users\\maoan\\PycharmProjects\\PracticeSalon\\venv\\Scripts\\python',
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

gulp.task('go', function() {
    livereload.listen();
    watch("salon/static/css/style.css", ["css-minify"]);
    watch("salon/static/js/main.js", ['js-minify']);
    watch(["salon/static/js/main.js", "salon/templates/*", "salon/static/css/style.css"]).on('change', livereload.changed);
});

gulp.task('uri', function(){
  gulp.src(__filename)
  .pipe(open({uri: 'http://192.168.0.105:8000/'}));
});

gulp.task('default', ['django', 'go', 'uri']);