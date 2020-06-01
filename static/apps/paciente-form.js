$(function () {

  /* Functions */

  var loadForm = function (e) {

    e.preventDefault();

    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-cliente .modal-content").html("");
        $("#modal-cliente").modal("show");
      },
      success: function (data) {
        $("#modal-cliente .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#cliente-table tbody").html(data.html_cliente_list);
          $("#modal-cliente").modal("hide");
        }
        else {
          $("#modal-cliente .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create cliente
  $(".js-create-cliente").click(loadForm);
  $("#modal-cliente").on("submit", ".js-cliente-create-form", saveForm);

  // Update cliente
  $("#cliente-table").on("click", ".js-update-cliente", loadForm);
  $("#modal-cliente").on("submit", ".js-cliente-update-form", saveForm);

  // Delete cliente
  $("#cliente-table").on("click", ".js-delete-cliente", loadForm);
  $("#modal-cliente").on("submit", ".js-cliente-delete-form", saveForm);

});