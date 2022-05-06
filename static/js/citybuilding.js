const buildinglocked = "lock.png" // -1
const building0 = "not_loaded.png"; // 0
const building1 = "townhall.png";
const building2 = "blacksmith.png";
const building3 = "armorsmith.png";
const building4 = "goldmine.png";
const building5 = "necropolis.png";
const building6 = "barracks.png";
const building7 = "sacrafice.png";
const building8 = "castle.png";

function city_onload() {
  console.log("Loaded.")
  var pd;
  pd = document.getElementById("djangoData").value;
  pd = JSON.parse(JSON.parse(pd)) // Yeah, it needs DOUBLE PARSIN'.
  document.getElementById("djangoData").remove() // Get rid of that pesky element that reveals us to the player. They'll still be able to see it using View -> Source, but harder to automate now.
  window.playerData = pd;
  window.staticData = document.getElementById("staticData").value;
  update_plots();
}

function update_plots() {
  for (let i in playerData.plots) {
    switch (playerData.plots[i]) {
    case -1:
      document.getElementById("i" + i).src = staticData + buildinglocked;
      break;
    case 0:
      document.getElementById("i" + i).src = staticData + building0;
      break;
    case 1:
      document.getElementById("i" + i).src = staticData + building1;
      break;
    case 2:
      document.getElementById("i" + i).src = staticData + building2;
      break;
    case 3:
      document.getElementById("i" + i).src = staticData + building3;
      break;
    case 4:
      document.getElementById("i" + i).src = staticData + building4;
      break;
    case 5:
      document.getElementById("i" + i).src = staticData + building5;
      break;
    case 6:
      document.getElementById("i" + i).src = staticData + building6;
      break;
    case 7:
      document.getElementById("i" + i).src = staticData + building7;
      break;
    case 8:
      document.getElementById("i" + i).src = staticData + building8;
      break;
    default:
      break;
    }
  }

  console.log("Updated plots.");
}