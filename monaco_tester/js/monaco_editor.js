$.getJSON("../../parser/colorMap.json", function(json) {
    const entries = Object.entries(json)
    for (const [ID, color] of entries) {
        element = document.createElement("div");
        element.classList.add("element");
        if (ID.charAt(0) == "c"){
            element.innerHTML += ID + ": " + color;
            element.style.backgroundColor = "#" + color;
        }

        document.getElementById("containerColors").appendChild(element);
    }
});