$(document).ready(function(e) {
	var companies = [];
	$.get("data.csv", function(response) {
		var data = response.split('Company,Link,Time to apply');
        var comps = data[1].split("\r")
        for (var i = 0; i < comps.length; i++) {
            c = comps[i].split(",")
            if(c[0] != ""){
            addComp(c[0].trim(), c[1].trim(), parseInt(c[2]))   
                }
        }
    })
})

function addComp(name, link, time){
    var item = "<tr><td><a target='_blank' href='" + link + "'>" + name + "</a></td></tr>"
    if (time <= 1){
        $("#1-min > tbody").append(item)
    }
    else if (time <= 5){
        $("#5-min > tbody").append(item)
    }
    else if (time <= 10){
        $("#10-min > tbody").append(item)
    }
    else{
        $("#11-min > tbody").append(item)
    }
}