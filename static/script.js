async function analyzeResume() {

    const data = {
        experience: parseInt(document.getElementById("experience").value),
        projects: parseInt(document.getElementById("projects").value),
        skills_score: parseInt(document.getElementById("skills").value),
        certifications: parseInt(document.getElementById("certifications").value),
        education_level: parseInt(document.getElementById("education").value)
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerText = result.result;
}
