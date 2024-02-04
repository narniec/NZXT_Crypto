$(document).ready(function(){
    // Получить погоду для Москвы
    $.ajax({
        url: "https://api.gismeteo.ru/weather-by-city/212221",
        dataType: "json",
        success: function(data) {
            var temp = data.temperature;
            var description = data.description;
            var icon = data.icon;
            $("#temp").text(temp);
            $("#description").text(description);
            $("#icon").attr("src", "https://www.gismeteo.ru/weather-icons/" + icon + ".png");
        }
    });
});
