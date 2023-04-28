$(document).ready(function () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
  function translateHello (langCode) {
    $.get(apiUrl, { lang: langCode }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    if (langCode !== '') {
      translateHello(langCode);
    }
  });
  $('#language_code').on('keypress', function (event) {
    const keyCode = event.keyCode || event.which;
    if (keyCode === 13) {
      const langCode = $(this).val();
      if (langCode !== '') {
        translateHello(langCode);
      }
    }
  });
});
