var gulp = require('gulp');
var less = require('gulp-less');
var path = require('path');
var bs = require('browser-sync').create();
var LessPluginCleanCSS = require('less-plugin-clean-css'),
  LessPluginAutoPrefix = require('less-plugin-autoprefix'),
  cleancss = new LessPluginCleanCSS({
    advanced: true
  }),
  autoprefix = new LessPluginAutoPrefix({
    browsers: ["last 2 versions"]
  });
/* ------------ FILE PATH ------------ */
var filePath = {};
filePath.src = './source';
filePath.tmp = './.tmp/';
filePath.page = ['./source/*.html'];
filePath.less = ['./source/less/*.less'];
filePath.js = ['./wap/**/*.js', './wap/**/**/*.js']
filePath.img = ['./images/lib/*.*']

gulp.task('less', function() {
  console.log('less')
  return gulp.src('./source/less/common.less')
    .pipe(less({
      plugins: [autoprefix, cleancss]
    }))
    .pipe(gulp.dest('./wap/site/css/lib/'));
});

gulp.task('img', function() {
  return gulp.src(filePath.img)
    .pipe(gulp.dest('./wap/site/images/lib/'));
})
gulp.task('serve', function() {
  bs.init({
    server: {
      baseDir: './',
      directory: true
    }
  });

});

gulp.task('watch', function() {
  gulp.watch(filePath.less, ['reload', 'less']);
  gulp.watch(filePath.img, ['reload', 'img']);
  bs.watch(filePath.page).on("change", bs.reload);
  bs.watch(filePath.js).on("change", bs.reload);
});
gulp.task('reload', function() {
  console.log('reload')
  bs.reload();
});

gulp.task('default', ['serve', 'less', 'watch']);