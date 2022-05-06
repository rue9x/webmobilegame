
function city_onload() {
    console.log("Loaded.")
    var pd;
    pd = document.getElementById("djangoData").value;
    pd = JSON.parse(JSON.parse(pd)) // Yeah, it needs DOUBLE PARSIN'.
    document.getElementById("djangoData").remove() // Get rid of that pesky element that reveals us to the player. They'll still be able to see it using View -> Source, but harder to automate now.
    window.playerData = pd;
}
    