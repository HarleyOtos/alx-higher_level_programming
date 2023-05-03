$(document).ready(function () {
  function translateHello() {
    const langCode = $('#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + langCode;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(translateHello);
  $('#language_code').keypress(function (e) {
    if (e.which == 13) {
      translateHello();
    }
  });
});
