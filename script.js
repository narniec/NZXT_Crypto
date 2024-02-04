$(document).ready(function() {
    // Функция для обновления курса биткоина
    function updatePrice() {
        $.ajax({
            url: "https://api.coindesk.com/v1/bpi/currentprice/BTC.json",
            success: function(data) {
                var price = data.bpi.USD.rate_float;
                $("#price").text("$" + price.toFixed(2));
            }
        });
    }

    // Обновление курса биткоина каждые 5 секунд
    setInterval(updatePrice, 5000);

    // Запуск обновления курса
    updatePrice();
});
