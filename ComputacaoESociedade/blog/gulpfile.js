const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const imagemin = require('gulp-imagemin');

function styles() {
    return gulp.src('./src/styles/*.scss')//recupera os arquivos
    .pipe(sass({ outputStyle: 'compressed' }))//compressão dos arquivos
    .pipe(gulp.dest('./public/css'));//pasta de destino
}
function images() {
    return gulp.src('./src/images/**/*')
    .pipe(gulp.dest('./public/images'))
    .on('error', console.error);
}

function html() {
    return gulp.src('./src/*.html')
    .pipe(gulp.dest('./public'))
    .on('error', console.error);
}

function js() {
    return gulp.src('./src/js/*.js')
    .pipe(gulp.dest('./public/js'))
    .on('error', console.error);
}

exports.default = gulp.parallel(styles, images, html, js);

exports.watch = function() {
    gulp.watch('./src/styles/*.scss', gulp.parallel(styles));
    gulp.watch('./src/*.html', gulp.parallel(html));
    gulp.watch('.src/js/*.js', gulp.parallel(js));
}