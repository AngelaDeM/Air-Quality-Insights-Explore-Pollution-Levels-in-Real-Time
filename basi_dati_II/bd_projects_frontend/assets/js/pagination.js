// Definisci il numero di righe da visualizzare per pagina
var rowsPerPage = 10;

// Funzione per mostrare le righe corrispondenti alla pagina specificata
function showPage(pageNum) {
  var rows = $("#data-table tbody").find("tr");
  var start = (pageNum - 1) * rowsPerPage;
  var end = start + rowsPerPage;

  rows.hide();
  rows.slice(start, end).show();
}

// Funzione per generare i controlli di paginazione
function createPagination() {
  var rows = $("#data-table tbody").find("tr");
  var numPages = Math.ceil(rows.length / rowsPerPage);

  var paginationHtml = "";
  for (var i = 1; i <= numPages; i++) {
    paginationHtml += '<button onclick="showPage(' + i + ')">' + i + '</button>';
  }

  $("#pagination").html(paginationHtml);
}
// Delegazione degli eventi per i pulsanti di paginazione
$(document).on("click", ".pagination-button", function() {
  var pageNum = parseInt($(this).text());
  showPage(pageNum);
});

// All'avvio del documento, inizializza la paginazione
$(document).ready(function() {
  showPage(1);
  createPagination();
});
// All'avvio del documento, inizializza la paginazione
$(document).ready(function() {
  showPage(1);
  createPagination();
});
