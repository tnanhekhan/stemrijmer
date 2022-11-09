const SpeechRecogniton = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecogniton();

recognition.lang = 'nl-NL';
recognition.continous = true;
recognition.interimResults = true;
recognition.maxAlternatives = 10;

function startRecognition() {
    recognition.start()
    document.getElementById("speech-output").innerHTML = "";
}

let final_result;
recognition.onresult = (event) => {
    if (event.results !== undefined) {

        let top_result = event.results[0][0].transcript;
        document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li><i>GEDETECTEERD: " + top_result + "</i></li>");
        final_result = top_result;
    }
}

recognition.onstart = (event) => {
    document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li><strong>Opname gestart!</strong></li>");
}

recognition.onspeechstart = (event) => {
    document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li><strong>Stem gedetecteerd!</strong></li>");

}

recognition.onspeechend = (event) => {
    document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li><strong>Stem niet meer gedetecteerd!</strong></li>");

}

recognition.onend = (event) => {
    document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li><strong>Opname gestopt!</strong></li>");
    document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li><i>Wat rijmt er op <strong>" + final_result + "</strong>?</i></li>");

    let formData = new FormData();
    formData.append('query', final_result);
    fetch('/rhyme', {method: 'POST', body: formData})
        .then(response => response.json())
        .then(data => {
            document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li><i>Dit rijmt op <strong>" + final_result + "</strong>:</i></li>");
            for (let i = 0; i < data.length; i++) {
                document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li>" + data[i] + "</li>");
            }
        })
        .catch(error => {
            document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li>Geen rijmende woorden gevonden </li>");
        });

    final_result = "";
}

document.getElementById("wotd-button").onclick = () => {
    let wotd = document.getElementById("wotd").innerHTML;
    let formData = new FormData();
    formData.append('query', wotd);
    fetch('/rhyme', {method: 'POST', body: formData})
        .then(response => response.json())
        .then(data => {
            document.getElementById("wotd-result").insertAdjacentHTML("beforeend", "<li><i>Dit rijmt op <strong>" + wotd
                + "</strong>:</i></li>");
            for (let i = 0; i < data.length; i++) {
                console.log(data[i])
                document.getElementById("wotd-result").insertAdjacentHTML("beforeend", "<li>" + data[i] + "</li>");
            }
        })
        .catch(error => {
            document.getElementById("wotd-result").insertAdjacentHTML("beforeend", "<li>Geen rijmende woorden gevonden </li>");
        });
}
