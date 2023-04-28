$.get('https://stefanbohacek.com/hellosalut/?lang=fr', (data) => {
  $('DIV#hello').text(data.hello);
});
