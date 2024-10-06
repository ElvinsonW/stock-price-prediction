document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-input');

    form.onsubmit = async function(e) {
        e.preventDefault();

        const formData = new FormData(form);
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        document.getElementById('predicted-title').style.display="block";
        document.getElementById('predicted-value').innerText = result.prediction;
        document.getElementById('none').style.display="none";
        document.getElementsByClassName('predicted-result').style.justifyContent = "start";
    };
});
