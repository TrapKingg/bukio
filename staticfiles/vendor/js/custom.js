$('#id_email').change(function(){
    var form = $(this).closest("form");
    $.ajax({
      url: form.attr("data-validate-email-url"),
      data: form.serialize(),
      dataType: 'json',
      success: function(data){
        if (data.is_taken){
          alert(data.error_message)
        }
      }
    })
});
