let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
            if (this.status == 200) {
                // Success: Display the response text
                let response = JSON.parse(xhttp.responseText); // Parse the JSON response
                document.getElementById("system_response").innerHTML = response.response;
            } else {
                // Error: Display the error message
                let response = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = response.response || "An error occurred!";
            }
        }
    };
    xhttp.open("GET", `/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`, true);
    xhttp.send();
};
