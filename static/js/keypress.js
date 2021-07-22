document.body.addEventListener("keypress", function (event) {
    if (event.key === "q" || event.key === "Q") {
        window.location.replace("/");
    }
    else {
        if (event.key === "h" || event.key === "H") {
            //alert('Want to know me more? Feel free to drop a message!');
            //location.href("#exampleModal");
            document.getElementById("modaltrigger").click();
        }
    }
});
