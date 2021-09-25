// filter = search

function mySearch() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}



// DELETE COURSE
const URL = window.location.href
$('.deleteProfessor').click(function() {
    const data = {
    action:'delete',
    professor_name:this.name
}
    jQuery.post(URL,data,function(data,status){
        console.log(`data -> ${data} | status -> ${statuc}`)
    })
    setTimeout(function () {
            window.location.reload()

    }, 500);
});
//