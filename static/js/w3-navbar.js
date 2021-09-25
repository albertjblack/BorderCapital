function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "mytopnav") {
      x.className += " responsive";
    } else {
      x.className = "mytopnav";
    }
  }
