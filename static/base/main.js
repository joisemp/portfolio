// Update Year automatically
document.getElementById('year').innerHTML = new Date().getFullYear()

// Toogle the image filter
function toogleImgFilter(id) {
    var x = document.getElementById(id);
    if (x.style.filter === "none") {
        x.style.filter = "grayscale(1)";
    } else {
        x.style.filter = "none";
    }
}

// Go back to the previous page
function goBack() {
    window.history.back();
}