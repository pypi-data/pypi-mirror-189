/* check/nocheck checkbox */
$('tbody :checkbox').change(function () {
    $(this).closest('tr').toggleClass('selected-row', this.checked);
});

$('thead :checkbox').change(function () {
    $('tbody :checkbox').prop('checked', this.checked).trigger('change');
});

/*show/hide menu*/
$('#menu-button').click(function () {
    $('#menu').toggleClass('hide mobile');
});



// add asterisk to required fields
document.querySelectorAll('input[required]').forEach(e => {
    e ? e.parentElement.classList.add('required-input') : null;
})