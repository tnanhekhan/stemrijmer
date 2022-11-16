const SpeechRecogniton = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecogniton();

recognition.lang = 'nl-NL';
recognition.continous = true;
recognition.interimResults = true;
recognition.maxAlternatives = 10;

const sleep = ms => new Promise(r => setTimeout(r, ms));


function startRecognition() {
    const to_speak = new SpeechSynthesisUtterance("Zeg een woord!");
    window.speechSynthesis.speak(to_speak);

    sleep(2000).then(() => {
        recognition.start()
        document.getElementById("speech-output").innerHTML = "";
    });
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
        .then(response => response.text())
        .then(data => {
            sleep(1000)
                .then(() => {
                    const to_speak = new SpeechSynthesisUtterance(data);
                    window.speechSynthesis.speak(to_speak);
                });

            document.getElementById("speech-output").insertAdjacentHTML("beforeend", data);
        })
        .catch(error => {
            document.getElementById("speech-output").insertAdjacentHTML("beforeend", "<li>Geen rijmende woorden gevonden </li>");
        });

    final_result = "";
}

document.getElementById("wotd-button").onclick = () => {
    let wotd = document.getElementById("wotd").innerHTML;
    let formData = new FormData();

    const to_speak = new SpeechSynthesisUtterance("Wat rijmt er op, " + wotd + "?");
    window.speechSynthesis.speak(to_speak);

    formData.append('query', wotd);
    fetch('/rhyme', {method: 'POST', body: formData})
        .then(response => response.text())
        .then(data => {
            const to_speak = new SpeechSynthesisUtterance(data);
            window.speechSynthesis.speak(to_speak);

            document.getElementById("wotd-result").insertAdjacentHTML("beforeend", data);

        })
        .catch(error => {
            document.getElementById("wotd-result").insertAdjacentHTML("beforeend", "<li>Geen rijmende woorden gevonden </li>");
        });
}
