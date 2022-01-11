$('form[name="file-form"]').on('submit', function () {
    $('#overlay').addClass('overlay');
    $('#spinner').removeClass('d-none');
});