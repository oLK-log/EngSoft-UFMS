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
    .pipe(imagemin())
    .pipe(gulp.dest('./public/images'));
}

function html() {
    return gulp.src('./src/*.html')
    .pipe(gulp.dest('./public'));
}

exports.default = gulp.parallel(styles, images, html);

exports.watch = function() {
    gulp.watch('./src/styles/*.scss', gulp.parallel(styles));
    gulp.watch('./src/*.html', gulp.parallel(html));
}