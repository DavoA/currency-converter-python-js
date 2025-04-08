let convertedValue;

function convertCurrency() {
    let fromCurrency = document.getElementById('fromCurrency').value
    let toCurrency = document.getElementById('toCurrency').value
    let amount = document.getElementById('amount').value
    let requestedCurrencies = [fromCurrency, toCurrency, amount]
    fetch('/convert', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ expression: requestedCurrencies })
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(`Error: ${data.error}`);
            }
            else {
                convertedValue = data.result.toString();
                document.getElementById('conversionResult').innerHTML = 'Converted Amount: ' + convertedValue;
            }
        })
        .catch(() => {
            alert('Error with conecting to server');
        });
    return;
}