var gulp        = require('gulp');
var plumber     = require('gulp-plumber');
var sass        = require('gulp-sass');
var notify      = require('gulp-notify');
var browserSync = require('browser-sync').create();
var beep        = require('beepbeep')
var exec        = require('child_process').exec;
var flaskProcess = exec('flask run')

/* Global Function Declarations */
function plumbError(){
    return plumber({
        errorHandler: function (err) {
            notify.onError({
                templateOptions: {
                    date: new Date()
                },
                title: "Gulp error in" + err.plugin,
                message: err.toString()
            })(err);
        this.emit('end');
        }
    });
}

// Compile sass into CSS & auto-inject into browsers
gulp.task('sass', function() {
    return gulp.src(['node_modules/bootstrap/scss/bootstrap.scss', 'static/scss/*.scss'])
        .pipe(plumbError())
        .pipe(sass())
        .pipe(gulp.dest("static/css"))
        .pipe(browserSync.stream());
});

// Move the javascript files into our /src/js folder
gulp.task('js', function() {
    return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js', 'node_modules/jquery/dist/jquery.min.js', 'node_modules/tether/dist/js/tether.min.js'])
        .pipe(plumbError())
        .pipe(gulp.dest("static/js"))
        .pipe(browserSync.stream());
});

// Static Server + watching scss/html files
gulp.task('serve', ['sass'], function() {
    browserSync.init({
        // server: "./static",
        // notify: false,
        proxy: "127.0.0.1:5000"
    });
    gulp.watch(['node_modules/bootstrap/scss/bootstrap.scss',
        'static/scss/*.scss'], ['sass']);
    gulp.watch("templates/*.html").on('change', browserSync.reload);
    gulp.watch("../*.py").on('change', browserSync.reload);
});

/* Run Flask Server */
gulp.task('runFlask', function () {
    flaskProcess.stdout.on('data', function (data) {
        console.log(data);
    });
    flaskProcess.stderr.on('data', function (data) {
        console.log(data);
    });
});

gulp.task('default', ['runFlask','js','serve']);
