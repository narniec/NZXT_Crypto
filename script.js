$(document).ready(function(){
    // Получить погоду для Москвы
    $.ajax({
        url: "https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=YOUR_API_KEY&units=metric&lang=ru",
        dataType: "json",
        success: function(data) {
            var temp = data.main.temp.toFixed(1);
            var description = data.weather[0].description;
            var icon = data.weather[0].icon;
            $("#temp").text(temp);
            $("#description").text(description);
            $("#icon").attr("src", "https://openweathermap.org/img/wn/" + icon + "@2x.png");
        }
    });
    // Получить дату и время
    var date = new Date();
    var day = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    $("#date").text(day + "." + month + "." + year);
    $("#time").text(hours + ":" + minutes + ":" + seconds);
});
