
function analyze() {
    const skills = document.getElementById("skills").value.split(",");

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ skills: skills })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML = `
            <h3>Recommended Career: ${data.recommended_career}</h3>
            <p><b>Missing Skills:</b> ${data.missing_skills.join(", ")}</p>
        `;
    });
}
