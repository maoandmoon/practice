const gulp = require('gulp');
const watch = require('gulp-watch');
const livereload = require('gulp-livereload');
const imagemin = require('gulp-imagemin');
const autoprefixer = require('gulp-autoprefixer');
const cssmin = require('gulp-cssmin');
const rename = require('gulp-rename');
const minify = require('gulp-minify');

const spawn = require('child_process').spawn;
const open = require('gulp-open');


const gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

gulp.task('css-minify', function() {
    gulp.src(['./salon/static/css/*.css', '!./salon/static/css/*.min.css'])
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
  .pipe(open({uri: 'http://192.168.0.105:8000/'}));
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
    gulp.watch(["salon/static/css/*.css","!salon/static/css/*.min.css" ], ["css-minify"]);
    gulp.watch("salon/static/js/main.js", ['js-minify']);
    gulp.watch(["salon/static/js/*", "salon/templates/*", "salon/static/css/*"]).on('change', livereload.changed);
});

gulp.task('default', ['django', 'go', 'uri']);