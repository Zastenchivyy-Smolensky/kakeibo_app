$(function () {
  // $("h2")
  //   .mouseover(function () {
  //     $(this).text("マウスが載ったよ");
  //   })
  //   .mouseout(function () {
  //     $(this).text("テスト");
  //   });
  // $("h2").hover(
  //   function () {
  //     $(this).text("マウスが載ったよ");
  //   },
  //   function () {
  //     $(this).text("マウスが外れてたよ");
  //   }
  // );
  $(".example").hide();
  $(".menu1")
    .mouseover(function () {
      $(".example1").show();
    })
    .mouseout(function () {
      $(".example1").hide();
    });
});
